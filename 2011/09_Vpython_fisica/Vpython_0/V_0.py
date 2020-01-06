
import visual

coords = (-3, 3)

cor1 = (0.9, 0.9, 1.0)

cor2 = (0.5, 0.5, 0.6)

for x in coords:
	for y in coords:
		for z in coords:

			visual.sphere(pos=(x, y, z), color=cor1)

for x in coords:
	for z in coords:


		visual.cylinder(pos=(x, 3, z), color=cor2,
			radius=0.25, axis=(0, -6, 0))
	for y in coords:
		visual.cylinder(pos=(x, y, 3), color=cor2,
			radius=0.25, axis=(0, 0, -6))
for y in coords:
	for z in coords:
		visual.cylinder(pos=(3, y, z), color=cor2,
			radius=0.25, axis=(-6, 0, 0))		