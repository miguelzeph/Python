from basic import db, Puppy

##CRUD###
#Create
#Read
#Update
#Delete
#########

## Create ##
my_puppy = Puppy('Rufus',5)

db.session.add(my_puppy)
db.session.commit()


## Read ##
all_puppies = Puppy.query.all() # List of Puppies object in the Table
print(all_puppies)


# Select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)


# Filters

# pelo name
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
# ou pela idade
#puppy_frankie = Puppy.query.filter_by(age = 4)

print(puppy_frankie.all()) # -> "Frankie is 3 years old"


## UPDATE ##
first_puppy = Puppy.query.get(1) # Pegou o de id=1... que é o Frankie
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


#OBSSSSSS>>>> SE você rodar mais de uma vez ele vai
# dar erro, pois você já deletou  uma vez!!!!!!
# ... delete o data.sqlite e rode novamente tudo

## Delete ##
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


all_puppies = Puppy.query.all()
print(all_puppies)