from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    TANK = 'TA'
    HEALER = 'HE'
    DD = 'DD'
    MERCHANT = 'ME'
    GUILDMASTER = 'GM'
    QUESTGIVER = 'QG'
    BLACKSMITH = 'BS'
    SKINNER = 'SK'
    POTIONEER = 'PO'
    SPELLMASTER = 'SO'
    
    CATEGORIES = [
        (TANK, 'Танк'),
        (HEALER, 'Хил'),
        (DD, 'ДД'),
        (MERCHANT, 'Торговец'),
        (GUILDMASTER, 'Гилдмастер'),
        (QUESTGIVER, 'Квестгивер'),
        (BLACKSMITH, 'Кузнец'),
        (SKINNER, 'Кожевник'),
        (POTIONEER, 'Зельевар'),
        (SPELLMASTER, 'Мастер Заклинаний'),
    ]
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    upload = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email