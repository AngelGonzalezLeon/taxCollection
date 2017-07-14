# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Year2013
from .models import Year2014
from .models import Year2015
from .models import Year2016

admin.site.register(Year2013)
admin.site.register(Year2014)
admin.site.register(Year2015)
admin.site.register(Year2016)
