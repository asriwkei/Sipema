from django.db import models
import datetime
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20, primary_key=True)
	ROLE_TYPE = (('Sekretariat', 'Sekretariat'),('Dosen', 'Dosen'),('Admin','Admin'),)
	role = models.CharField(max_length=20, choices=ROLE_TYPE, default='Dosen')
	nama_user = models.CharField(max_length=45)
	def __str__(self):
		return self.nama_user
		
class JadwalKelas(models.Model):
	dosen = models.ForeignKey(User, limit_choices_to={'role':"Dosen"})
	LIST_HARI = (
	('Senin','Senin'), ('Selasa','Selasa'), ('Rabu','Rabu'),
	('Kamis','Kamis'), ('Jum\'at','Jum\'at'), ('Sabtu','Sabtu'),
	('Minggu','Minggu'),)
	hari = models.CharField(max_length=20, choices=LIST_HARI, default='Senin')
	jam_mulai = models.TimeField(max_length=15)
	jam_selesai = models.TimeField(max_length=45) 
	ruangan = models.CharField(max_length=5)
	class Meta:
		unique_together = (('dosen','hari','jam_mulai','jam_selesai'),)
	def __str__(self):
		return " %s \ %s \ %s \ %s \ %s" %(self.dosen.nama_user, self.hari, self.jam_mulai, self.jam_selesai, self.ruangan)

class Order(models.Model):
	waktu_order = models.DateField(auto_now_add=True, auto_now=False) 
	#tanggal = datetime.datetime.now().date
	dosen = models.ForeignKey(User, limit_choices_to={'role':"Dosen"}, related_name='dosen')
	sekretariat = models.ForeignKey(User, limit_choices_to={'role':"Sekretariat"}, blank=True, null=True, related_name='sekretariat')
	class Meta:
		unique_together = (('dosen','waktu_order'),)
	def __str__(self):
		return " %s \ %s " %(self.waktu_order, self.dosen.nama_user)

class Restaurant(models.Model):
	nama_restoran = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return " %s " %(self.nama_restoran)
		
class Food(models.Model):
	restoran = models.ForeignKey(Restaurant)
	nama_makanan = models.CharField(max_length=30)
	total_rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
	class Meta:
		unique_together = (('restoran','nama_makanan'),)
	def __str__(self):
		return " %s  \ %s" %(self.nama_makanan, self.restoran.nama_restoran)	

class OrderItem(models.Model):
	order = models.ForeignKey(Order)
	food = models.ForeignKey(Food, blank=True, null=True)#yang sekretariat bisa karena ada related name sekretariat, yang ini ga ada nama_makanan
	LIST_KUANTITAS = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),)
	kuantitas = models.PositiveIntegerField(choices=LIST_KUANTITAS, default=1)
	LIST_TIPE = (
	('Dosen','Dosen'), ('Asisten','Asisten'),)
	tipe_konsumen = models.CharField(max_length=20, choices=LIST_TIPE, default="Dosen")
	permintaan_lain = models.CharField(max_length=200, null=True, blank=True)
	class Meta:
		unique_together = (('order','food','tipe_konsumen'),)
	def __str__(self):
		return " %s \ %s \ %s \ %s \ %s " %(self.order.waktu_order, self.order.dosen.nama_user, self.food, self.kuantitas, self.permintaan_lain)	
	
class Review(models.Model):
	food = models.ForeignKey(Food)
	LIST_RATING = (
	(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),)
	rating = models.PositiveIntegerField(choices=LIST_RATING, default=0) 
	komentar = models.TextField(null=True, blank=True)
	dosen = models.ForeignKey(User, limit_choices_to={'role':"Dosen"})
	class Meta:
		unique_together = (('food','dosen'),)
	def __str__(self):
		return " %s \ %s \%s \ %s" %(self.food.nama_makanan, self.dosen.nama_user, self.rating, self.komentar)
	

class Pembayaran(models.Model):
	waktu_bayar = models.DateField(primary_key=True)
	total_pembayaran = models.PositiveIntegerField(default=0)
	sekretariat = models.ForeignKey(User, limit_choices_to={'role':"Sekretariat"})
			
	def __str__(self):
		return " %s \ %s \%s \%s" %(self.waktu_bayar, self.total_pembayaran, self.sekretariat)
