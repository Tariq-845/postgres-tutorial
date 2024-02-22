from sqlalchemy import (
  create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# executing the intructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
# class Programmer(base):
#   __tablename__ = "Programmer"
#   id = Column(Integer, primary_key=True)
#   first_name = Column(String)
#   last_name = Column(String)
#   gender = Column(String)
#   nationality = Column(String)
#   famous_for = Column(String)

# create a class-based model for the "FavouritePlaces" table
class FavouritePlaces(base):
  __tablename__ = "Favourite Places"
  id = Column(Integer, primary_key=True)
  country_name = Column(String)
  capital_city = Column(String)
  population = Column(Integer)



# instead of conenecting to the db directly, we will ask for a session
# create a new instance of sessionmaker, then point to our enginer (the db)
Session = sessionmaker(db)
# opens an actual session by calling Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our "Programmer" table
# ada_lovelace = Programmer(
#   first_name="Ada",
#   last_name="Lovelace",
#   gender="F",
#   nationality="British",
#   famous_for="First Programmer"
# )

# alan_turing = Programmer(
#   first_name="Alan",
#   last_name="Turing",
#   gender="M",
#   nationality="British",
#   famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#   first_name="Grace",
#   last_name="Hopper",
#   gender="F",
#   nationality="American",
#   famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#   first_name="Margaret",
#   last_name="Hamilton",
#   gender="F",
#   nationality="American",
#   famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#   first_name="Bill",
#   last_name="Gates",
#   gender="M",
#   nationality="American",
#   famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#   first_name="Tim",
#   last_name="Berners-Lee",
#   gender="M",
#   nationality="British",
#   famous_for="World Wide Web"
# )

# tariq_ebden = Programmer(
#   first_name="Tariq",
#   last_name="Ebden",
#   gender="M",
#   nationality="South African",
#   famous_for="Dumbest Programmer",
# )

# creating records on our "FavouritePlaces" table
spain = FavouritePlaces(
  country_name="Spain",
  capital_city="Madrid",
  population=4700000
)

japan = FavouritePlaces(
  country_name="Japan",
  capital_city="Tokyo",
  population=125000000
)

germany = FavouritePlaces(
  country_name="Germany",
  capital_city="Berlin",
  population=83000000
)

# add each instance of our programmers to our session
session.add(spain)
session.add(japan)
session.add(germany)

# commit our session to the db
session.commit()

# query the database to find all countries
places = session.query(FavouritePlaces)
for place in places:
  print(
    place.id,
    place.country_name,
    place.capital_city,
    place.population,
    sep=" | "
  )


# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(tariq_ebden)

# remove double ada_lovelace entry
# session.delete(ada_lovelace)


# updating a single record
# programmer = session.query(Programmer).filter_by(id=13).first()
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()

# update multiple records 
# people = session.query(Programmer)
# for person in people:
#   if person.gender == "F":
#     person.gender = "Female"
#   elif person.gender == "M":
#     person.gender = "Male"
#   else:
#     print("Gender not defined")
#   session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#   print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#   confirmation = input("Are you sure you want to delete this record? (y/n) ")
#   if confirmation.lower() == "y":
#     session.delete(programmer)
#     session.commit()
#     print("Programmer has been deleted")
#   else:
#     print("Programmer not deleted")
# else:
#   print("No records found")

# delete multiple records


# query the database to find all "Programmers"
# programmers = session.query(Programmer)
# for programmer in programmers:
#   print(
#     programmer.id,
#     programmer.first_name + " " + programmer.last_name,
#     programmer.gender,
#     programmer.nationality,
#     programmer.famous_for,
#     sep=" | "
#   )