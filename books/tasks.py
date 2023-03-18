from celery import shared_task
from django.core.mail import EmailMessage
from django.db.models import Sum

from books.models import Order, Book, OrderLineItem, Author
from books.telegram import send_telegram_message

@shared_task
def run_every_5_seconds():
    print("The task is running every 5 seconds...")


@shared_task(autoretry_for=(BaseException,), retry_backoff=2)
def new_order_created(order_id):
    instance = OrderLineItem.objects.get(id=order_id)
    book_name = instance.book.name
    quantity = instance.quantity
    b: Book = Book.objects.get(name=book_name)
    authors = b.authors.all()

    for author in authors:
        if author.telegram_account_id:
            text = f'"Hi, {author.first_name}! You have a your book sold ({quantity} inst.). Sincerely, your Viktor ' \
                   f'Volchok"'
            send_telegram_message(text, author.telegram_account_id)


@shared_task
def statistic_sending():
    authors = Author.objects.annotate(total_count_sold=Sum('book__count_sold'))
    for author in authors:
        if author.telegram_account_id:
            text = f'Hi, {author.first_name}! There is already {author.total_count_sold} of your books being sold"'
            send_telegram_message(text, author.telegram_account_id)
