print("="*70)    
print("         WELCOME IN CORDINATE GEOMETRY    ")
print("=" *70)
def distance(a, b, c, d):
	return((c - a)**2 + (d - b)**2)**0.5
def mid(a, b):
	return(a +b)/2
x1 = float(input("Entre your x of vertics A :"))
y1 = float(input("Enter your y of vertics A: "))
x2= float(input("Enter your x of vertics B :"))
y2= float(input("Enter your y of vertics B :")) 
x3 = float(input("Entre your x of vertics C:"))
y3 = float(input("Enter your y of vertics C: "))
x4= float(input("Enter your x of vertics D :"))
y4= float(input("Enter your y of vertics D :")) 
AB = distance(x1, y1, x2, y2)
BC = distance(x2, y2, x3, y3)
CD = distance(x3, y3, x4, y4)
DA = distance(x4, y4, x1, y1)
AC = distance(x1, y1, x3, y3)
BD = distance(x2, y2, x4, y4)
mx1 = mid(x1,x3)
my1 = mid(y1,y3)
mx2 = mid(x2,y4)
my2 = mid(y2,y4)
if AB == CD and BC == DA and AB == BC and AC == BD:
	print("ABCD is a Squre")
elif AB ==CD and BC == DA and AC== BD:
	print("ABCD is a Rectuangle")
elif AB == BC== CD==DA and AC != BD:
	print("ABCD is a Rhombus")
elif AB*CD + BC*DA == AC*BD:
	print("ABCD is a Cyclic Quadilater")
elif AB == CD and BC == DA and AC != BD and AB != BC and mx1== mx2 and my1 == my2 :
	print("ABCD is a Parellogram")
else:
	print("This is a normal quardilater")
