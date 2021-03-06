# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResumeWhitoutStaffDailyReportData'
        db.create_table(u'dash_resumewhitoutstaffdailyreportdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resume_commends_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resume_view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resume_view_proportion', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('resume_fav_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resume_down_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resume_down_proportion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('company_card_send_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('interviewed_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('entered_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('dash', ['ResumeWhitoutStaffDailyReportData'])


    def backwards(self, orm):
        # Deleting model 'ResumeWhitoutStaffDailyReportData'
        db.delete_table(u'dash_resumewhitoutstaffdailyreportdata')


    models = {
        'dash.coredailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'CoreDailyReportData'},
            'active_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lively_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'repeat_visit_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dash.feeddailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'FeedDailyReportData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lively_feed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lively_feed_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lively_feed_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_feed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dash.monthreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'MonthReportData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month_lively_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'month_lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'month_repeat_visit_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'month_repeat_visit_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dash.partnerdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'PartnerDailyReportData'},
            'accept_task_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accept_task_user_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accusation_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accusation_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'all_extra_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'all_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'do_task_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'do_task_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'interviewed_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resume_download_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_download_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_viewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_viewed_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_accedpted_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_accedpted_count_contrast': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'task_accedpted_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_viewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_commend_and_check_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_commend_and_download_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_extra_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_resume_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_resume_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dash.pinbotdailyreport': {
            'Meta': {'object_name': 'PinbotDailyReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pay_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {}),
            'total_pay_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uv': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dash.resumedailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'ResumeDailyReportData'},
            'company_card_send_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resume_commends_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_down_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_down_proportion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'resume_fav_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_view_proportion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'})
        },
        'dash.resumewhitoutstaffdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'ResumeWhitoutStaffDailyReportData'},
            'company_card_send_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resume_commends_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_down_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_down_proportion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'resume_fav_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_view_proportion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'})
        },
        'dash.tasksystemdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'TaskSystemDailyReportData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'task_A10_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A10_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A11_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A12_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A13_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A14_L1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A15_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A15_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A15_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A16_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A17_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A18_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A18_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A3_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A4_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A5_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A6_L1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A6_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A6_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A6_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A7_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A7_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A7_R3_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A7_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A8_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A8_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A8_R3_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A8_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A9_R1_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A9_R2_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A9_R3_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_A9_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dash.userdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'UserDailyReportData'},
            'all_total_active_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_experience_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_manual_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_self_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'total_experience_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_manual_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_self_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dash.weekreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'WeekReportData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'week_lively_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_repeat_visit_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_repeat_visit_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dash.weixindailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'WeixinDailyReportData'},
            'feed_notify_send_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'feed_notify_view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lively_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_bind_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_feed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_feed_favours_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_reg_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'total_bind_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['dash']