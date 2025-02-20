from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200) # Task name
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)  # Task complete hai ya nahi

    def __str__(self):
        return self.title # Admin panel ka name show hoga


# Create your models here.
