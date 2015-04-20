from django.shortcuts import render, render_to_response, RequestContext
import json, certifi, re, urllib3
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Food, User, JadwalKelas, Order, OrderItem, Review, Pembayaran, Restaurant
from django.template import Context, loader
from .forms import *

#from django.template.context_processors import csrf

"""==============================================KEI's (start)==========================================="""
def viewfood(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":	
			food_list2 = Food.objects.all()
			food_list = food_list2.order_by('restoran')
			loop_times = [i+1 for i in range(len(food_list))]
			context = {'food_list':food_list, 'loop_times':loop_times}
			template = "user-interfaces/m_makanan.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)
def managefood(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			food_list2 = Food.objects.all()
			food_list = food_list2.order_by('restoran')
			loop_times = [i+1 for i in range(len(food_list))]
			context = {'food_list':food_list,'loop_times':loop_times}
			template = "user-interfaces/m_makanan_m.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)

def addrestoran(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			form = RestoranForm(request.POST or None)
			if 'simpan' in request.POST:
				if form.is_valid():
					save_it =  form.save(commit=False)
					#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
					nama = form.cleaned_data['nama_restoran']
					save_it.save()
					return HttpResponseRedirect('/add/food/')
			#		return list(request, message="Makanan berhasil ditambahkan")
			elif 'batal' in request.POST:
				return HttpResponseRedirect('/add/food/') #jika batal kembali ke halaman view
			context = {"form":form,}
			template = "user-interfaces/tambahrestoran.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)

#menambahkan nama makanan ke dalam database
def addfood(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			food_list = Food.objects.all()
			form = FoodForm(request.POST or None)
			if 'simpan' in request.POST:
				if form.is_valid():
					save_it =  form.save(commit=False)
					notifikasi = "Makanan baru berhasil disimpan"
					#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
					#nama = form.cleaned_data['nama_makanan']
					save_it.save()
					form.clean()
					context = {"food_list":food_list, 'notifikasi':notifikasi}
					template = "user-interfaces/m_makanan.html"
					return render(request, template, context)
					#return HttpResponseRedirect('/add/food/')
			#		return list(request, message="Makanan berhasil ditambahkan")
			elif 'batal' in request.POST:
				return HttpResponseRedirect('/view/food/') #jika batal kembali ke halaman view
			context = {"form":form, 'food_list':food_list}
			template = "user-interfaces/daftarmakanan.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)

def deleteFood(request):
	if 'username' not in request.session:
		return index(request)
	else:
		food_list = Food.objects.all()
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			if request.method == 'POST' :
				food_list2 = Food.objects.filter(id=request.POST.get("delete"))
				food_list2.delete()
			notifikasi = "Makanan telah dihapus"
			context = {"food_list":food_list, 'notifikasi':notifikasi,}
			template = "user-interfaces/m_makanan_m.html"				
			return render(request, template, context)
			#return HttpResponseRedirect('/manage/food/')
		else:
			return redirect_to_base(request, user2)

def updateFood(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			food_list = Food.objects.filter(id=request.POST.get("edit"))
			context = {"food_list":food_list,}
			template = "user-interfaces/updatemakanan.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)

def updateFoodSave(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Sekretariat":
			if 'simpan' in request.POST:
					restoran_list = Restaurant.objects.all()
					food_list = Food.objects.all()
					food_list = food_list.order_by('restoran')
					food2 = Food.objects.filter(id=request.POST.get("restoran"))
					food3 = Food.objects.filter(id=request.POST.get("restoran"), nama_makanan=request.POST.get("nama_makanan"))
					if food3.exists():
						notifikasi = "Nama dan restoran sudah tersedia"
						context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
						template = "user-interfaces/m_makanan_m.html"
						return render(request, template, context)
					else:
						notifikasi = "Perubahan telah disimpan"
						food2.update(nama_makanan=request.POST.get("nama_makanan"))
						context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
						template = "user-interfaces/m_makanan_m.html"				
						return render(request, template, context)
			#		return list(request, message="Makanan berhasil diubah")
			elif 'batal' in request.POST:
				return HttpResponseRedirect('/manage/food/') #jika batal kembali ke halaman view
		else:
			return redirect_to_base(request, user2)
		
# def updateFoodSave(request):
# 	if 'simpan' in request.POST:
# 			notifikasi = "Perubahan telah disimpan"
# 			food_list = Food.objects.all()
# 			food_list = food_list.order_by('restoran')
# 			food2 = Food.objects.filter(id=request.POST.get("restoran"))
# 			food2.update(nama_makanan=request.POST.get("nama_makanan"))
# 			context = {"food_list":food_list, 'notifikasi':notifikasi}
# 			template = "user-interfaces/m_makanan.html"
# 			return render(request, template, context)
# 			#return HttpResponseRedirect('/view/food/')
# 	#		return list(request, message="Makanan berhasil diubah")
# 	elif 'batal' in request.POST:
# 		return HttpResponseRedirect('/view/food/') #jika batal kembali ke halaman view	
"""
def updateFoodSave(request):
	if 'simpan' in request.POST:
			restoran_list = Restaurant.objects.all()
			food_list = Food.objects.all()
			food_list = food_list.order_by('restoran')
			food2 = Food.objects.filter(id=request.POST.get("restoran"))
			if food2.exists():
				notifikasi = "Nama makanan dan restoran sudah tersedia"
				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
				template = "user-interfaces/m_makanan_m.html"
				return render(request, template, context)
			else:
				notifikasi = "Perubahan telah disimpan"
				food2.update(nama_makanan=request.POST.get("nama_makanan"))
				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
				template = "user-interfaces/m_makanan_m.html"
				return render(request, template, context)
	elif 'batal' in request.POST:
		return HttpResponseRedirect('/manage/food/') #jika batal kembali ke halaman kelola makanan	
"""
	
"""==============================================KEI's (end)==========================================="""
	
"""==============================================Hamka's (start)==========================================="""

def editUser(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			user_list = User.objects.all()
			context = {'user_list':user_list}
			template = "user-interfaces/p_akun.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)
	
def lihatUser(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			user_list = User.objects.all()
			context = {'user_list':user_list}
			template = "user-interfaces/lihat_akun.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)
	
def addUser(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			user_list = User.objects.all()
			form = UserForm(request.POST or None)
			if 'simpan' in request.POST:
				if form.is_valid():
					save_it =  form.save(commit=False)
					#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
					#nama = form.cleaned_data['nama_makanan']
					save_it.save()
					return HttpResponseRedirect('/view/user/')
			#		return list(request, message="User berhasil ditambahkan")
			elif 'batal' in request.POST:
				return HttpResponseRedirect('/view/user/') #jika batal kembali ke halaman view
			context = {"form":form, 'user_list':user_list}
			template = "addUser.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)
#	
def deleteUser(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			if request.method == 'POST' :
				user_list = User.objects.filter(username=request.POST.get("delete"))
				user_list.delete()
			return HttpResponseRedirect('/view/user/')
		else:
			return redirect_to_base(request, user2)
#		

def updateUser(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			request.session['selected_username'] = request.POST.get("edit")
			user_list = User.objects.filter(username=request.session['selected_username'])
			context = {"user_list":user_list,}
			template = "user-interfaces/updateUser.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user2)

def updateUserSave(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user2= ''
		for f in user:
			user2 = f
		if user2.role=="Admin":
			if 'simpan' in request.POST:
					user2 = User.objects.filter(username=request.session['selected_username'])
					user2.update(username=request.POST.get("username"))
					user2.update(role=request.POST.get("role"))
					user2.update(nama_user=request.POST.get("nama"))
					return HttpResponseRedirect('/view/user/')
			elif 'batal' in request.POST:
				return HttpResponseRedirect('/view/user/') #jika batal kembali ke halaman view
		else:
			return redirect_to_base(request, user2)	
"""==============================================Hamka's (end)==========================================="""



"""==============================================AWAL FADLI==========================================="""
	

	
"""==============================================AKHIR FADLI==========================================="""

'''
def addUSer(request) :
	User = User.objects.all()
	form = UserForm(request.POST or None)
	if 'simpan' in request.POST:
		if form.is_valid():
			save_it =  form.save(commit=False)
			
			nama = form.cleaned_data['nama']
			
			save_it.save()
			return HttpResponseRedirect('/view/user/')
			
	elif 'batal' in request.POST:
		return HttpResponseRedirect('/view/user/')
	context = {"form":form, 'food_list':food_list}
	template = "user-interfaces/p_akun.html"
	return render(request, template, context)
'''

"""==============================================AWAL ariel==========================================="""
def addOrder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			form = OrderItemForm(request.POST or None)
			context = {'form':form}
			template = "user-interfaces/addorder.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)



def viewOrder1(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			if user_obj.username == request.session['username']:
				u = user_obj.nama_user
				order = Order.objects.filter(dosen = u, waktu_order = dateNow)
				#order1 = order.filter(waktu_order = dateNow )
				orderitem = OrderItem.objects.filter(order = order)
				context = {'orderitem': orderitem,}
				template = "user-interfaces/lihatorder.html"
				return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)
			
def viewOrder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			if user_obj.username == request.session['username']:
				u = user_obj.nama_user #berisi nama user dari user yang login
				orders = Order.objects.filter(dosen=user_obj, waktu_order=dateNow) #query set yang difilter berdasarkan dosen yg login dan waktu sekarang
				o = ''
				for x in orders:
					o = x #mengambil object dari query set
				orderitem_list = OrderItem.objects.filter(order = o) #query set order item dari filter object order
				order = Order.objects.filter(dosen = u, waktu_order = dateNow) # query set order yang difilter based on dosen yg skrg dan waktu skrg
				orderitem = OrderItem.objects.filter(order = order) #bandingin atribut order item dengan hasil query set order
				context = {'orderitem_list': orderitem_list,}
				template = "user-interfaces/lihatorder.html"
				return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)

def editOrder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			if user_obj.username == request.session['username']:
				u = user_obj.nama_user #berisi nama user dari user yang login
				orders = Order.objects.filter(dosen=user_obj, waktu_order=dateNow) #query set yang difilter berdasarkan dosen yg login dan waktu sekarang
				o = ''
				for x in orders:
					o = x #mengambil object dari query set
				orderitem_list = OrderItem.objects.filter(order = o) #query set order item dari filter object order
				order = Order.objects.filter(dosen = u, waktu_order = dateNow) # query set order yang difilter based on dosen yg skrg dan waktu skrg
				orderitem = OrderItem.objects.filter(order = order) #bandingin atribut order item dengan hasil query set order
				context = {'orderitem_list': orderitem_list,}
				template = "user-interfaces/editorder.html"
				return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)

def deleteOrder1(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			if user_obj.username == request.session['username']:
				u = user_obj.nama_user #berisi nama user dari user yang login
				orders = Order.objects.filter(dosen=user_obj, waktu_order=dateNow) #query set yang difilter berdasarkan dosen yg login dan waktu sekarang
				o = ''
				for x in orders:
					o = x #mengambil object dari query set
				orderitem_list = OrderItem.objects.filter(order = o) #query set order item dari filter object order
				order = Order.objects.filter(dosen = u, waktu_order = dateNow) # query set order yang difilter based on dosen yg skrg dan waktu skrg
				orderitem = OrderItem.objects.filter(order = order) #bandingin atribut order item dengan hasil query set order
			notifikasi = "Pesanan telah dihapus"
			if request.method == 'POST' :
				order_list = OrderItem.objects.filter(id=request.POST.get("delete"))
				order_list.delete()
				context = {'orderitem_list': orderitem_list,'notifikasi':notifikasi}
				template = "user-interfaces/editorder.html"
				return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)
	
def deleteOrder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			notifikasi = "Pesanan telah dihapus"
			orderitem_list = OrderItem.objects.all()
			order = Order.objects.filter(dosen = user_obj)
			order = order.filter(waktu_order = dateNow )
			orderitem = OrderItem.objects.filter(order = order)
			if request.method == 'POST' :
				order_list = OrderItem.objects.filter(id=request.POST.get("delete"))
				order_list.delete()
			context = {"orderitem_list":orderitem_list, 'notifikasi':notifikasi,}
			template = 'user-interfaces/editorder.html'				
			return render(request, template, context)
			#return HttpResponseRedirect('/manage/food/')
		else:
			return redirect_to_base(request, user_obj)
			
def daftarpesanan(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Sekretariat":
			#if user_obj.username == request.session['username']:
				#u = user_obj.nama_user #berisi nama user dari user yang login
				#orders = Order.objects.filter(dosen=user_obj, waktu_order=dateNow) #query set yang difilter berdasarkan dosen yg login dan waktu sekarang
				#o = ''
				#for x in orders:
				#	o = x #mengambil object dari query set
				#orderitem_list = OrderItem.objects.filter(order = o) #query set order item dari filter object order
				#order = Order.objects.filter(dosen = u, waktu_order = dateNow) # query set order yang difilter based on dosen yg skrg dan waktu skrg
				#orderitem = OrderItem.objects.filter(order = order) #bandingin atribut order item dengan hasil query set order
				#context = {'orderitem' : orderitem,}
			#merupakan list order yang dilakukan hari ini
			user2 = User.objects.filter( role = 'Dosen') # berisi nama nama user dalam bentuk query
			user_obj2 =''
			for f in user2:
				user_obj2 = f # berisi nama nama user dalam bentuk objek
			u = user_obj2.nama_user
			orders = Order.objects.filter(waktu_order=dateNow)
			a = ''
			
			for x in orders:
				orderitem_list = OrderItem.objects.filter(order = x)
				a = x #mengambil object dari query set
			if a != '':				
				orderitem_list = OrderItem.objects.filter(order = a)
				order4 = Order.objects.filter(dosen = u, waktu_order = dateNow)
				orderitem = OrderItem.objects.filter(order = order4)
				context = {'orderitem' : orderitem}
			else:
				context = ''
			template = "user-interfaces/dp_harian.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)
			



def sekretariataddorder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		form = OForm(request.POST or None)
		form2 = OrderItemForm(request.POST or None)
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		for f in user:
			user_obj = f
		if user_obj.role=="Sekretariat":
			if form.is_valid() and form2.is_valid():
				save_it =  form.save(commit=False)
				save_it.save()
				save_it =  form2.save(commit=False)
				save_it.save()
			context = {'form' : form, 'form2' : form2 }
			template = "user-interfaces/sp_makanan.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)



def historyOrder(request):
	orderitem_list = OrderItem.objects.all() 
	u = loader.get_template('user-interfaces/r_pemesanan.html')
	b = Context({'orderitem_list': orderitem_list,})
	return HttpResponse(u.render(b))
	#return render(request, "user-interfaces/r_pemesanan.html",'')

def va_dosen(request):
	return render(request, "user-interfaces/va_dosen.html",'')

	
#------------------------------------LOG IN ----------------------------------------#
def login(request):								
	if request.method == 'POST':
		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(),)
		username = request.POST['username']
		password = request.POST['password']
		req = http.request("POST", "https://apps.cs.ui.ac.id/webservice/login_ldap.php?username=" + username + "&password=" + password)
		temp = req.data
		decoder = temp.decode('utf-8')
		user = json.loads(decoder)
		status = user["state"]
		if status == 1: 	
			username2 = username
			is_registered =  User.objects.filter(username=username2)
			if not is_registered:
				return HttpResponse("Anda Gagal Login SiPeMa")
			else:	
				request.session['username']= username2
				user = ''
				for f in is_registered:
					user = f		
				"""if user.role=='Sekretariat':
					t = loader.get_template('base_sekretariat.html')
					c = RequestContext(request, {'sekretariat':username2})
					return HttpResponse(t.render(c))
				elif user.role=='Dosen':	
					t = loader.get_template('base_dosen.html')
					c = RequestContext(request, {'dosen':username2})
					return HttpResponse(t.render(c))					
				elif user.role=='Admin':
					t = loader.get_template('base_admin.html')
					c = RequestContext(request, {'dosen':username2})
					return HttpResponse(t.render(c))
				"""
				return redirect_to_base(request, user)	
		else:
			return HttpResponse("Anda Gagal Login SSO UI")


def logout(request):
	request.session.flush()
	t = loader.get_template('index.html')
	c = Context('')
	return HttpResponse(t.render(c))

	
def index(request):
	if 'username' not in request.session:
		return logout(request)
	else:
		is_registered = User.objects.filter(username=request.session['username'])
		user = ''
		for f in is_registered:
			user = f
		"""if user.role=='Sekretariat':
			t = loader.get_template('user-interfaces/home_sekretariat.html')
			c = RequestContext(request, {'sekretariat':username2})
			return HttpResponse(t.render(c))
		elif user.role=='Dosen':	
			request.session.flush()
			return HttpResponse("Dosen")		
		elif user.role=='Admin':
			return viewUser(request)
		"""
		return redirect_to_base(request, user)
			
def redirect_to_base(request, user):		
	username2 = user.username
	if user.role=='Sekretariat':
		t = loader.get_template('base/base_sekretariat.html')
		c = RequestContext(request, {'sekretariat':username2})
		#return HttpResponse(t.render(c))
		return daftarpesanan(request)	
	elif user.role=='Dosen':	
		t = loader.get_template('user-interfaces/addorder.html')
		c = RequestContext(request, {'dosen':username2})
		#return HttpResponse(t.render(c))
		return addOrder(request)					
	elif user.role=='Admin':
		t = loader.get_template('user-interfaces/lihat_akun.html')
		c = RequestContext(request, {'dosen':username2})
		#return HttpResponse(t.render(c))
		return lihatUser(request)
