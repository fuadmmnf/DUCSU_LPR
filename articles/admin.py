from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Article)
admin.site.register(models.Author)
admin.site.register(models.Tag)
admin.site.register(models.Article_Author)
admin.site.register(models.Article_Tag)
admin.site.register(models.ImageUrl)