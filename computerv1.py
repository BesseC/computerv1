#!/usr/bin/env python3
# coding: utf-8

import re

def get_coef(tab):
	res = 0
	i = 1
	for temp in tab:
		coef = temp.replace(" ", "")
		if i == 2:
			coef = float(coef) * -1 
		res += float(coef)
		i += 1
	return res

def solve_quadratic(coef):
	a = coef[2]
	b = coef[1]
	c = coef[0]
	d = b * b - 4 * a * c
	if d == 0:
		print("Discriminant is equal to 0\nThe solution is: {r}".format(r = -(b / 2 * a)))
	elif d < 0:
		print("Discriminant is strictly negative\nThe two solutions are 2 complex conjugates:")
		print("x0 = {r} + i * {c}".format(r =  -(b / 2 * a), c = (-d)**(.5) / 2 * a))
		print("x1 = {r} - i * {c}".format(r =  -(b / 2 * a), c = (-d)**(.5) / 2 * a))
	else:
		print("Discriminant is strictly positive\nThe two solutions are 2 real number:")
		print("x0 = {r}".format(r =  -(b - d**(.5)) / (2 * a)))
		print("x1 = {r}".format(r =  -(b + d**(.5)) / (2 * a)))

def solve_eq(coef):
	if len(coef) == 3 and coef[2] != 0:
		solve_quadratic(coef)
	elif len(coef) == 2 or coef[2] == 0:
		print("The solution is: {r}".format(r = -(coef[0] / coef[1])))		
	else:
		print("Every real number are solution")

line = input("Enter an equation: ")
i = 0
coef = []
while(re.findall("\s?([ +-]*[0-9]*\.?[0-9]*) \* X\^{j}".format(j = i), line)):
	tab = re.findall("\s?([ +-]*[0-9]*\.?[0-9]*) \* X\^{j}".format(j = i), line)
	coef.append(get_coef(tab))
	i += 1
print("Polynomial degree:", len(coef) - 1)
i = 0
print("Reduced form : ", end = '')
for t in coef:
	if i > 0 and t >= 0:
		print('+', end = '')
	print("{nb} * X^{e} ".format(nb = t, e = i), end = '')
	i += 1	
print ("= 0")
if (len(coef) > 3):
	print("The polynomial degree is stricly greater than 2, I can't solve.")
else:
	solve_eq(coef)
