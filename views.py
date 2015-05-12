from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
# Create your views here.
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import *
from django.template import Context, loader
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
#from django.template.context_processors import csrf

def viewfood(request):
    food_list = Food.objects.all().order_by('restoran')
    restoran = Restaurant.objects.all()
    context = {'food_list':food_list,'restoran':restoran}
    template = "user-interfaces/m_makanan.html"
    return render(request, template, context)

def filter_food(request):
	if request.method == 'POST' :
		food_list = Food.objects.none()
		resto_id = request.POST.get('restoran')
		print resto_id
		if resto_id == 'all':
			print "masuk all"
			food_list = Food.objects.all().order_by('restoran')
		else:
			resto = Restaurant.objects.get(id=resto_id)
			print "masuk else"
			print resto
			food_list = Food.objects.filter(restoran=resto)
		restoran =Restaurant.objects.all()
		context = {'food_list':food_list, 'restoran':restoran}
		template = "user-interfaces/m_makanan.html"
		return render(request, template, context)

def filter_food_manage(request):
	if request.method == 'POST' :
		food_list = Food.objects.none()
		resto_id = request.POST.get('restoran')
		print resto_id
		if resto_id == 'all':
			print "masuk all"
			food_list = Food.objects.all().order_by('restoran')
		else:
			resto = Restaurant.objects.get(id=resto_id)
			print "masuk else"
			print resto
			food_list = Food.objects.filter(restoran=resto)
		restoran =Restaurant.objects.all()
		context = {'food_list':food_list, 'restoran':restoran}
		template = "user-interfaces/m_makanan_m.html"
		return render(request, template, context)

def managefood(request):
    food_list = Food.objects.all().order_by('restoran')
    restoran = Restaurant.objects.all()
    context = {'food_list':food_list, 'restoran':restoran}
    template = "user-interfaces/m_makanan_m.html"
    return render(request, template, context)

def managerestoran(request):
    restoran = Restaurant.objects.all()
    context = {'restoran':restoran}
    template = "user-interfaces/m_restoran.html"
    return render(request, template, context)

def addrestoran(request):
	form = RestoranForm(request.POST or None)
	if 'simpan' in request.POST:
		if form.is_valid():
			save_it =  form.save(commit=False)
			nama = form.cleaned_data['nama_restoran']
			save_it.save()
			return HttpResponseRedirect('/add/food/')
	elif 'batal' in request.POST:
		return HttpResponseRedirect('/view/food/') #jika batal kembali ke halaman view
	context = {"form":form,}
	template = "user-interfaces/tambahrestoran.html"
	return render(request, template, context)

def deleteRestoran(request):
	if request.method == 'POST' :
		restoran_list = Restaurant.objects.filter(id=request.POST.get("delete"))
		restoran_list.delete()
	return HttpResponseRedirect('/manage/restoran/')

def updateRestoran(request):
	restoran = Restaurant.objects.filter(id=request.POST.get("edit"))
	context = {"restoran":restoran}
	template = "user-interfaces/update-restoran.html"
	return render(request, template, context)

def updateRestoranSave(request):
	if request.method == "POST":
		restoran = Restaurant.objects.all()
		resto = Restaurant.objects.filter(nama_restoran=request.POST.get("nama_restoran"))
		if len(resto)>0:
			notifikasi = "Restoran sudah tersedia"
			context = {"notifikasi":notifikasi, "restoran":restoran}
			template = "user-interfaces/m_restoran.html"				
			return render(request, template, context)
		elif len(resto)==0:
			notifikasi = "Perubahan telah disimpan"
			restoran_list = Restaurant.objects.filter(id=request.POST.get("simpan"))
			restoran_list.update(nama_restoran=request.POST.get("nama_restoran"))
			context = {"notifikasi":notifikasi, "restoran":restoran}
			template = "user-interfaces/m_restoran.html"				
			return render(request, template, context)

#menambahkan nama makanan ke dalam database
def addfood(request):
	food_list = Food.objects.all()
	form = FoodForm(request.POST or None)
	if 'simpan' in request.POST:
		if form.is_valid():
			save_it =  form.save(commit=False)
			notifikasi = "Makanan baru berhasil disimpan"
			save_it.save()
			context = {"food_list":food_list, 'notifikasi':notifikasi}
			template = "user-interfaces/m_makanan.html"
			return render(request, template, context)
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

