import threading
from django.core.management.base import BaseCommand

from System.models import User, Order, Product


users_data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com"},
    {"id": 6, "name": "Frank", "email": "frank@example.com"},
    {"id": 7, "name": "Grace", "email": "grace@example.com"},
    {"id": 8, "name": "Alice", "email": "alice@example.com"},
    {"id": 9, "name": "Henry", "email": "henry@example.com"},
    {"id": 10, "name": None, "email": "jane@example.com"},
]

products_data = [
    {"id": 1, "name": "Laptop", "price": 1000.00},
    {"id": 2, "name": "Smartphone", "price": 700.00},
    {"id": 3, "name": "Headphones", "price": 150.00},
    {"id": 4, "name": "Monitor", "price": 300.00},
    {"id": 5, "name": "Keyboard", "price": 50.00},
    {"id": 6, "name": "Mouse", "price": 30.00},
    {"id": 7, "name": "Laptop", "price": 1000.00},
    {"id": 8, "name": "Smartwatch", "price": 250.00},
    {"id": 9, "name": "Gaming Chair", "price": 500.00},
    {"id": 10, "name": "Earbuds", "price": -50.00},
]

orders_data = [
    {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2},
    {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1},
    {"id": 3, "user_id": 3, "product_id": 3, "quantity": 5},
    {"id": 4, "user_id": 4, "product_id": 4, "quantity": 1},
    {"id": 5, "user_id": 5, "product_id": 5, "quantity": 3},
    {"id": 6, "user_id": 6, "product_id": 6, "quantity": 4},
    {"id": 7, "user_id": 7, "product_id": 7, "quantity": 2},
    {"id": 8, "user_id": 8, "product_id": 8, "quantity": 0},
    {"id": 9, "user_id": 9, "product_id": 1, "quantity": -1},
    {"id": 10, "user_id": 10, "product_id": 11, "quantity": 2},
]


def insert_users():
    for user in users_data:
        User.objects.create(**user)

def insert_products():
    for product in products_data:
        Product.objects.create(**product)

def insert_orders():
    for order in orders_data:
        try:
            Order.objects.create(**order)
        except Exception as e:
            print(f"Error inserting order {order}: {e}")

class Command(BaseCommand):
    help = "Insert data into the database concurrently"

    def handle(self, *args, **kwargs):
        user_thread = threading.Thread(target=insert_users)
        product_thread = threading.Thread(target=insert_products)
        order_thread = threading.Thread(target=insert_orders)

        user_thread.start()
        product_thread.start()
        order_thread.start()

        user_thread.join()
        product_thread.join()
        order_thread.join()

        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))
