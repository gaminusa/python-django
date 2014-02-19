# -*- coding: utf-8 -*-
"""
models for ubigeo utils
"""

from django.db import models


class UbigeoManager(models.Manager):
    def departments(self):
        return self.filter(parent__isnull=True)


class Ubigeo(models.Model):
    name = models.CharField('nombre', max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True)

    objects = UbigeoManager()
    
    class Meta:
        verbose_name = 'Ubigeo'
        verbose_name_plural = 'Ubigeos'

    def __unicode__(self):
        return u'%s' % self.name

    def is_department(self):
        return bool(not self.parent)

    def is_province(self):
        return bool(self.parent and not self.parent.parent)

    def is_district(self):
        return bool(self.parent and self.parent.parent)

    def department(self):
        return self.name if not self.parent else self.district()

    def province(self):
        parent = self.parent
        return None if not parent else parent.name if not parent.parent else parent.parent.name

    def district(self):
        parent = self.parent
        return None if not (parent or parent.parent) else parent.parent.name
