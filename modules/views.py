from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Module
from .forms import AddModuleForm, UpdateModuleForm


def synch_module():
    try:
        for m in settings.INSTALLED_MODULE:
            module, created = Module.objects.get_or_create(name=m)
            module.save()
    except:
        raise
# Function for check is super user
def is_superuser(user):
    return user.is_superuser
    
def user_is_superuser(view_func):
    decorated_view_func = user_passes_test(
        is_superuser,
        login_url=None,  # If you want to redirect to the login page, fill in the login URL.
        redirect_field_name=None,
    )(view_func)
    
    def _wrapped_view(request, *args, **kwargs):
        if not is_superuser(request.user):
            return HttpResponseForbidden("You do not have permission to access this page.")
        return decorated_view_func(request, *args, **kwargs)
    
    return _wrapped_view

def module_list(request):
    modules = Module.objects.all()
    synch_module()
    return render(request, 'modules/module_list.html', {'modules': modules})

# Only superuser can access this view
@login_required
@user_is_superuser
def install_module(request):
    if request.method == 'POST':
        form = AddModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modules:module_list')
    else:
        form = AddModuleForm()
    return render(request, 'modules/install_module.html', {'form': form})

# Only superuser can access this view
@login_required
@user_is_superuser
def upgrade_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = UpdateModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            module.status = 'installed'
            module.save()
            return redirect('modules:module_list')
    else:
        form = UpdateModuleForm(instance=module)
    return render(request, 'modules/upgrade_module.html', {'form': form})

# Only superuser can access this view
@login_required
@user_is_superuser
def uninstall_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    #module.delete()
    module.status = 'uninstalled'
    module.save()
    return redirect('modules:module_list')
    
    
    