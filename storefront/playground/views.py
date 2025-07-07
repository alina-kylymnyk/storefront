from django.shortcuts import render
from django.db.models import Q, F, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from store.models import Product, Customer, Collection, OrderItem, Order


def say_hello(request):

    with transaction.atomic():

        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    return render(request, "hello.html", {"name": "Alina"})
