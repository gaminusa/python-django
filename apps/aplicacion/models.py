#encoding:utf-8
from django import forms
from django.db import models
from aplicacion import constants
from aplicacion.constants import CHOICES_EDAD
from ubigeo.models import Ubigeo


class Inscrito(models.Model):
    fecha_registro = models.DateTimeField(
        auto_now=True
    )
    num_doc = models.CharField(
        u'N° de Documento',
        max_length=15
    )
    tipo_doc = models.PositiveIntegerField(
        u'Tipo de Documento',
        choices=constants.CHOICES_TIPO_DOCUMENTO,
        max_length=1
    )
    fec_nac = models.DateField(
        u'Fecha Nacimiento',
    )
    nombres = models.CharField(
        u'Nombres',
        max_length=30
    )
    apellido_paterno = models.CharField(
        u'Apellido Paterno',
        max_length=30
    )
    apellido_materno = models.CharField(
        u'Apellido Materno',
        max_length=30
    )
    sexo = models.PositiveIntegerField(
        verbose_name=u'Sexo',
        choices=constants.CHOICES_SEXO,
        max_length=1
    )
    email = models.EmailField(
        u'Email',
    )
    direccion = models.CharField(
        u'Direccion',
        max_length=120
    )
    telefono = models.CharField(
        u'Telefono',
        max_length=15
    )
    celular = models.PositiveIntegerField(
        u'Celular',
        max_length=10
    )
    ubigeo = models.ForeignKey(
        Ubigeo,
        verbose_name=u'Ubigeo',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s %s" % (self.nombres, self.apellido_paterno)


class Pata(models.Model):
    nombres = models.CharField(
        u'Nombres',
        max_length=100
    )
    mayor_edad = models.PositiveIntegerField(
        choices=CHOICES_EDAD,
        blank=False,
        null=False
    )
    ubigeo = models.ForeignKey(
        Ubigeo,
        verbose_name=u'Ubigeo',
        blank=True,
        null=True

    )
    direccion = models.CharField(
        u'Direccion',
        max_length=100
    )
    referencia = models.CharField(
        u'Referencia',
        max_length=100
    )
    cel = models.PositiveIntegerField(
        u'Celular',
    )
    dni_inscrito = models.CharField(
        u'Dni Pata',
        max_length=15
    )
    mensaje = models.CharField(
        u'Mensaje',
        max_length=150,
    )

    def __unicode__(self):
        return u"%s %s %s" % (self.nombres, self.dni_inscrito, self.mensaje)


class PromocionesInscritos(models.Model):
    dni = models.CharField(
        u'Dni',
        max_length=15
    )
    id_promocion = models.IntegerField()
    fecha_registro = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = u'promociones_inscrito'


