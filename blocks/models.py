from django.db import models

class Block(models.Model):
    
    block_hash = models.CharField(max_length=256)
    latest_hash = models.CharField(max_length=256, default=None)
    