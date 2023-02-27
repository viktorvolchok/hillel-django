from threading import Thread
from time import sleep
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from books.telegram import send_telegram_message
from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


@receiver(post_save, sender=Order)
def on_order_save_in_thread(sender, instance: Order, created, **kwargs):
    if created:
        thread = Thread(target=on_order_save, args=(instance,))
        thread.start()


def on_order_save(instance):
    sleep(5)
    # text = f"ORDER {instance.id} CREATED.\nPhone: {instance.customer.phone_number}\n"
    text = f"""
ORDER {instance.id} CREATED.
Phone: {instance.customer.phone_number}
"""

    for line_item in instance.line_items.all():
        text += f"{line_item.book.name} - {line_item.quantity}\n"

    send_telegram_message(text)
