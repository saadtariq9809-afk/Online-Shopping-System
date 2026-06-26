from abc import ABC, abstractmethod
import random

# =========================
# POLYMORPHISM: Payment Interface
# =========================
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def generate_receipt(self):
        pass

# Concrete Payment Classes
class JazzCashPayment(Payment):
    def pay(self, amount): 
        return f"Rs.{amount} paid successfully via JazzCash."
    def generate_receipt(self): 
        return f"JZ-{random.randint(1000, 9999)}"

class CreditCardPayment(Payment):
    def pay(self, amount): 
        return f"Rs.{amount} paid successfully via Credit Card."
    def generate_receipt(self): 
        return f"CC-{random.randint(1000, 9999)}"

class PayPalPayment(Payment):
    def pay(self, amount): 
        return f"Rs.{amount} paid successfully via PayPal."
    def generate_receipt(self): 
        return f"PP-{random.randint(1000, 9999)}"

# =========================
# CORE CLASSES
# =========================
class FoodItem:
    def __init__(self, item_id, name, price, category, image_url):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.image_url = image_url

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Encapsulation
        self.cart = []
    
    @property
    def password(self): 
        return self.__password

# =========================
# SYSTEM DATA & MENU (Fixed High-Resolution Images)
# =========================
users_db = {}

# These links are direct-source to ensure they load reliably in your Flask app.
menu_items = [
    FoodItem(1, "Zinger Burger", 550, "Fast Food", "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500"),
    FoodItem(2, "Beef Steak Burger", 850, "Fast Food", "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500"),
    FoodItem(3, "Chicken Tikka Pizza", 1400, "Pizza", "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500"),
    FoodItem(4, "Fajita Pizza", 1350, "Pizza", "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=500"),
    FoodItem(5, "Chicken Shawarma", 300, "Local", "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=500"),
    FoodItem(6, "Platter Shawarma", 650, "Local", "https://images.unsplash.com/photo-1719282431723-9d0f4370d4bc?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    FoodItem(7, "Loaded Fries", 450, "Sides", "https://images.unsplash.com/photo-1585109649139-366815a0d713?w=500"),
    FoodItem(8, "Garlic Mayo Fries", 350, "Sides", "https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=500"),
    FoodItem(9, "Chicken Biryani", 450, "Desi", "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?q=80&w=1188&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    FoodItem(10, "Chicken Karahi", 1200, "Desi", "https://images.unsplash.com/photo-1603496987351-f84a3ba5ec85?w=500"),
    FoodItem(11, "Mint Margarita", 250, "Drinks", "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=500"),
    FoodItem(12, "Soft Drink", 150, "Drinks", "https://images.unsplash.com/photo-1543253687-c931c8e01820?w=500"),
]