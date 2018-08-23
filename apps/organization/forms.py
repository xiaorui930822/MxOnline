# -*- coding: utf-8 -*-
__author__ = 'xurui'
__date__ = '2018/4/25 0025 15:51'

import re
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):  # 直接继承model中的格式
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            #抛出号码异常
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")
