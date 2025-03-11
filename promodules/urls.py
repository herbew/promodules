from django.contrib import admin
from django.urls import path
from modules import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('module/', views.module_list, name='module_list'),
    path('module/install/', views.install_module, name='install_module'),
    path('module/upgrade/<int:module_id>/', views.upgrade_module, name='upgrade_module'),
    path('module/uninstall/<int:module_id>/', views.uninstall_module, name='uninstall_module'),
]