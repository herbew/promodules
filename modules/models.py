from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    status = models.CharField(max_length=20, 
    	choices=[('installed', 'Installed'), ('uninstalled', 'Uninstalled')]
    	)
    installed_at = models.DateTimeField(auto_now_add=True)
    repository = models.URLField()
    description = models.TextField()

    class Meta:
        db_table = 'modules_module'