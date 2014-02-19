# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inscrito'
        db.create_table(u'aplicacion_inscrito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_registro', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('num_doc', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tipo_doc', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('fec_nac', self.gf('django.db.models.fields.DateField')()),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sexo', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('celular', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=10)),
            ('ubigeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubigeo.Ubigeo'], null=True, blank=True)),
        ))
        db.send_create_signal(u'aplicacion', ['Inscrito'])

        # Adding model 'Pata'
        db.create_table(u'aplicacion_pata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mayor_edad', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ubigeo', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cel', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dni_inscrito', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mensaje', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'aplicacion', ['Pata'])

        # Adding model 'PromocionesInscritos'
        db.create_table(u'promociones_inscrito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('id_promocion', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_registro', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'aplicacion', ['PromocionesInscritos'])


    def backwards(self, orm):
        # Deleting model 'Inscrito'
        db.delete_table(u'aplicacion_inscrito')

        # Deleting model 'Pata'
        db.delete_table(u'aplicacion_pata')

        # Deleting model 'PromocionesInscritos'
        db.delete_table(u'promociones_inscrito')


    models = {
        u'aplicacion.inscrito': {
            'Meta': {'object_name': 'Inscrito'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fec_nac': ('django.db.models.fields.DateField', [], {}),
            'fecha_registro': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_doc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sexo': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipo_doc': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            'ubigeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubigeo.Ubigeo']", 'null': 'True', 'blank': 'True'})
        },
        u'aplicacion.pata': {
            'Meta': {'object_name': 'Pata'},
            'cel': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dni_inscrito': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mayor_edad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'mensaje': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ubigeo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'aplicacion.promocionesinscritos': {
            'Meta': {'object_name': 'PromocionesInscritos', 'db_table': "u'promociones_inscrito'"},
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fecha_registro': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_promocion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ubigeo.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubigeo.Ubigeo']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['aplicacion']