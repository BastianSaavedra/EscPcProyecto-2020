from django.db import models
from django.urls import reverse
import uuid


class PlacasMadre(models.Model):
    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=100,help_text='Modelo del producto')

    CATALOGO_FORMATO_PLACAMADRE = (
        ('seleccione','Seleccione'),
        ('ATX','ATX'),
        ('Mini ITX','Mini ITX'),
        ('Micro ATX','Micro ATX'),
    )

    formato = models.CharField(max_length=10,choices=CATALOGO_FORMATO_PLACAMADRE,blank=False,default='s',help_text='Formato de la Placa Madre')

    CATALOGO_PLATAFORMA_PLACAMADRE = (
        ('seleccione','Seleccione'),
        ('AMD','AMD'),
        ('Intel','Intel')
    )

    plataforma = models.CharField(max_length=10,choices=CATALOGO_PLATAFORMA_PLACAMADRE,blank=False,default='se',help_text='Plataforma de la Placa Madre')
    stock = models.IntegerField(default=0,help_text='Stock del producto')
    imagen = models.ImageField(upload_to='placasmadres/',null=True)
    imagen_detail = models.ImageField(upload_to='placasmadres_detail/',null=True)
    precio = models.IntegerField(default=0,help_text='Precio del producto')

    def __str__(self):
        return f'{self.marca},{self.modelo}'


class Procesadore(models.Model):
    CATALOGO_MARCA_PROCESADOR = (
        ('seleccione','Seleccione'),
        ('AMD','AMD'),
        ('Intel','Intel')
    )
    marca = models.CharField(max_length=10,choices=CATALOGO_MARCA_PROCESADOR,blank=False,default='s',help_text='Marca del producto')
    modelo = models.CharField(max_length=100,help_text='Modelo del producto')
    frecuencia = models.CharField(max_length=50,help_text='Frecuencia del producto')
    CATALOGO_SOCKET_PROCESADOR = (
        ('seleccione','Seleccione'),
        ('LGA 1151-v2','LGA 1151-v2'),
        ('AM4','AM4'),
        ('TR4','TR4')
    )
    socket = models.CharField(max_length=11,choices=CATALOGO_SOCKET_PROCESADOR,blank=False,default='s',help_text='Socket del producto')
    stock = models.IntegerField(default=0,help_text='Stock del producto')
    imagen = models.ImageField(upload_to='procesador/',null=True)
    imagen_detail = models.ImageField(upload_to='procesador_detail/',null=True)
    precio = models.IntegerField(default=0,help_text='Precio del producto')
    def __str__(self):
        return  f'{self.marca},{self.modelo}'

class Gpu(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')
    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=100)

    CATALOGO_PLATAFORMA_GPU = (
        ('seleccione','Seleccione'),
        ('AMD','AMD'),
        ('Nvidia','Nvidia'),
    )

    plataforma = models.CharField(max_length=10, choices=CATALOGO_PLATAFORMA_GPU,blank=False,default='s',help_text='Plataforma del producto')
    memoria = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='gpu/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return  self.modelo

class Ram(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')
    marca = models.CharField(max_length=100,help_text='Marca del producto')
    capacidad = models.CharField(max_length=100)

    CATALOGO_TIPO_RAM = (
        ('seleccione','Seleccione'),
        ('DDR3','DDR3'),
        ('DDR4','DDR4'),
    )

    tipo = models.CharField(max_length=10,choices=CATALOGO_TIPO_RAM,blank=False,default='se',help_text='Tipo de ram')
    frecuencia = models.CharField(max_length=50)

    CATALOGO_FORMATO_RAM = (
        ('seleccione','Seleccione'),
        ('DIMM','DIMM'),
        ('SO-DIMM','SO-DIMM')
    )

    formato = models.CharField(max_length=10,choices=CATALOGO_FORMATO_RAM,blank=False,default='s',help_text='Formato de la Ram')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='ram/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.marca

class Almacenamiento(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unido del producto')
    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)

    CATALOGO_FORMATO_ALMACENAMIENTO = (
        ('seleccione','Seleccione'),
        ('HDD','HDD'),
        ('M.2','M.2'),
        ('2.5"','2.5"'),
    )

    formato = models.CharField(max_length=10,choices=CATALOGO_FORMATO_ALMACENAMIENTO,blank=False,default='s',help_text='Formato del producto')
    bus = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='almacenamiento/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return  self.modelo

class FuentesPoder(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    marca = models.CharField(max_length=100,help_text='Marca del producto')
    potencia = models.CharField(max_length=50)

    CATALOGO_CERTIFICACION_FUENTE = (
        ('seleleccione','Seleccione'),
        ('80PLUS Gold','80PLUS Gold'),
        ('80PLUS Bronze','80PLUS Bronze'),
        ('Sin Certificacion','Sin Certificacion')
    )

    certificacion = models.CharField(max_length=20,choices=CATALOGO_CERTIFICACION_FUENTE,blank=False,default='sele',help_text='Certificacion del producto')

    CATALOGO_MODULAR_FUENTE = (
        ('se','Seleccione'),
        ('SI','SI'),
        ('NO','NO')
    )

    modular = models.CharField(max_length=2,choices=CATALOGO_MODULAR_FUENTE,blank=False,default='se')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='fuentedepoder/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.marca


class Gabinete(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=50)

    CATALOGO_FUENTE_GABINETE = (
        ('seleccione','Seleccione'),
        ('No posee','No posee'),
        ('Si posee','Si posee')
    )

    fuente_gabinete = models.CharField(max_length=10,choices=CATALOGO_FUENTE_GABINETE,blank=False,default='se',help_text='Posee o no posee fuente de poder dentro del gabinete')

    CATALOGO_PANEL_GABIENTE = (
        ('seleccione','Seleccione'),
        ('Vidrio Templado','Vidrio Templado'),
        ('Panel Acrilico','Panel Acrilico')
    )
    panel = models.CharField(max_length=20,choices=CATALOGO_PANEL_GABIENTE,blank=False,default='s',help_text='Tipo de panel del gabinete')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='gabinete/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.modelo

class Monitore(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=50)

    CATALOGO_PULGADAS_MONITOR = (
        ('seleccione','Seleccione'),
        ('23.0"','23.0"'),
        ('24.0"','24.0"'),
        ('25.0"','25.0"'),
        ('26.0"','26.0"'),
        ('27.0"','27.0"')
    )

    pulgadas = models.CharField(max_length=10,choices=CATALOGO_PULGADAS_MONITOR,blank=False,default='sele',help_text='Pulgadas del monitor')
    resolucion = models.CharField(max_length=50)

    CATALOGO_TIEMPO_MONITOR = (
        ('seleccione','Seleccione'),
        ('1 ms','1 ms'),
        ('2 ms','2 ms'),
        ('3 ms','3 ms'),
        ('4 ms','4 ms'),
    )

    tiempo_respuesta = models.CharField(max_length=10,choices=CATALOGO_TIEMPO_MONITOR,blank=False,default='s',help_text='Tiempo de respuesta del monitor')

    CATALOGO_TASA_MONITOR = (
        ('seleccione','Seleccione'),
        ('120 Hz','120 Hz'),
        ('144 Hz','144 Hz'),
        ('165 Hz','165 Hz')
    )

    tasa_refresco = models.CharField(max_length=10,choices=CATALOGO_TASA_MONITOR,blank=False,default='sel',help_text='Tasa de refresco del monitor')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='monitor/',null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.modelo

opciones_consultas = [
    [0,"consulta"],
    [1,"sugerencia"],
    [2,"reclamo"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.email
