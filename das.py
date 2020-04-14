"""
	date:2020.04.13
	author:Derec_Lee
"""
print ('Hello World!')

a = 1.3
print (a)
print (type(a),'hard,max')

s1 = ('SAD',1.3,False,4)#tuple enum can't change
s2 = [1.4,4,True]#list enum can be changed
print(s1[0])
print(s2[2])
print(s1[0:4:2])#start:end:jump paramater
str = 'abcdefg'
print(str[3:5])#String is a kind of tuple

b = (((1+8-1)*2/4)**2)%3
print (b)#+,-,*,/,**,%;==.!=,>,>=,<,<=,in;and,or,not

i = 1
if i > 0:
	print('positive i')
	i = i + 1
elif  i == 0:
	print('i is 0')
	i = i *10
else:
	print('negative i')
	i = i - 1
print('new i:',i) 

for c in s1:
	print(c)

for a in range(20):#range() is a list of 0 to n-1
	print(a**3)

for i in range(20):
	if i==3:
		continue
	print(i)
	if i==18:
		break

t = 0
while t<10:
	print(t)
	t = t+1

def yearSelect(n):
	if (n%4==0 and n%100!=0) or n%400==0:
		return True
	else:
		return False

print(yearSelect(2008))

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print ('after move:',summer.move(5,8))

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print (summer.have_feather)
print (summer.move(5,8))

class Human(object):
	def __init__(self,input):#two _ _ _ _
		print("start")
		# self.laugh_100th()
		self.gender = input
	laugh = 'hahahaha'
	def show_laugh(self):
		print(self.laugh)
	def laugh_100th(self):
		for i in range(100):
			self.show_laugh()
	def printGender(self):
		print(self.gender)
thingsada = Human('7777777')
thingsada.printGender()#object paramater not class paramater

# print(dir(thingsada))
# print(help(thingsada))

print(dir(list))
print(help(list))		
		

