from django.db import models

class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ip = models.IPAddressField()
    port = models.IntegerField()
    private = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
