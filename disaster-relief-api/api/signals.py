from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    # Define our groups
    roles = ['Volunteer', 'Public']

    for role in roles:
        Group.objects.get_or_create(name=role)


from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import UserProfile  # assuming you already have a UserProfile linked to User

User = get_user_model()

# This signal runs after a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile and assign default role
        UserProfile.objects.create(user=instance, role="public")  
        # 👆 you can change "public" to "volunteer" if you want default volunteer role
