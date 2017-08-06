# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Slider
from .models import About
from .models import Management_Philosophy
from .models import Partner
from .models import Contact
from .models import Company

# Register your models here.
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Management_Philosophy)
admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(Company)
