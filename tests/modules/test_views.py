
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from .models import Module
from .forms import AddModuleForm, UpdateModuleForm

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ModuleViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='active',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )

    def test_module_list_view(self):
        response = self.client.get(reverse('module_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modules/module_list.html')
        self.assertContains(response, 'Test Module')

    def test_install_module_view(self):
        data = {
            'name': 'New Test Module',
            'version': '2.0',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is a new test module'
        }
        response = self.client.post(reverse('install_module'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('module_list'))
        self.assertEqual(Module.objects.count(), 2)

    def test_upgrade_module_view(self):
        data = {
            'name': 'Updated Test Module',
            'version': '1.1',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is an updated test module'
        }
        response = self.client.post(reverse('upgrade_module', args=[self.module.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('module_list'))
        self.module.refresh_from_db()
        self.assertEqual(self.module.name, 'Updated Test Module')

    def test_uninstall_module_view(self):
        response = self.client.post(reverse('uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('module_list'))
        self.assertEqual(Module.objects.count(), 0)
        
        
        
        
"""from django.test import TestCase, Client
from django.urls import reverse
from ..models import Module

class ModuleViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='Test Description'
        )

    def test_module_list_view(self):
        response = self.client.get(reverse('module_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Module')

    def test_install_module_view(self):
        response = self.client.get(reverse('install_module'))
        self.assertEqual(response.status_code, 200)

    def test_upgrade_module_view(self):
        response = self.client.get(reverse('upgrade_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 200)

    def test_uninstall_module_view(self):
        response = self.client.get(reverse('uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 200)"""
        
        
        