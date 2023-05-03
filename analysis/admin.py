from django.contrib import admin
from analysis.models import Twittertext
# Register your models here.
@admin.register(Twittertext)
class TestAdmin(admin.ModelAdmin):
    pass