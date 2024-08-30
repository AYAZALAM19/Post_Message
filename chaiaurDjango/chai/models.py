from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE = [
        ('ML', 'MASALA'),
        ('L', 'LASSI'),
        ('C', 'COFFEE'),
        ('T', 'TEA'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)

    def __str__(self):
        return self.name


class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# Many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')  # Fixed typo

    def __str__(self):
        return self.name

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, related_name='certificate', on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'  # Fixed typo
