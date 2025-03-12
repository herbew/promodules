from django.test import TestCase, Client, override_settings
from django.urls import reverse
from modules.models import Module

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ModuleTemplatesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )

    def test_module_list_template(self):
        response = self.client.get(reverse('modules:module_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modules/module_list.html')
        self.assertContains(response, 'Test Module')
        self.assertContains(response, '1.0')
        self.assertContains(response, 'installed')

    def test_install_module_template(self):
        response = self.client.get(reverse('modules:install_module'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modules/install_module.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Install Module')

    def test_upgrade_module_template(self):
        response = self.client.get(reverse('modules:upgrade_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modules/upgrade_module.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Upgrade Module')

    def test_uninstall_module_template(self):
        response = self.client.get(reverse('modules:uninstall_module', args=[self.module.id]))
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'modules/module_list.html')
        #self.assertContains(response, 'Are you sure you want to uninstall Test Module?')
        #self.assertContains(response, '<form method="post">')
        
        
        
        
        