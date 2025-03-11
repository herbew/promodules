from django.shortcuts import render, get_object_or_404, redirect
from .models import Module
from .forms import AddModuleForm, UpdateModuleForm

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'modules/module_list.html', {'modules': modules})

def install_module(request):
    if request.method == 'POST':
        form = AddModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = AddModuleForm()
    return render(request, 'modules/install_module.html', {'form': form})

def upgrade_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = UpdateModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = UpdateModuleForm(instance=module)
    return render(request, 'modules/upgrade_module.html', {'form': form})

def uninstall_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.delete()
    return redirect('module_list')