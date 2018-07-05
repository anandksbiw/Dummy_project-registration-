from django.contrib import admin
from . import models

admin.site.register(models.UserProfileInfo)


from import_export import resources


class LibResource(resources.ModelResource):

    class Meta:
        model = models.librarydue


# Register your models here.
