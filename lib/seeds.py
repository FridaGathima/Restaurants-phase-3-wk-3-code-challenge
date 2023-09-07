from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review  # Replace 'your_module_name' with the actual name of your module

engine = create_engine('sqlite:///revi.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create restaurants
restaurant1 = Restaurant(name='Restaurant 1', price=2)
restaurant2 = Restaurant(name='Restaurant 2', price=3)

# Create customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Create reviews and associate them with restaurants and customers
review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

# Add the objects to the session and commit to the database
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

print("Seed data has been created.")