from django.db import models

# Create your models here.

class Plan(models.Model):
    """
    Model representing a plan.
    """
    name = models.CharField(max_length=100, verbose_name='Plan Name')
    description = models.TextField(verbose_name='Description', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.name