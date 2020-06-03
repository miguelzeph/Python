from basic import db, Puppy

# Create all the Tables Models -> dB Table
db.create_all()

#Objetos criados com a Classe Pyppy
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

# add todos OBJETOS tudo de uma vez
db.session.add_all([sam,frank])

# add one by one object
#db.session.add(sam)
#db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
