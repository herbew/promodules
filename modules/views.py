from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Module
from .forms import AddModuleForm, UpdateModuleForm

# Function for check is super user
def is_superuser(user):
    return user.is_superuser

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'modules/module_list.html', {'modules': modules})

# Only superuser can access this view
@login_required
@user_passes_test(is_superuser)
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
@user_passes_test(is_superuser)
def upgrade_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = UpdateModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('modules:module_list')
    else:
        form = UpdateModuleForm(instance=module)
    return render(request, 'modules/upgrade_module.html', {'form': form})

# Only superuser can access this view
@login_required
@user_passes_test(is_superuser)
def uninstall_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    #module.delete()
    module.status = 'Uninstalled'
    module.save()
    return redirect('modules:module_list')
    
    
    