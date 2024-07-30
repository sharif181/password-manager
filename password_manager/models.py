from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class PasswordStore(models.Model):
    website_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website_link = models.URLField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.website_name
