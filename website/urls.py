from django.urls import path
from website import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'website'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.adminEmployeeLogin, name='adminEmployeeLogin'),
    path('login_view/', views.login_view, name='login_view'),
    path('search_results/', views.search_results, name='search_results'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
]
