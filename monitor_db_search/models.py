from django.db import models

class raw_data_caltalog(models.Model):
    source = models.CharField(max_length=255, null=True)
    source_type = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=255, null=True)
    destination_type = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)


class RawDataCaltalog(models.Model):
    source = models.CharField(max_length=255, null=True)
    source_type = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=255, null=True)
    destination_type = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)