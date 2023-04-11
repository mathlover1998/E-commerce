# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import UserMetadata

# @receiver(post_save, sender=User)
# def create_user_metadata(sender, instance, created, **kwargs):
#     if created:
#         UserMetadata.objects.create(user=instance)