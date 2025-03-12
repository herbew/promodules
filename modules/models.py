from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20, blank=True, null=True,)
    status = models.CharField(max_length=20, 
    	choices=[('installed', 'Installed'), ('uninstalled', 'Uninstalled')],
    	default='installed'
    	)
    installed_at = models.DateTimeField(auto_now_add=True)
    repository = models.URLField(blank=True, null=True,)
    description = models.TextField(blank=True, null=True,)

    class Meta:
        db_table = 'modules_module'
        unique_together = (("name", "version"),)