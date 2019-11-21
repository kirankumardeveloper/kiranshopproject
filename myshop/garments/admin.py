from django.contrib import admin
from garments.models import FormalShirt
from garments.models import CasualShirt
from garments.models import TShirt
from garments.models import Trousers

# Register your models here.
class FormalShirtAdmin(admin.ModelAdmin):
    list_display=('name','stock','price','available','created','updated')
admin.site.register(FormalShirt,FormalShirtAdmin)

class CasualShirtAdmin(admin.ModelAdmin):
    list_display=('name','stock','price','available','created','updated')
admin.site.register(CasualShirt,CasualShirtAdmin)

class TShirtAdmin(admin.ModelAdmin):
    list_display=('name','stock','price','available','created','updated')
admin.site.register(TShirt,TShirtAdmin)

class TrousersAdmin(admin.ModelAdmin):
    list_display=('name','stock','price','available','created','updated')
admin.site.register(Trousers,TrousersAdmin)
