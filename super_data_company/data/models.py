from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "users_user"

    def __str__(self):
        return self.name