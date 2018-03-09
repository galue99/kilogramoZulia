from django.contrib import admin
from .models import User, Weight, Company
from django.http import HttpResponse
from .resources import UserResource
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


class BookResource(resources.ModelResource):
	proveedor = Field()
	operador = Field()
	class Meta:
		model = Weight
		exclude = ('id', )
		widgets = {
			'published': {'format': '%d.%m.%Y'},
		}

	def dehydrate_proveedor(self, weight):
		return '%s  %s' % (weight.provider.first_name, weight.provider.last_name)

	def dehydrate_operador(self, weight):
		return '%s  %s' % (weight.user.first_name, weight.user.last_name)

class BookAdmin(ImportExportModelAdmin):
	resource_class = BookResource

class WeightAdmin(ImportExportModelAdmin):
	class Meta:
		model = Weight
	list_display = ('provider', 'date', 'time')

admin.site.register(User)
admin.site.register(Company)
