# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ResumeMarkSetting.good_result'
        db.add_column(u'system_resumemarksetting', 'good_result',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ResumeMarkSetting.classify'
        db.add_column(u'system_resumemarksetting', 'classify',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ResumeMarkSetting.good_result'
        db.delete_column(u'system_resumemarksetting', 'good_result')

        # Deleting field 'ResumeMarkSetting.classify'
        db.delete_column(u'system_resumemarksetting', 'classify')


    models = {
        u'system.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'system.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'system.companycategoryprefer': {
            'Meta': {'object_name': 'CompanyCategoryPrefer'},
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'system.companywelfare': {
            'Meta': {'object_name': 'CompanyWelfare'},
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'system.positioncategory': {
            'Meta': {'object_name': 'PositionCategory'},
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'system.positioncategorytag': {
            'Meta': {'object_name': 'PositionCategoryTag'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'category_tags'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['system.PositionCategory']"}),
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_tags'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['system.PositionCategoryTag']"})
        },
        u'system.resumemarksetting': {
            'Meta': {'object_name': 'ResumeMarkSetting'},
            'change': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'classify': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'good_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mark_choices'", 'null': 'True', 'to': u"orm['system.ResumeMarkSetting']"})
        }
    }

    complete_apps = ['system']