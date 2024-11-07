from django.db import models

class VacantHome(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    registration_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    safety_grade = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title} ({self.location})"
    

class CommunityBoard(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)