from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Plan(models.Model):
    """
    Model representing a plan.
    """
    name = models.CharField(max_length=100, verbose_name='Plan Name')
    private = models.BooleanField(default=False, verbose_name='Private Plan')
    height = models.FloatField(default=0, verbose_name='Height')
    weight = models.FloatField(default=0, verbose_name='Weight')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Start Time')
    end_time = models.DateTimeField(auto_now_add=True, verbose_name='End Time')
    month_target = models.FloatField(default=0, verbose_name='Monthly Target')
    final_target = models.FloatField(default=0, verbose_name='Final Target')
    description = models.TextField(verbose_name='Description', blank=True, max_length=450)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.name