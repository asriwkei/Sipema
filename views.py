from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
# Create your views here.
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import *
from django.template import Context, loader
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
#from django.template.context_processors import csrf

def index(request):
	#food_list = Food.objects.all()
	#return HttpResponse("Hello SiPeMa User")
	t = loader.get_template('user-interfaces/home-login.html')
	c = Context('')
	return HttpResponse(t.render(c))
	
def login(request):
	username = 'username'
	password = 'password'
	if request.method == 'POST':
		username2 = request.POST.get('username')
		password2 = request.POST.get('password')
		if usename == username2:
			t = loader.get_template('user-interfaces/m_makanan.html')
			c = Context('')
			return HttpResponse()
"""
def viewfood(request):
	food_list = Food.objects.all()
	t = loader.get_template('user-interfaces/m_makanan.html')
	c = Context({'food_list': food_list,})
	return HttpResponse(t.render(c))
	#return render(request,"user-interfaces/m_makanan.html",food_list)
"""
"""============================================== KEI's ========================================================="""

def viewfood(request):
    food_list2 = Food.objects.all()
    food_list = food_list2.order_by('restoran')
    loop_times = [i+1 for i in range(len(food_list))]
    context = {'food_list':food_list,'loop_times':loop_times}
    template = "user-interfaces/m_makanan.html"
    return render(request, template, context)

def managefood(request):
    food_list2 = Food.objects.all()
    food_list = food_list2.order_by('restoran')
    loop_times = [i+1 for i in range(len(food_list))]
    context = {'food_list':food_list,'loop_times':loop_times}
    template = "user-interfaces/m_makanan_m.html"
    return render(request, template, context)

def addrestoran(request):
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
		return HttpResponseRedirect('/view/food/') #jika batal kembali ke halaman view
	context = {"form":form,}
	template = "user-interfaces/tambahrestoran.html"
	return render(request, template, context)

#menambahkan nama makanan ke dalam database
def addfood(request):
	food_list = Food.objects.all()
	form = FoodForm(request.POST or None)
	if 'simpan' in request.POST:
		if form.is_valid():
			save_it =  form.save(commit=False)
			notifikasi = "Makanan baru berhasil disimpan"
			#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
			#nama = form.cleaned_data['nama_makanan']
			save_it.save()
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

def deleteFood(request):
	if request.method == 'POST' :
		food_list2 = Food.objects.filter(id=request.POST.get("delete"))
		food_list2.delete()
	return HttpResponseRedirect('/manage/food/')

def updateFood(request):
	food_list = Food.objects.filter(id=request.POST.get("edit"))
	food = Food.objects.get(id=request.POST.get("edit"))
	print food
	restoran_list = Restaurant.objects.all()
	restoran = Restaurant.objects.get(id = food.restoran.id)
	context = {"food_list":food_list,"restoran_list":restoran_list, "restoran":restoran}
	template = "user-interfaces/updatemakanan.html"
	return render(request, template, context)

# def updateFood(request): 
#     instance = get_object_or_404(Food, id=request.POST.get("edit"))
#     form = FoodForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('/manage/food/')
#     return render(request, 'user-interfaces/updatemakanan2.html', {'form': form})

# def updateFoodSave(request):
# 	if 'simpan' in request.POST:
# 			notifikasi = "Perubahan telah disimpan"
# 			restoran_list = Restaurant.objects.all()
# 			food_list = Food.objects.all()
# 			food_list = food_list.order_by('restoran')
# 			food2 = Food.objects.filter(id=request.POST.get("restoran"))
# 			food2.update(nama_makanan=request.POST.get("nama_makanan"))
# 			context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
# 			template = "user-interfaces/m_makanan_m.html"
# 			return render(request, template, context)
# 			#return HttpResponseRedirect('/view/food/')
# 	#		return list(request, message="Makanan berhasil diubah")
# 	elif 'batal' in request.POST:
# 		return HttpResponseRedirect('/view/food/') #jika batal kembali ke halaman view	

