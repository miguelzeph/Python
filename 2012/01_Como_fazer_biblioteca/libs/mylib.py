# -*- coding: utf-8 -*-

def fatorial(num):
	if num < 0:
		return None
	
	fat=1
	
	for i in range(1, num+1):
		fat=fat*i
	
	return fat

def quadrado(num):
	return num*num
