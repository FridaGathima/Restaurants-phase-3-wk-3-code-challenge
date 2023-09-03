<h1>Phase 3 Code Challenge: Restaurants</h1>

For this assignment, we'll be working with a restaurant review domain.

We have three models: 

 - Restaurant 
 - Review 
 - Customer

For our purposes, a Restaurant has many Reviews, a Customer has many Reviews, and a Review belongs to a Restaurant and to a Customer.

Restaurant - Customer is a many to many relationship.

 <h2>Topics</>

- SQLAlchemy Migrations

- SQLAlchemy Relationships

- Class and Instance Methods

- SQLAlchemy Querying

Navigate to **lib folder** which has 3 files i.e. **customer.py**, **restaurant.py** and **review.py** to see the solutions.

<h2>What You Need to Have</h2>

You need to have migrations and models for the initial `Restaurant` and `Customer` models, and seed data for some `Restaurant`s and `Customer`s.

The schema currently looks like this: 

**restaurants table**
| Column	 | Type    |
|----------- |-------- |
| name	     | String  |
| price	     | Integer |


**customers Table**
| Column	   | Type   |
|--------------|--------|
| first_name   | String |
| last_name	   | String |


You will need to create the migration for the `reviews` table using the attributes specified in the deliverables below.

 

**Deliverables**

Write the following methods in the classes. Feel free to build out any helper methods if needed.

Remember: SQLAlchemy give your classes access to a lot of methods already! Keep in mind what methods SQLAlchemy gives you access to on each of your classes when you're approaching the deliverables below.

**Migrations**
Before working on the rest of the deliverables, you will need to create a migration for all tables.

 
- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to a  `Customer`.  In your migration, create any columns your `reviews` table will

 need to establish these relationships.

The `reviews` table should also have:  - A `star_rating` column that stores an integer.
 

After creating the `reviews` table using a migration, use the `seeds.py` file to create instances of all your classes so you can test your code.

 

**Once you've set up your tables**, work on building out the following deliverables.

 

**Object Relationship Methods**
 

Use SQLAlchemy query methods where appropriate.

 

**Review**

- `Review customer()`

 - should return the `Customer` instance for this review

- `Review restaurant()`

 - should return the `Restaurant` instance for this review

 

**Restaurant**
 

- `Restaurant reviews()`

 - returns a collection of all the reviews for the `Restaurant`

- `Restaurant customers()`

 - returns a collection of all the customers who reviewed the `Restaurant`

 

**Customer**
 

- `Customer reviews()`

 - should return a collection of all the reviews that the `Customer` has left

- `Customer restaurants()`

 - should return a collection of all the restaurants that the `Customer` has reviewed

 

Check that these methods work before proceeding. For example, you should be able to call `session.query(Customer).first().restaurants` and see a list of the restaurants for the first customer in the database based on your seed data; and `session.query(Review).first().customer` should return the customer for the first review in the database.

 

 **Aggregate and Relationship Methods**
 

 **Customer**
 

- `Customer full_name()`

 - returns the full name of the customer, with the first name and the last name  concatenated, Western style.

- `Customer favorite_restaurant()`

 - returns the restaurant instance that has the highest star rating from this customer

- `Customer add_review(restaurant, rating)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and a rating

 - creates a new review for the restaurant with the given `restaurant_id`

- `Customer delete_reviews(restaurant)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and

 - removes **all** their reviews for this restaurant

 - you will have to delete rows from the `reviews` table to get this to work!

 

**Review**

- `Review full_review()`

 - should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

 

**Restaurant**

- `Restaurant fanciest(), this method should be a class method`

 - returns _one_ restaurant instance for the restaurant that has the highest   price

- `Restaurant all_reviews()`

 - should return an list of strings with all the reviews for this restaurant

   formatted as follows:

[

 "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

 "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

]

<h2>Languages</h2>

- Python
- Github
- Git
- SQLAlchemy

<h2>Author</h2>

Frida Nduta Gathima 

<h2>Licence</h2>

Copyright (c) 2023 Frida Nduta Gathima.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.