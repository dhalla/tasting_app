# -*- coding: utf-8 -*-
#
from django.contrib import admin
from bar.models import Spirit, Region, Spirittype, Distillery


class SpiritAdmin(admin.ModelAdmin):
    radio_fields = {"spirittype": admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Distillery)
admin.site.register(Spirit, SpiritAdmin)
admin.site.register(Region)
admin.site.register(Spirittype)
