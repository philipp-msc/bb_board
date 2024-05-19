
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Ad, Response

@receiver(post_save, sender=Ad)
def send_new_ad_notification(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        for user in users:
            send_mail(
                subject='Новое объявление на сайте',
                message=f'На сайте было добавлено новое объявление: "{instance.title}".\n'
                        f'Категория: {instance.get_category_display()}\n'
                        f'Автор: {instance.author.username}\n'
                        f'Дата: {instance.date}\n\n'
                        f'Текст объявления:\n{instance.text}\n\n'
                        f'Ссылка на объявление: http://127.0.0.1:8000/ad/{instance.pk}/',
                from_email='sf.mailbox@yandex.ru',  
                recipient_list=[user.email],
                
            )

@receiver(post_save, sender=Response)
def send_new_response_notification(sender, instance, created, **kwargs):
    if created:
        ad = instance.ad
        author = ad.author
        send_mail(
            subject='Новый отклик на ваше объявление',
            message=f'На ваше объявление "{ad.title}" был оставлен новый отклик.\n'
                    f'Автор отклика: {instance.author.username}\n'
                    f'Текст отклика:\n{instance.text}\n\n'
                    f'Ссылка на объявление: http://127.0.0.1:8000/ad/{ad.pk}/',
            from_email='sf.mailbox@yandex.ru',  
            recipient_list=[author.email],
        )

@receiver(post_save, sender=Response)
def send_response_accepted_notification(sender, instance, created, **kwargs):
    if not created and instance.status:
        author = instance.author
        ad = instance.ad
        send_mail(
            subject='Ваш отклик принят',
            message=f'Ваш отклик на объявление "{ad.title}" был принят.\n\n'
                    f'Ссылка на объявление: http://127.0.0.1:8000/ad/{ad.pk}/',
            from_email='sf.mailbox@yandex.ru',  
            recipient_list=[author.email],
        )

@receiver(post_delete, sender=Response)
def send_response_deleted_notification(sender, instance, **kwargs):
    author = instance.author
    ad = instance.ad
    send_mail(
        subject='Ваш отклик удален',
        message=f'Ваш отклик на объявление "{ad.title}" был удален.\n\n'
                f'Ссылка на объявление: http://127.0.0.1:8000/ad/{ad.pk}/',
        from_email='sf.mailbox@yandex.ru',  
        recipient_list=[author.email],
    )