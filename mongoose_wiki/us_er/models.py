from django.db import models
from django.contrib import admin

class User(models.Model):
    username = models.CharField(max_length=256)
    def __unicode__(self):
        return self.username
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']