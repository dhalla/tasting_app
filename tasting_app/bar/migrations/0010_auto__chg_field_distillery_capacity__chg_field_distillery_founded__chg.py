# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Distillery.capacity'
        db.alter_column(u'bar_distillery', 'capacity', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Distillery.founded'
        db.alter_column(u'bar_distillery', 'founded', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0))

        # Changing field 'Distillery.location'
        db.alter_column(u'bar_distillery', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

    def backwards(self, orm):

        # Changing field 'Distillery.capacity'
        db.alter_column(u'bar_distillery', 'capacity', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Distillery.founded'
        db.alter_column(u'bar_distillery', 'founded', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

        # Changing field 'Distillery.location'
        db.alter_column(u'bar_distillery', 'location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'bar.distillery': {
            'Meta': {'object_name': 'Distillery'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bar.Region']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'bar.image': {
            'Meta': {'object_name': 'Image'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'spirit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bar.Spirit']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        u'bar.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'bar.spirit': {
            'Meta': {'ordering': "['name', 'age']", 'object_name': 'Spirit'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'distillery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bar.Distillery']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'spirittype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bar.Spirittype']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'bar.spirittype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Spirittype'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bar']