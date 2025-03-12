from django.urls import path
from modules import views

app_name = "modules"

urlpatterns = [
	path('list/', views.module_list, name='module_list'),
    path('install/', views.install_module, name='install_module'),
    path('upgrade/<int:module_id>/', views.upgrade_module, name='upgrade_module'),
    path('uninstall/<int:module_id>/', views.uninstall_module, name='uninstall_module'),
    ]