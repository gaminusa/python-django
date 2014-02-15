#encoding:utf-8
from django.db import models
from aplicacion import constants


class Inscrito(models.Model):
    fecha_registro = models.DateTimeField(
        auto_now=True
    )
    num_doc = models.CharField(
        u'Numero de Documento',
        max_length=15
    )
    tipo_doc = models.PositiveIntegerField(
        choices=constants.CHOICES_TIPO_DOCUMENTO,
        max_length=1
    )
    fec_nac = models.DateField()
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
    ubigeo = models.CharField(
        max_length=6
    )

    def __unicode__(self):
        return u"%s %s" % (self.nombres, self.apellido_paterno)
