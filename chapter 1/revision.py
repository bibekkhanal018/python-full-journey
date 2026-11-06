#variable and operators 
a=int(1)
b=3
print (a+b)


#string slicing in python
name = 'name is bibek'
ch=name[1]
c=name[1:14]
d=name[-14:-1]
print (c)
print (ch)
print (d)

# skipping in string slicing in python
print (name[1:7:2])

#some strings functions
s='bibek'
f='bibek khanal'
print (s.endswith('bek'))
print (s.startswith('bib'))
print (f.count('k'))
print (f.capitalize())
print (f.find('khanal'))
print (f.title())
replaced_strings=f.replace('khanal','rijal')
print (replaced_strings)

#escape sequence like \n , \t , \;\\
a='bibek is a bad \n boy not \n a \n bad \t one \'hey\' '
print (a)


letter='''dear name,
you are selected!
date
'''
print (letter.replace('name','bibek').replace('date','2057 02 23')) #strings are immutable

#list and its functions
friends = ['apple',1,'bibek','5']
print (friends[0])  #lists are mutable
print (friends[0:3])  
friends.append('khanal') #it appends khanal at the end of the list 'friends'
print (friends)


l1=[1,3,5,8,32,2,7,41]
l1.sort() #it sorts the list of numbers
print (l1)
l1.reverse() #it reverses the list items
print (l1)