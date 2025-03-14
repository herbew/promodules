from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from modules.views import module_list, install_module, upgrade_module, uninstall_module

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ModuleURLTestCase(TestCase):
    def test_module_list_url(self):
        url = reverse('modules:module_list')
        self.assertEqual(url, '/module/list/')
        self.assertEqual(resolve(url).func, module_list)

    def test_install_module_url(self):
        url = reverse('modules:install_module')
        self.assertEqual(url, '/module/install/')
        self.assertEqual(resolve(url).func, install_module)

    def test_upgrade_module_url(self):
        url = reverse('modules:upgrade_module', args=[1])
        self.assertEqual(url, '/module/upgrade/1/')
        self.assertEqual(resolve(url).func, upgrade_module)

    def test_uninstall_module_url(self):
        url = reverse('modules:uninstall_module', args=[1])
        self.assertEqual(url, '/module/uninstall/1/')
        self.assertEqual(resolve(url).func, uninstall_module)
        