# def updateFoodSave(request):
# 	if 'simpan' in request.POST:
# 			restoran_list = Restaurant.objects.all()
# 			food_list = Food.objects.all()
# 			food_list = food_list.order_by('restoran')
# 			# food2 = Food.objects.filter(id=request.POST.get("restoran"))
# 			# food3 = Food.objects.filter(id=request.POST.get("restoran"), nama_makanan=request.POST.get("nama_makanan"))
# 			food = Food.objects.filter(id=request.POST.get("restoran"), nama_makanan=request.POST.get("nama_makanan"))
# 			food2= ''
# 			for f in food:
# 				food2 = f
# 			print food2
# 			#print food3
# 			if not food2:
# 				notifikasi = "Perubahan telah disimpan"
# 				food.update(nama_makanan=request.POST.get("nama_makanan"))
# 				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
# 				template = "user-interfaces/m_makanan_m.html"				
# 				return render(request, template, context)
# 			else:
# 				notifikasi = "Nama dan restoran sudah tersedia"
# 				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
# 				template = "user-interfaces/m_makanan_m.html"
# 				return render(request, template, context)
# 			#return HttpResponseRedirect('/view/food/')
# 	#		return list(request, message="Makanan berhasil diubah")
# 	elif 'batal' in request.POST:
# 		return HttpResponseRedirect('/manage/food/') #jika batal kembali ke halaman view
 #=========================================exclusive update ============================#
def updateFoodSave(request):
	if request.method == "POST":
		restoran_list = Restaurant.objects.all()
		food_list = Food.objects.all()
		food_list = food_list.order_by('restoran')
		restoran = Restaurant.objects.get(id=request.POST.get("restoran"))
		print restoran #ada hasilnya
		print request.POST.get("nama_makanan") #ada hasilnya
		food3 = Food.objects.filter(restoran=restoran, nama_makanan=request.POST.get("nama_makanan"))
		print food3
		if len(food3)>0:
			notifikasi = "Nama dan restoran sudah tersedia"
			context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
			template = "user-interfaces/m_makanan_m.html"				
			return render(request, template, context)
		elif len(food3)==0:
			notifikasi = "Perubahan telah disimpan"
			food2 = Food.objects.filter(id=request.POST.get("simpan"))
			food2.update(nama_makanan=request.POST.get("nama_makanan"))
			context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
			template = "user-interfaces/m_makanan_m.html"				
			return render(request, template, context)

#======================================exclusive update ===================#	

# def updateFoodSave(request):
# 	if 'simpan' in request.POST:
# 			restoran_list = Restaurant.objects.all()
# 			food_list = Food.objects.all()
# 			food3 = Food.objects.get(restoran=request.POST.get("restoran"), nama_makanan=request.POST.get("nama_makanan"))
# 			print food3
# 			if food3.exist():
# 				print "masuk lebih dari 0"
# 				notifikasi = "Nama makanan dan restoran sudah tersedia"
# 				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
# 				template = "user-interfaces/m_makanan_m.html"
# 				return render(request, template, context)
# 			else:
# 				print "masuk kurang dari 1"
# 				notifikasi = "Perubahan telah disimpan"
# 				food3.update(restoran=request.POST.get("restoran"), nama_makanan=request.POST.get("nama_makanan"))
# 				context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
# 				template = "user-interfaces/m_makanan_m.html"
# 				return render(request, template, context)
# 	elif 'batal' in request.POST:
# 		return HttpResponseRedirect('/manage/food/') #jika batal kembali ke halaman kelola makanan	

"""============================================== FADLI's========================================================="""
	
def jadwal_kelas(request):
	jadwal_list = JadwalKelas.objects.all()
	context = {'jadwal_list':jadwal_list}
	template = "user-interfaces/j_dosen.html"
	return render(request, template, context)

def addJadwal(request):
	form = Jadwal_kelasForm(request.POST or None)
	if form.is_valid():
		save_it =  form.save(commit=False)
		save_it.save()
	return render_to_response("addjadwal.html", locals(), context_instance=RequestContext(request))

"""============================================== HAMKA's========================================================="""
# def editUser(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			user_list = User.objects.all()
# 			context = {'user_list':user_list}
# 			template = "user-interfaces/p_akun.html"
# 			return render(request, template, context)
# 		else:
# 			return redirect_to_base(request, user2)
	
