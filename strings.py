#variables...........................................................


name = 'Hasnat Osman' #single quotes......
info = "I\'m a student.\nBut now I don't study!" #use double quotes instead...
text = """I am Hasnat.
I don't care khaled or whoever he is! """
check ="""\             
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""            #use """..""" to display as it is.....................



#string manipulations................................................


first_name = str.upper(name[0:6]) #character is position..........
last_name = str.upper(name[7:]) # upper case conversion.....






#printing outputs....................................................
print(" >>>>>>>>>>>>>>> Here are some string manipulations!!!")
print()
print("My name is :", name)
print( "Total character is :", len(name))
print("First name is :", first_name)
print("Last name is: ", last_name)


print(info)
print(text)
print()
print(check)
print()












print(3 * "...........SUCCESSFULLY PASSED!!!\n")
