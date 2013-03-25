# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'bar_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bar', ['Region'])

        # Adding model 'Spirittype'
        db.create_table(u'bar_spirittype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bar', ['Spirittype'])

        # Adding model 'Distillery'
        db.create_table(u'bar_distillery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bar.Region'], null=True, on_delete=models.SET_NULL)),
            ('founded', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bar', ['Distillery'])

        # Adding model 'Spirit'
        db.create_table(u'bar_spirit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('distillery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bar.Distillery'], null=True, on_delete=models.SET_NULL)),
            ('spirittype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bar.Spirittype'], null=True, on_delete=models.SET_NULL)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bar', ['Spirit'])

        # Adding model 'Image'
        db.create_table(u'bar_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('hero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('spirit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bar.Spirit'], null=True, on_delete=models.SET_NULL)),
            ('ordering', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bar', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'bar_region')

        # Deleting model 'Spirittype'
        db.delete_table(u'bar_spirittype')

        # Deleting model 'Distillery'
        db.delete_table(u'bar_distillery')

        # Deleting model 'Spirit'
        db.delete_table(u'bar_spirit')

        # Deleting model 'Image'
        db.delete_table(u'bar_image')


    models = {
        u'bar.distillery': {
            'Meta': {'object_name': 'Distillery'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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