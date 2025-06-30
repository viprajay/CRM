"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website import views

admin.site.site_header = "CRM | CRM Application"
admin.site.site_title = "CRM | CRM Application"
admin.site.index_title = "Welcome to CRM"

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('project/', views.project, name='project'),
    path('client/', views.client, name='client'),
    path('index/', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('revenue/', views.revenue, name='revenue'),
    path('deposit/', views.deposit, name='deposit'),
    path('forgot/', views.forgot, name='forgot'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('search_results/', views.search_results, name='search_results'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
    path('employee/login/', views.employee_login, name='employee_login'),
    path('adminEmployeeLogin/', views.adminEmployeeLogin, name='adminEmployeeLogin'),
    path('employee/profile/update/', views.update_employee_profile, name='employee_profile_update'),
    path('accounts/',include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
