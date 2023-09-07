from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')


    def __init__(self, reviews, customers):
        self.reviews = reviews
        self.customers = customers

    def reviews(self):
        return self.reviews

    def customers(self):
        return self.customers
    
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')

    def __init__(self, reviews, restaurant):
        self.reviews = reviews
        self.restaurant = restaurant

    def reviews(self):
        return self.reviews
    
    def restaurant(self):
        return self.restaurant
    
    def full_name(self, first_name, last_name):
        print(f"{first_name} {last_name}")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)  # Make sure this line exists
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer

    # should return the `Customer` instance for this review
    def customer(self):
        return self.customer
    
    # should return the `Restaurant` instance for this review
    def restaurant(self):
        return self.restaurant


    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

