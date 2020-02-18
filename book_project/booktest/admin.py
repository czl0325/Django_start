from django.contrib import admin
from booktest.models import HeroInfo, BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook_id']


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