# def lihatUser(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			user_list = User.objects.all()
# 			context = {'user_list':user_list}
# 			template = "user-interfaces/lihat_akun.html"
# 			return render(request, template, context)
# 		else:
# 			return redirect_to_base(request, user2)
	
# def addUser(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			user_list = User.objects.all()
# 			form = UserForm(request.POST or None)
# 			if 'simpan' in request.POST:
# 				if form.is_valid():
# 					save_it =  form.save(commit=False)
# 					#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
# 					#nama = form.cleaned_data['nama_makanan']
# 					save_it.save()
# 					return HttpResponseRedirect('/view/user/')
# 			#		return list(request, message="User berhasil ditambahkan")
# 			elif 'batal' in request.POST:
# 				return HttpResponseRedirect('/view/user/') #jika batal kembali ke halaman view
# 			context = {"form":form, 'user_list':user_list}
# 			template = "addUser.html"
# 			return render(request, template, context)
# 		else:
# 			return redirect_to_base(request, user2)
# #	
# def deleteUser(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			if request.method == 'POST' :
# 				user_list = User.objects.filter(username=request.POST.get("delete"))
# 				user_list.delete()
# 			return HttpResponseRedirect('/view/user/')
# 		else:
# 			return redirect_to_base(request, user2)
# #		

# def updateUser(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			request.session['selected_username'] = request.POST.get("edit")
# 			user_list = User.objects.filter(username=request.session['selected_username'])
# 			context = {"user_list":user_list,}
# 			template = "user-interfaces/updateUser.html"
# 			return render(request, template, context)
# 		else:
# 			return redirect_to_base(request, user2)

# def updateUserSave(request):
# 	if 'username' not in request.session:
# 		return index(request)
# 	else:
# 		user = User.objects.filter(username=request.session['username'])
# 		user2= ''
# 		for f in user:
# 			user2 = f
# 		if user2.role=="Admin":
# 			if 'simpan' in request.POST:
# 					user2 = User.objects.filter(username=request.session['selected_username'])
# 					user2.update(username=request.POST.get("username"))
# 					user2.update(role=request.POST.get("role"))
# 					user2.update(nama_user=request.POST.get("nama"))
# 					return HttpResponseRedirect('/view/user/')
# 			elif 'batal' in request.POST:
# 				return HttpResponseRedirect('/view/user/') #jika batal kembali ke halaman view
# 		else:
# 			return redirect_to_base(request, user2)	


"""============================================== ARIEL's========================================================="""

def addOrder(request):
	if 'username' not in request.session:
		return index(request)
	else:
		user = User.objects.filter(username=request.session['username'])
		user_obj =''
		dateNow = datetime.datetime.now().date
		for f in user:
			user_obj = f
		if user_obj.role=="Dosen":
			form = OrderItemForm(request.POST or None)
			if form.is_valid():
				save_it =  form.save(commit=False)
				save_it.save()
				return addOrder(request)
			context = {"form":form}
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
			order = Order.objects.filter(dosen = user_obj)
			order = order.filter(waktu_order = dateNow )
			orderitem = OrderItem.objects.filter(order = order)
			context = {'orderitem': orderitem,}
			template = "user-interfaces/lihatorder.html"
			return render(request, template, context)
		else:
			return redirect_to_base(request, user_obj)

def editOrder(request):
	orderitem_list = OrderItem.objects.all() 
	u = loader.get_template('user-interfaces/editorder.html')
	b = Context({'orderitem_list': orderitem_list,})
	return HttpResponse(u.render(b))

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
			order = Order.objects.filter(dosen = user_obj)
			order = order.filter(waktu_order = dateNow )
			orderitem = OrderItem.objects.filter(order = order)
			if request.method == 'POST' :
				order_list = OrderItem.objects.filter(id=request.POST.get("delete"))
				order_list.delete()
				return HttpResponseRedirect('/manage/order/')
		else:
			return redirect_to_base(request, user_obj)