def updateFoodSave(request):
	if request.method == "POST":
		restoran_list = Restaurant.objects.all()
		food_list = Food.objects.all()
		food_list = food_list.order_by('restoran')
		restoran = Restaurant.objects.get(id=request.POST.get("restoran"))
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
			food2.update(restoran=restoran, nama_makanan=request.POST.get("nama_makanan"))
			context = {"food_list":food_list, 'notifikasi':notifikasi, "restoran_list":restoran_list}
			template = "user-interfaces/m_makanan_m.html"				
			return render(request, template, context)

def review_food(request):
	user = User.objects.get(username='melisa')
	makanan_id = request.POST.get("review")
	makanan = Food.objects.get(id=makanan_id)
	review_list = Review.objects.filter(food=makanan, dosen=user)
	if len(review_list)>0:
		review_food = Review.objects.get(food=makanan, dosen=user)
		context = {"review_food":review_food}
		template = "user-interfaces/see-review.html"				
		return render(request, template, context)
	else:
		makanan_id = request.POST.get("review")
		makanan = Food.objects.get(id=makanan_id)
		review_all = Review.objects.all()
		context = {"review_all":review_all,"makanan_id":makanan_id,"makanan":makanan}
		template = "user-interfaces/review-food.html"				
		return render(request, template, context)

def save_review(request):
	user = User.objects.get(username='melisa')
	rate = request.POST.get("rating")
	komen = request.POST.get("komentar")
	makanan = Food.objects.get(id=request.POST.get("simpan"))
	if request.method == "POST":
		if len(Review.objects.filter(food=makanan, dosen=user))>0:
			return HttpResponseRedirect('/historyorder/')
		else:
			r = Review(food=makanan, rating=rate, komentar=komen, dosen=user)
			r.save()
			orderItem_list = OrderItem.objects.all()
			user2 = User.objects.get(username='wahyu.asri')
			daftar_pesanan = []
			for g in orderItem_list:
				if g.order.dosen == user2:
					baris_pesanan  = []
					baris_pesanan.append(g.order.waktu_order)
					baris_pesanan.append(g.food)
					baris_pesanan.append(g.kuantitas)
					baris_pesanan.append(g.permintaan_lain)
					baris_pesanan.append(g.tipe_konsumen)
					daftar_pesanan.append(baris_pesanan)
			context = {"orderitem_list":daftar_pesanan, "notifikasi":notifikasi}
			template = "user-interfaces/r_pemesanan.html"
			return render(request, template, context)

def recommended_food(request):
	food_list = Food.objects.all()
	for m in food_list:
		makanan_id = m.id
		review_selected = Review.objects.filter(food=m)
		total = 0
		for x in review_selected:
			rating = x.rating
			total = total + rating
		if len(review_selected)!=0:
			avg_rating = total/(len(review_selected)+0.00)
		else:
			avg_rating = total/1
		food = Food.objects.filter(id=makanan_id)
		food.update(total_rating=avg_rating)
	sorted_food = Food.objects.all().order_by('-total_rating')
	print sorted_food
	foods = []
	for i in sorted_food:
		foods.append(i)
	recommended_food = []
	if len(foods) >=5:
		for x in xrange(0,5):
			recommended_food.append(foods[x]) #index out of range
		context = {"recommended_food":recommended_food}
		template = "user-interfaces/addorder.html"
		return render(request, template, context)
	else:
		for a in foods:
			recommended_food.append(foods[x])
		context = {"recommended_food":recommended_food}
		template = "user-interfaces/addorder.html"
		return render(request, template, context)


def historyOrder(request):
	# orderitem_list = OrderItem.objects.all()
	# context = {"orderitem_list":orderitem_list}
	# template = "user-interfaces/r_pemesanan.html"
	# return render(request, template, context)
	orderItem_list = OrderItem.objects.all()
	user2 = User.objects.get(username='wahyu.asri')
	daftar_pesanan = []
	for g in orderItem_list:
		if g.order.dosen == user2:
			baris_pesanan  = []
			baris_pesanan.append(g.order.waktu_order)
			baris_pesanan.append(g.food)
			baris_pesanan.append(g.kuantitas)
			baris_pesanan.append(g.permintaan_lain)
			baris_pesanan.append(g.tipe_konsumen)
			daftar_pesanan.append(baris_pesanan)
	context = {"orderitem_list":daftar_pesanan}
	template = "user-interfaces/r_pemesanan.html"
	return render(request, template, context)
