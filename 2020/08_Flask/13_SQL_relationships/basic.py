# Basic.py
from models import db, Puppy, Owner, Toy

# Creating 2 pupis

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add Puppies to DB
db.session.add_all([rufus,fido])
db.session.commit()

#Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first() #or .all[0]
print(rufus)

# Cheate Owner Object
jose = Owner('Jose',rufus.id)

# Give Rufus some Toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# GRAB RUFUS after THOSE ADDITIONS
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())

