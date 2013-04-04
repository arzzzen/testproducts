# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.image'
        db.add_column(u'products_product', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='images/default.jpg', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.image'
        db.delete_column(u'products_product', 'image')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['products']