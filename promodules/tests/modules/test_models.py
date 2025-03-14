from django.test import TestCase, override_settings
from modules.models import Module

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ModuleModelTest(TestCase):
    def test_create_module(self):
        module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )
        self.assertEqual(module.name, 'Test Module')
        self.assertEqual(module.version, '1.0')
        self.assertEqual(module.status, 'installed')
        self.assertEqual(module.repository, 'https://github.com/herbew/promodules.git')
        self.assertEqual(module.description, 'This is a test module')
        
    def test_update_module(self):
        module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )
        module.name = 'Updated Test Module'
        module.save()
        self.assertEqual(module.name, 'Updated Test Module')

    def test_delete_module(self):
        module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='installed',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )
        module.delete()
        self.assertFalse(Module.objects.filter(name='Test Module').exists())