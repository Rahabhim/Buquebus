from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sector(models.Model):
        nombre=models.CharField(max_length=50)
        creado=models.DateTimeField(auto_now_add=True)
        actualizado=models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name="sector"
            verbose_name_plural="sectores"

        def __str__(self):
            return self.nombre

class Cuit(models.Model):
    nombre=models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Cuit"
        verbose_name_plural="cuits"


    def __str__(self):
        return self.nombre



class Orden(models.Model):
        empresa=models.CharField(max_length=50, null=True)
        contacto=models.CharField(max_length=50, null=True, blank=True)
        creado=models.DateField(auto_now_add=True)

        # imagen=models.ImageField(upload_to='blog', null=True, blank=True)
        autor=models.ForeignKey(User, on_delete=models.CASCADE)
        cuit=models.ManyToManyField(Cuit)
        sectores=models.ManyToManyField(Sector)
        presupuesto=models.CharField(max_length=50, null=True, blank=True)
        descripcion=models.TextField(max_length=5000, null=True)
        total=models.CharField(max_length=50, null=True)
        actualizado=models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name="orden"
            verbose_name_plural="ordenes"

        def __str__(self):
            return self.empresa
