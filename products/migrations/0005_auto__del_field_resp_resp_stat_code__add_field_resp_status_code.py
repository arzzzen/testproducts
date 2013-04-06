# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Resp.resp_stat_code'
        db.delete_column(u'products_resp', 'resp_stat_code')

        # Adding field 'Resp.status_code'
        db.add_column(u'products_resp', 'status_code',
                      self.gf('django.db.models.fields.IntegerField')(default=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Resp.resp_stat_code'
        db.add_column(u'products_resp', 'resp_stat_code',
                      self.gf('django.db.models.fields.IntegerField')(default=200),
                      keep_default=False)

        # Deleting field 'Resp.status_code'
        db.delete_column(u'products_resp', 'status_code')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'colortwo': ('django.db.models.fields.CharField', [], {'default': "'#000'", 'max_length': '7'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'products.resp': {
            'Meta': {'object_name': 'Resp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['products']