from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=30)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de Empleado'

    def __str__(self):
        return self.habilidad

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    Job_Choices = [
        ('0', 'CEO'),
        ('1', 'Gerente'),
        ('2', 'Repartidor'),
        ('3', 'Empaquetador'),
        ('4', 'Contador'),
        ('5', 'Vendedor'),
        ('6', 'Trabajador(a) Social'),
        ('7', 'Otro'),
    ]
    first_name = models.CharField('Nombre(s)', max_length=60)
    last_name = models.CharField('Apellido(s)', max_length=60)
    phone = models.CharField('Telefono', max_length=10)
    adress = models.CharField('Direccion', max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    job = models.CharField('Trabajo', max_length=1, choices=Job_Choices)
    avatar = models.ImageField(upload_to='empleados', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField('Hoja De Vida')
        
    class Meta:
        verbose_name = 'Empleados'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['id']
        unique_together = ('first_name', 'last_name', 'job', 'departamento')
    
    def __str__(self):
        return (
            str(self.id) + ' - ' + 
            self.first_name + ' ' + 
            self.last_name + ' - ' + 
            str(self.departamento.name)
        )