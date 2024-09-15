from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here - first interview model

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    code_skills = models.IntegerField(null=False, blank=False)
    project_presentation = models.IntegerField(null=False, blank=False)
    knowledge = models.IntegerField(null=False, blank=False)
    confidence = models.IntegerField(null=False, blank=False)
    notes = models.TextField(blank=True,null=True)
    
    @property
    def total_grade(self):
        fields = [self.code_skills, self.project_presentation, self.knowledge, self.confidence] 
        return sum(fields) / len(fields)

    
    def __str__(self):
        return f"{self.company_name} - {self.position}"
    

