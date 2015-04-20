from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
#from sipema import polls
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sipema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'polls.views_index.index'), #
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login', 'polls.views_index.login'),
	url(r'^logout', 'polls.views_index.logout'),
	## solve regex untuk log out
	#url(r'^([A-Za-z0-9_\\.\\/]+)/logout', 'polls.views_index.logout'),
	
	#---------------------fadli--------------------------
	
	url(r'^view/daftar_dosen/$', 'polls.views_fadli.daftar_dosen'),
	url(r'^view/jadwal/$', 'polls.views_fadli.view_jadwal'),
	url(r'^add/jadwal/$', 'polls.views_fadli.add_jadwal'),
		url(r'^add/jadwal2/$', 'polls.views_fadli.add_jadwal2'),
	url(r'^edit/jadwal/$', 'polls.views_fadli.edit_jadwal'),
	url(r'^edit/jadwal2/$', 'polls.views_fadli.edit_jadwal2'),
	url(r'^edit/jadwal3/$', 'polls.views_fadli.edit_jadwal3'),
	url(r'^edit/jadwal4/$', 'polls.views_fadli.edit_jadwal4'),
	url(r'^delete/jadwal/$', 'polls.views_fadli.delete_jadwal'),
	
	url(r'^view/biaya/$', 'polls.views_fadli.view_biaya'),
	url(r'^add/biaya/$', 'polls.views_fadli.add_biaya'),
	url(r'^add/biaya2/$', 'polls.views_fadli.add_biaya2'),
	
	#----------------------LOGIN-------------------------
	url(r'^view/biaya/login/', 'polls.views_index.login'),
	url(r'^add/biaya/login/', 'polls.views_index.login'),
	url(r'^add/biaya2/login/', 'polls.views_index.login'),
	

	url(r'^add/jadwal/login/', 'polls.views_index.login'),
	url(r'^add/jadwal2/login/', 'polls.views_index.login'),
	url(r'^view/jadwal/login/', 'polls.views_index.login'),
	url(r'^view/daftar_dosen/login/', 'polls.views_index.login'),
	url(r'^edit/jadwal/login/', 'polls.views_index.login'),
	url(r'^edit/jadwal2/login/', 'polls.views_index.login'),
	url(r'^edit/jadwal3/login/', 'polls.views_index.login'),
	url(r'^edit/jadwal4/login/', 'polls.views_index.login'),
	url(r'^delete/jadwal/login/', 'polls.views_index.login'),
	#----------------LOGOUT--------------------------
	url(r'^view/biaya/logout/', 'polls.views_index.logout'),
	url(r'^add/biaya/logout/', 'polls.views_index.logout'),
	url(r'^add/biaya2/logout/', 'polls.views_index.logout'),
	url(r'^edit/jadwal3/logout/', 'polls.views_index.logout'),
	url(r'^edit/jadwal4/logout/', 'polls.views_index.logout'),
	url(r'^edit/jadwal2/logout/', 'polls.views_index.logout'),
	url(r'^edit/jadwal/logout/', 'polls.views_index.logout'),
	url(r'^add/jadwal/logout/', 'polls.views_index.logout'),
	url(r'^add/jadwal2/logout/', 'polls.views_index.logout'),
	url(r'^view/jadwal/logout/', 'polls.views_index.logout'),
	url(r'^view/daftar_dosen/logout/', 'polls.views_index.logout'),
	url(r'^delete/jadwal/logout/', 'polls.views_index.logout'),


	
	#----------------------------------------------------


	#---------------------ariel-----------------------
	url(r'^add/order/$', 'polls.views.addOrder'),
	url(r'^view/order/$', 'polls.views.viewOrder'),
	url(r'^manage/order/$', 'polls.views.editOrder'),
	url(r'^view/order/delete/$', 'polls.views.deleteOrder1'),
	url(r'^historyorder/$', 'polls.views.historyOrder'),
	url(r'^view/order/today/$', 'polls.views_ariel.daftarpesanan'),
	url(r'^sekretariat/add/order/$', 'polls.views.sekretariataddorder'),
	
	url(r'^va_dosen/$', 'polls.views.va_dosen'),

	#LOG OUT
	url(r'^add/order/logout/', 'polls.views_index.logout'),
	url(r'^view/order/logout/', 'polls.views_index.logout'),
	url(r'^edit/order/logout/', 'polls.views_index.logout'),
	url(r'^historyorder/logout/', 'polls.views_index.logout'),
	url(r'^sekretariat/add/order/logout/', 'polls.views_index.logout'),
	url(r'^manage/order/logout/', 'polls.views_index.logout'),
	url(r'^view/order/today/logout/', 'polls.views_index.logout'),

	#LOG IN
	url(r'^add/order/login/', 'polls.views_index.login'),
	url(r'^view/order/login/', 'polls.views_index.login'),
	url(r'^edit/order/login/', 'polls.views_index.login'),
	url(r'^historyorder/login/', 'polls.views_index.login'),
	url(r'^manage/order/login/', 'polls.views_index.login'),
	url(r'^view/order/today/login/', 'polls.views_index.login'),
	url(r'^sekretariat/add/order/login/', 'polls.views_index.login'),

	#---------------------hamka------------------------
	url(r'^edit/user/$', 'polls.views.editUser'),
	url(r'^view/user/$', 'polls.views.lihatUser'), 
	url(r'^add/user/$', 'polls.views.addUser'),
	url(r'^view/user/delete/$', 'polls.views.deleteUser'), #
	url(r'^view/user/update/$', 'polls.views.updateUser'),#
	url(r'^view/user/updatesave/$', 'polls.views.updateUserSave'),#
	
	#LOG IN
	url(r'^add/user/login/', 'polls.views_index.login'),
	url(r'^view/user/login/', 'polls.views_index.login'),
	url(r'^edit/user/login/', 'polls.views_index.login'),
	url(r'^view/user/delete/login/', 'polls.views_index.login'),
	url(r'^view/user/update/login/', 'polls.views_index.login'),
	url(r'^view/user/updatesave/login/', 'polls.views_index.login'),
	
	#LOG OUT
	url(r'^add/user/logout/', 'polls.views_index.logout'),
	url(r'^view/user/logout/', 'polls.views_index.logout'),
	url(r'^edit/user/logout/', 'polls.views_index.logout'),
	url(r'^view/user/delete/logout/', 'polls.views_index.logout'),
	url(r'^view/user/update/logout/', 'polls.views_index.logout'),
	url(r'^view/user/updatesave/logout/', 'polls.views_index.logout'),


	#===========KEI(start)======================================
	url(r'^add/food/$', 'polls.views.addfood'),
	url(r'^add/restoran/$', 'polls.views.addrestoran'),
	url(r'^view/food/$', 'polls.views.viewfood'),
	url(r'^manage/food/$', 'polls.views.managefood'),
	url(r'^view/food/delete/$', 'polls.views.deleteFood'),
	url(r'^view/food/update/$', 'polls.views.updateFood'),
	url(r'^view/food/updatesave/$', 'polls.views.updateFoodSave'),
	#
	#LOG IN
	url(r'^add/food/login/', 'polls.views_index.login'),
	url(r'^add/restoran/login/', 'polls.views_index.login'),
	url(r'^view/food/login/', 'polls.views_index.login'),
	url(r'^manage/food/login/', 'polls.views_index.login'),
	url(r'^view/food/delete/login/', 'polls.views_index.login'),
	url(r'^view/food/update/login/', 'polls.views_index.login'),
	url(r'^view/food/updatesave/login/', 'polls.views_index.login'),
	
	#LOG OUT
	url(r'^add/food/logout/', 'polls.views_index.logout'),
	url(r'^add/restoran/logout/', 'polls.views_index.logout'),
	url(r'^view/food/logout/', 'polls.views_index.logout'),
	url(r'^manage/food/logout/', 'polls.views_index.logout'),
	url(r'^view/food/update/logout/', 'polls.views_index.logout'),
	url(r'^view/food/updatesave/logout/', 'polls.views_index.logout'),
	#===========KEI(end)======================================


	#url(r'^index/$', 'polls.views.index'),
	


) #+static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
