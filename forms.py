from django import forms
from .models import *

class RestoranForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ('nama_restoran',)

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = ('restoran','nama_makanan',)

class FoodFormAdmin(forms.ModelForm):
	class Meta:
		model = Food
		fields = ('restoran', 'nama_makanan','total_rating',)

class Jadwal_kelasForm(forms.ModelForm):
	class Meta:
			model = JadwalKelas
			fields = ('dosen','hari','jam_mulai','jam_selesai','ruangan')


class UserForm(forms.ModelForm):
	class Meta:
			model = User
			fields = ('username','role','nama_user')

class OrderItemForm(forms.ModelForm):
	class Meta:			
			model = OrderItem			
			fields = ('food','kuantitas','tipe_konsumen', 'permintaan_lain')

class OForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('dosen',)

