# -*- coding: utf-8 -*-
__author__ = 'xurui'
__date__ = '2018/4/12 0012 20:39'
import xadmin

from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']  # 按照点击数排序
    readonly_fields = ['click_nums', 'fav_nums', 'image']  # 设置只读字段
    # exclude = ['learn_times']  # 设置隐藏
    list_editable = ['degree', 'desc', 'detail'] # 列表页直接编辑
    #detail就是要显示为富文本的字段名
    # style_fields = {"detail": "ueditor"}


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
