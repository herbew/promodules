from django.test import TestCase, override_settings
from .forms import AddModuleForm, UpdateModuleForm
from .models import Module

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class AddModuleFormTestCase(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'Test Module',
            'version': '1.0',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is a test module'
        }
        form = AddModuleForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'version': '1.0',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is a test module'
        }
        form = AddModuleForm(data)
        self.assertFalse(form.is_valid())

class UpdateModuleFormTestCase(TestCase):
    def setUp(self):
        self.module = Module.objects.create(
            name='Test Module',
            version='1.0',
            status='active',
            repository='https://github.com/herbew/promodules.git',
            description='This is a test module'
        )

    def test_valid_form(self):
        data = {
            'name': 'Updated Test Module',
            'version': '1.1',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is an updated test module'
        }
        form = UpdateModuleForm(data, instance=self.module)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'version': '1.1',
            'status': 'active',
            'repository': 'https://github.com/herbew/promodules.git',
            'description': 'This is an updated test module'
        }
        form = UpdateModuleForm(data, instance=self.module)
        self.assertFalse(form.is_valid())