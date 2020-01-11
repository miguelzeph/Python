v = [1,2,3,4,5,15,20,35,67,66,89,5,5,5,5,6,7,10,1,2,3,4,5,2,4,5,10,1,2,3,4,5,2,3,5,5,5,5,5,5,5,5,10]


k=0
while True:
	try :
	
		if v[k] == 5:
			
			q = k
			
			while (v[q] != 10):
			
				v[q] = None
				
				q = q+1
			
			k = q
			
			
		
		raw_input()
		k=k+1
		
	except IndexError:
		break
print v