from django.test import TestCase
from django.urls import reverse

class ModuleURLTestCase(TestCase):
    def test_module_list_url(self):
        url = reverse('module_list')
        self.assertEqual(url, '/module/')

    def test_install_module_url(self):
        url = reverse('install_module')
        self.assertEqual(url, '/module/install/')

    def test_upgrade_module_url(self):
        url = reverse('upgrade_module', args=[1])
        self.assertEqual(url, '/module/upgrade/1/')

    def test_uninstall_module_url(self):
        url = reverse('uninstall_module', args=[1])
        self.assertEqual(url, '/module/uninstall/1/')

        
        
        
        