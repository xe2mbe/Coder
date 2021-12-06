from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, GenericIPAddressField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Maestro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
class Familiar(models.Model):
    genero_eleccion = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero = models.CharField(choices=genero_eleccion, default="Selecciona", max_length=100)
    nombre = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default="Ninguna")
    apellido = models.CharField(max_length=40)
    birthday = models.DateField()
    mobile = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField()

class Device(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    brand = models.DateField()
    model = PhoneNumberField(unique = True, null = False, blank = False)
    ip = GenericIPAddressField
