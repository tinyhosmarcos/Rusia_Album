from django.db import models
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.utils import timezone
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Pagina(models.Model):
	id=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	PAIS='Pais'
	MISCALENEO='MS'
	list_tipo=((PAIS,'Pais'),(MISCALENEO,'Miscaleneo'))
	tipo=models.CharField(max_length=30,choices=list_tipo,default=PAIS)
	def __str__(self):
		return self.nombre


class UserProfile(models.Model):
	user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
	num_sobres=models.IntegerField(default=3)
	time_sobres=models.DateTimeField(default=timezone.now)
	def set_time(num):
		time_sobres.time.second=num


class Record(models.Model):
	title = models.CharField(max_length=15)
	text = models.CharField(max_length=)
	date = models.DateField(default=timezone.now)
	img_id = models.CharField(max_length=20)
	

class List_Cromo(models.Model):
	user_id=models.OneToOneField(User,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.user_id)

class Cromo(models.Model):
	id=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	JUGADOR='Jugador'
	MISCALENEO='Miscaleneo'
	list_tipo=((JUGADOR,'Jugador'),(MISCALENEO,'Miscaleneo'))
	tipo=models.CharField(max_length=30,choices=list_tipo,default=JUGADOR)
	page_id=models.ForeignKey(Pagina,on_delete=models.CASCADE)
	pub_date=models.DateTimeField('date published')
	
	def __str__(self):
		return self.nombre
class Cromo_Rep(models.Model):
	list_cromo_id=models.ForeignKey(List_Cromo,on_delete=models.CASCADE)
	cromo=models.ForeignKey(Cromo,on_delete=models.CASCADE)
	no_repeat=models.IntegerField(primary_key=True)
	cantidad=models.IntegerField(default=0)
	def __str__(self):
		return str(self.cromo)



class Estadistica(models.Model):
	cromo_id = models.OneToOneField(Cromo, on_delete=models.CASCADE,primary_key=True, unique=True)
	posicion = models.CharField(max_length=20)
	fecha_nacimiento=models.DateTimeField()
	club = models.CharField(max_length=40)
	altura = models.CharField(max_length=10)
	peso= models.CharField(max_length=10)
	debut = models.IntegerField()
	def __str__(self):
		return str(self.cromo_id)



def create_user_profile(sender,instance,created,**kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_user_profile,sender=User)

@receiver(pre_save,sender=Cromo_Rep)
def my_callback(sender, instance, *args, **kwargs):
    instance.no_repeat = slugify(instance.list_cromo_id)




"""class Page(models.Model):
	id=models.AutoField(primary_key=True)
	nombre_des=models.CharField(max_length=20)
	#choices
	PAIS='PA'
	MISCALENEO='MS'
	list_diseño=((PAIS,'Pais'),(MISCALENEO,'Miscaleneo'))
	diseño=models.CharField(max_length=2,choices=list_diseño,default=PAIS)
	def __str__(self):
		return self.nombre_des
		
class Country(models.Model):
	page_id=models.OneToOneField(Page, on_delete=models.CASCADE,primary_key=True)
	nombre=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class Miscaleneo(models.Model):
	page_id=models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True)
	description_text=models.CharField(max_length=300)
	description_misc=models.CharField(max_length=40)
	def __str__(self):
		return self.description_misc

class Cromo(models.Model):
	id = models.AutoField(primary_key=True)
	cromo_img=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	#new add models
	page_id=models.ForeignKey(Page, on_delete=models.CASCADE)
	#choices
	JUGADOR='jr'
	ESTADIO='es'
	list_tipo=((JUGADOR,'Jugador'),(ESTADIO,'Estadio'))
	tipo=models.CharField(max_length=2,choices=list_tipo,default=JUGADOR)
	def __str__(self):
		return self.tipo

class Jugador(models.Model):
	cromo_id	=models.OneToOneField(Cromo, on_delete=models.CASCADE,primary_key=True)
	seleccion	=models.ForeignKey(Country,on_delete=models.CASCADE,default=1)
	nombres		=models.CharField(max_length=30)
	apellidos	=models.CharField(max_length=30)
	posicion	=models.CharField(max_length=20)
	peso		=models.CharField(max_length=20)
	altura		=models.CharField(max_length=20)
	club_actual	=models.CharField(max_length=40)
	f_nacimiento=models.DateField(auto_now=False, auto_now_add=False)
	def __str__(self):
		return self.nombres

class Estadio(models.Model):
	cromo_id=models.OneToOneField(Cromo,on_delete=models.CASCADE,primary_key=True)
	nombre=models.CharField(max_length=40)
	f_creacion=models.DateField(auto_now=False,auto_now_add=False)
	def __str__(self):
		return self.nombre"""