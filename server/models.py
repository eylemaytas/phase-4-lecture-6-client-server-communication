from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# class Destination(db.Model, SerializerMixin):
#     __tablename__ = 'destinations'

#     id = db.Column(db.Integer, primary_key=True)

#     city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

#     #Relationships
#     city = db.relationship('City', back_populates='destinations')

#     #Serializer
#     serialize_rules = ('-city',)

class City(db.Model, SerializerMixin):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)

    continent_id = db.Column(db.Integer, db.ForeignKey('continents.id'))

    #Relationships
    continent = db.relationship('Continent', back_populates='cities')
    foods = db.relationship('Food', back_populates='city')
    # destinations = db.relationship('Destination', back_populates='city')

    #Serializer
    serialize_rules = ('-continent',)

class Food(db.Model, SerializerMixin):
    __tablename__ = 'foods'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    restaurant_recommendation = db.Column(db.String, nullable=False)

    # continent_id = db.Column(db.Integer, db.ForeignKey('continents.id'))
    # destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    #Relationships
    # continent = db.relationship('Continent', back_populates='foods')
    # destination = db.relationship('Destination', back_populates='foods')
    city = db.relationship('City', back_populates='foods')

    #Serializer
    serialize_rules=('-continent', '-destination')
    

class Continent(db.Model, SerializerMixin):
    __tablename__ = 'continents'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    # food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))
    # city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    #Relationships
    cities = db.relationship('City', back_populates='continent')
    # foods = db.relationship('Food', back_populates='continent')

    #Serializer
    serialize_rules=('-cities', '-foods')

# class User(db.Model, SerializerMixin):
#     __tablename__ = 'users'


#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable=False)
#     username = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)
#     created_at = db.Column(db.DateTime, default = datetime.now)
#     updated_at = db.Column(db.Datetime, default=datetime.now, onupdate=datetime.now)

#     #Relationships
#     blogs = db.relationship('Blog', backref='user')

#     #Serializer


# class Blog(db.Model, SerializerMixin):
#     __tablename__ = 'blogs'

    
#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.String, nullable=False)
#     blog_post = db.Column(db.String, nullable=False)
#     like_count = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, default = datetime.now)
#     updated_at = db.Column(db.Datetime, default=datetime.now, onupdate=datetime.now)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     #Relationships

#     #Serializer

















# class Hotel(db.Model, SerializerMixin):
#     __tablename__ = 'hotels'

#     serialize_rules = ('-reviews',)

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False, unique=True)
#     image = db.Column(db.String, nullable=False)

#     reviews = db.relationship('Review', back_populates='hotel')

#     customers = association_proxy('reviews', 'customer',
#         creator=lambda c: Review(customer=c))

#     @validates('name')
#     def validate_name(self, key, value):
#         if len(value) < 5:
#             raise ValueError(f"{key} must be at least 5 characters long.")
#         return value
    
#     def __repr__(self):
#         return f"Hotel # {self.id}: {self.name} hotel"

# class Customer(db.Model, SerializerMixin):
#     __tablename__ = 'customers'

#     serialize_rules = ('-reviews',)

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable=False)

#     reviews = db.relationship('Review', back_populates='customer')

#     hotels = association_proxy('reviews', 'hotel',
#         creator=lambda h: Review(hotel=h))

#     __table_args__ = (
#         db.CheckConstraint('(first_name != last_name)'),
#     )

#     @validates('first_name', 'last_name')
#     def validate_first_name(self, key, value):
#         if value is None:
#             raise ValueError(f"{key} cannot be null.")
#         elif len(value) < 4:
#             raise ValueError(f"{key} must be at least 4 characters long.")
#         return value
    
#     def __repr__(self):
#         return f"Customer # {self.id}: {self.first_name} {self.last_name}"
    
# class Review(db.Model, SerializerMixin):
#     __tablename__ = 'reviews'

#     serialize_rules = ('-hotel.reviews', '-customer.reviews')

#     id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.Integer)

#     hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

#     hotel = db.relationship('Hotel', back_populates='reviews')
#     customer = db.relationship('Customer', back_populates='reviews')

#     def __repr__(self):
#         return f"Review # {self.id}: {self.customer.first_name} {self.customer.last_name} left of a review for {self.hotel.name} with a rating of {self.rating}."