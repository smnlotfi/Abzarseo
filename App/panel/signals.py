from django.db.models.signals import post_save
from django.dispatch import receiver
from accounting.models import HowMuchUse
from django.contrib.auth.models import User




@receiver(post_save,sender=User)
def Uses_number(sender,instance,created,**kwargs):
    if created:
        HowMuchUse.objects.create(user=instance,usesnumber=0)
