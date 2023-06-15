from django.db import models



class Form(models.Model):
    visitor_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, verbose_name="Email(optional):")
    subject = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.visitor_name}'
