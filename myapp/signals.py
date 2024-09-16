import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received, starting slow process...")
    time.sleep(5)  # Simulate a long process
    print("Signal processing finished.")
