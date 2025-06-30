from django.contrib import admin
from .models import Emp, Client,Service, Withdraw, Deposit, Project, Task
from django.utils.html import format_html

def active_selected_record(self, request, queryset):
    queryset.update(is_active=True)

def inactive_selected_record(self, request, queryset):
    queryset.update(is_active=False)

class EmpAdmin(admin.ModelAdmin):
    list_display=['employee_id','employee_pass','image_tag','name','phone','email','address','join_date','salary','created_on','is_active']

    def image_tag(self, obj):
        return format_html('<img src="{}" border-radius: "15px" width="30px" height="30px" style="border-radius:15px;"/>'.format(obj.img.url))

    image_tag.short_description = 'Image'
    
    list_filter=['salary','is_active']
    search_fields=['name']

class ClientAdmin(admin.ModelAdmin):
    list_display=['client_id','name','service','phone','email','address','pincode','created_on','is_active']
    list_filter=['service','is_active']
    search_fields=['name','service']

class ProjectAdmin(admin.ModelAdmin):
    list_display=['project_id','project_name','client','start_date','work_on','status']
    list_filter=['project_name','is_active']
    search_fields=['project_name']

class ServiceAdmin(admin.ModelAdmin):
    list_display=['name','price','photo','video','created_on','is_active']
    
class DepositAdmin(admin.ModelAdmin):
    list_display=['client','name','phone','pay','pending','total','created_on']
    list_filter=['name','pay','pending']
    search_fields=['name','pay','client']

class WithdrawAdmin(admin.ModelAdmin):
    list_display=['name','purpose','amount','created_on']
    list_filter=['amount','amount']
    search_fields=['name','amount','purpose']

class TaskAdmin(admin.ModelAdmin):
    list_display=['title','assigned_to','deadline','is_completed','description','created_on']
    list_filter=['title','assigned_to','is_completed']
    


admin.site.register(Emp, EmpAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.add_action(active_selected_record)
admin.site.add_action(inactive_selected_record)