def daftarpesanan(request):
	order_list = Order.objects.filter(waktu_order = datetime.date.today()) 
	orderitem = OrderItem.objects.filter( order = order_list) #simpan order item oleh dosen yg login pada saat itu
	jadwal_list = JadwalKelas.objects.filter( dosen = order_list) #objek
	context = {'orderitem' : orderitem, 'jadwal_list' : jadwal_list}
	template = "user-interfaces/dp_harian.html"
	return render(request, template, context)

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


# def addOrder(request):
# 	orderitem_list = OrderItem.objects.all()
# 	form = PesananForm()
# 	food_list = Food.objects.all()
	# food_list.order_by('restoran')
	# user = User.objects.filter(username='wahyu.asri')
	# user2= ''
	# for f in user:
	# 	user2 = f
	
	# if Order.objects.filter(waktu_order=datetime.date.today(),dosen=user2).exists():
	# 	#isi order item
	# 	template = 'user-interfaces/addorder.html'
	# 	context = {'form':form,'food_list':food_list, 'orderitem_list':orderitem_list}
	# 	return render(request, template, context)
	# else:
	# 	o = Order(waktu_order=datetime.date.today(),dosen=user2)
	# 	o.save()
		#isi dan simpan orderitem

	# form = OrderItemForm(request.POST or None)
	# if form.is_valid():
	# 	save_it =  form.save(commit=False)
	# 	save_it.save()
	# 	return HttpResponseRedirect('/add/order/')
	# template = 'user-interfaces/addorder.html'
	# context = {'form':form,}
	# return render(request, template, context)

# def addOrder(request):
# 	if 'username' in request.session:
# 		form = OrderItemForm(request.POST or None)
# 		if form.is_valid():
# 			save_it =  form.save(commit=False)
# 			save_it.save()
# 			return HttpResponseRedirect('/add/order/')
# 		template = 'user-interfaces/addorder.html'
# 		context = {'form':form}
# 		return render(request, template, context)

# def viewOrder(request):
# 		request.session['selected_username_dosen']=request.POST.get('view')
# 		username_dosen2= "%s" % (request.session['selected_username_dosen'])
# 		dosen = User.objects.filter(username=username_dosen2)
# 		order_dosen = OrderItem.order.self.dosen.nama_user()
# 		order_list = OrderItem.objects.filter( order_dosen = dosen)
# 		#jadwal_list = JadwalKelas.objects.all()
# 		template = 'user-interfaces/lihatorder.html'
# 		context = {'order_list':order_list, 'sekretariat':username_dosen2}
# 		return render(request, template, context)

# def viewOrder1(request):
# 		user = User.objects.filter(username=request.session['username'])
# 		user_ob = User.objects.all()
# 		for user == user_ob:
# 			nama_user = User.objects.get('nama_user')
# 			user_order_list = Order.objects.get('dosen')
# 			for nama_user in user_order_list :	
# 				orderitem_list = Order_item.objects.all()
# 				context = {'orderitem_list': orderitem_list,}
# 				template = "user-interfaces/lihatorder.html"
# 				return render(request, template, context)
# 		else:
# 			return redirect_to_base(request, user2)

# def editOrder(request):
# 	orderitem_list = OrderItem.objects.all() 
# 	u = loader.get_template('user-interfaces/editorder.html')
# 	b = Context({'orderitem_list': orderitem_list,})
# 	return HttpResponse(u.render(b))

# def historyOrder(request):
# 	orderitem_list = OrderItem.objects.all() 
# 	u = loader.get_template('user-interfaces/r_pemesanan.html')
# 	b = Context({'orderitem_list': orderitem_list,})
# 	return HttpResponse(u.render(b))
# 	#return render(request, "user-interfaces/r_pemesanan.html",'')

# def daftarpesanan(request):
# 	jadwal_list= JadwalKelas.objects.all()
# 	order_list= JadwalKelas.objects.all()
# 	return render(request, "user-interfaces/dp_harian.html",'')

# def sekretariataddorder(request):
# 	form = UserForm(request.POST or None)
# 	if form.is_valid():
# 		save_it =  form.save(commit=False)
# 		save_it.save()
# 	return render_to_response("user-interfaces/sp_makanan.html", locals(), context_instance=RequestContext(request))

# def va_dosen(request):
# 	return render(request, "user-interfaces/va_dosen.html",'')
