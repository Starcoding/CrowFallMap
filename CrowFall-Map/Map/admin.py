from django.contrib import admin
from .models import Map, Dot, Category

# Register your models here.


class DotInline(admin.TabularInline):
    model = Dot
    extra = 0


class MapAdmin(admin.ModelAdmin):
    inlines = [
        DotInline,
    ]


admin.site.register(Category)
admin.site.register(Dot)
admin.site.register(Map, MapAdmin)
