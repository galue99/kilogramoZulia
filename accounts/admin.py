from django.contrib import admin
from .models import User, Weight, Company, Tara
from django.http import HttpResponse
from .resources import UserResource
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin


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


class AccountAdmin(UserAdmin):
	class Meta:
		model = User
	fieldsets = (
        (None, {
            'fields': ('alias', 'dni', 'email', 'first_name', 'password', 'username')
        }),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
	list_filter = ('alias', 'dni')
	search_fields = ['alias','dni']
	list_display = ('id', 'alias', 'first_name', 'last_name', 'dni', 'company', 'model_pic',)
	readonly_fields = ('admin_photo',)

admin.site.register(User, AccountAdmin)
admin.site.register(Company)
admin.site.register(Tara)
admin.site.register(Weight, WeightAdmin)

