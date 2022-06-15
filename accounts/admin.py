from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import Account

class AccountAdmin(UserAdmin):

    #defining the displaying items
    list_display = ('email','first_name','last_name' , 'username',
                    'last_login', 'date_joined', 'is_active')

    #to make listed username firstname etc links to open details
    list_display_links = ('email','first_name', 'last_name')

    #tomake below items readonly
    readonly_fields = ('last_login', 'date_joined')

    #descending order
    ordering = ('-date_joined' ,)

    #to make password readonly
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)