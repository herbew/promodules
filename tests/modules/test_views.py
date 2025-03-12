
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User

from modules.models import Module
from modules.forms import AddModuleForm, UpdateModuleForm


@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ModuleViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )
        
        self.user = User.objects.create_user(
            username='user',
            password='userpassword',
            email='user@example.com'
        )
        
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )
	
    def test_install_module_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:install_module'))
        self.assertEqual(response.status_code, 200)

    def test_install_module_regular_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get(reverse('modules:install_module'))
        self.assertEqual(response.status_code, 302)  # Forbidden
    
    def test_upgrade_module_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:upgrade_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 200)

    def test_upgrade_module_regular_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get(reverse('modules:upgrade_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)  # Forbidden
    
    def test_uninstall_module_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)

    def test_uninstall_module_regular_user(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get(reverse('modules:uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)  # Forbidden
    
    def test_module_list_view(self):
        response = self.client.get(reverse('modules:module_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modules/module_list.html')
        self.assertContains(response, 'Test Module')

    def test_install_module_view(self):
        data = {
            'name': 'New Test Module',
            'version': '2.0',
            'status': 'installed',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is a new test module'
        }
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('modules:install_module'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('modules:module_list'))
        self.assertEqual(Module.objects.count(), 2)

    def test_upgrade_module_view(self):
        data = {
            'name': 'Updated Test Module',
            'version': '1.1',
            'status': 'installed',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is an updated test module'
        }
        self.client.login(username='admin', password='adminpassword')
        
        response = self.client.post(reverse('modules:upgrade_module', args=[self.module.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('modules:module_list'))
        self.module.refresh_from_db()
        self.assertEqual(self.module.name, 'Updated Test Module')

    def test_uninstall_module_view(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('modules:uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('modules:module_list'))
        self.assertEqual(Module.objects.count(), 0)
        
        

class ModuleViewsTest1(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )
        
        self.user = User.objects.create_user(
            username='user',
            password='userpassword',
            email='user@example.com'
        )
        
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='Test Description'
        )

    def test_module_list_view(self):
        response = self.client.get(reverse('modules:module_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Module')

    def test_install_module_view(self):
        self.client.login( username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:install_module'))
        self.assertEqual(response.status_code, 200)

    def test_upgrade_module_view(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:upgrade_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 200)
  
    def test_uninstall_module_view(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('modules:uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)
        
        
        