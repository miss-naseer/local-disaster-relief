from django.contrib.auth.models import Group, User
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import UserProfile  # assuming you already have a UserProfile linked to User

@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    # Define our groups
    roles = ['Volunteer', 'Public']

    for role in roles:
        Group.objects.get_or_create(name=role)




# This signal runs after a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile and assign default role
        UserProfile.objects.create(user=instance, role="public")  


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
