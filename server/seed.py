#!/usr/bin/env python3

from app import app
from models import db, City, Food, Continent

with app.app_context():
    
    
    City.query.delete()
    Food.query.delete()
    Continent.query.delete()

    cities = []
    cities.append(City(name="Istanbul", image="https://www.travelandleisure.com/thmb/UXNrwYTm3z1CAEBl8z_sTxnyGEw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/istanbul-turkey-ISTANBULTG0721-a987bb021e5e4b42b069ba2518cde276.jpg",language="Turkish",continent_id=1))
    cities.append(City(name="Japan", image="https://rare-gallery.com/uploads/posts/350713-4k-wallpaper.jpg",language="Japanese",continent_id=2))
    cities.append(City(name="Morocco", image="https://media.timeout.com/images/105812493/1920/1080/image.jpg",language="Arabic",continent_id=3))
    cities.append(City(name="Sydney", image="https://www.riotgames.com/darkroom/2880/da80743860ce2a42d007f63076c3b73e:5d5618d142eae7c6f41a9e98522c4d12/riot-games-sydney-austrailia-office-page.png",language="English",continent_id=4))
    cities.append(City(name="New York City", image="https://hips.hearstapps.com/hmg-prod/images/gettyimages-688899881-1519413300.jpg?crop=1.00xw:0.756xh;0,0.134xh&resize=1200:*",language="English",continent_id=5))
    cities.append(City(name="Buenos Aires", image="https://www.travelandleisure.com/thmb/udBNy6Hr0U178om0bdoHWvYulDk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/world-class-design-buenos-aires-BAVISIT0418-5e990a610aab499bb9991771dac5fb54.jpg", language="Spanish",continent_id=6))

    continents = []
    continents.append(Continent(name="Europe",image="https://thumbs.dreamstime.com/z/vector-illustration-political-map-europe-european-continent-four-colors-country-name-labels-vector-illustration-cool-158754686.jpg"))
    continents.append(Continent(name="Asia",image="https://p4.wallpaperbetter.com/wallpaper/108/393/213/high-resolution-images-of-nature-3840x2160-wallpaper-preview.jpg",))
    continents.append(Continent(name="Africa",image="https://www.wallpapers13.com/wp-content/uploads/2019/09/Giraffe-Family-Giraffidae-the-tallest-living-land-animal-and-largest-survivor-Wild-Animals-from-Africa-4K-Ultra-HD-Wallpaper-for-Desktop-Laptop-840x525.jpg"))
    continents.append(Continent(name="Australia and Ocenia", image="https://cdn.britannica.com/66/194766-050-5908DD25/canyon-swell-reef-sunlight-water-surface-Pacific.jpg"))
    continents.append(Continent(name="North America", image="https://wallpapercave.com/dwp2x/wp10946351.jpg"))
    continents.append(Continent(name="South America", image="https://img.theculturetrip.com/1440x807/smart/wp-content/uploads/2021/04/kerkmt-e1618321977695.jpg"))

    foods = []
    foods.append(Food(name="kebap",image="https://images.deliveryhero.io/image/fd-tr/LH/wvnd-hero.jpg",description="too good to be true", restaurant_recommendation="eylemin yeri",city_id=1))

    


    # customers = []
    # customers.append(Customer(first_name="Alice", last_name="Baker"))
    # customers.append(Customer(first_name="Barry", last_name="Smith"))
    # customers.append(Customer(first_name="Chris", last_name="Jones"))

    # reviews = []
    # reviews.append(Review(hotel_id=1, customer_id=1, rating=5))
    # reviews.append(Review(hotel_id=2, customer_id=1, rating=5))
    # reviews.append(Review(hotel_id=1, customer_id=2, rating=4))
    # reviews.append(Review(hotel_id=1, customer_id=1, rating=3))

    db.session.add_all(cities)
    db.session.add_all(continents)
    db.session.add_all(foods)
    db.session.commit()
    print("🌱 Cities,continents, foods and destinations successfully seeded! 🌱")
