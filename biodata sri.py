
# This My Biodata perform By Python Programing language

#input biodata
from unicodedata import name


Name = input("Enter your name       : ")
Class = input("Enter your class     : ")
Major = input("Enter your study program : ")
Age = int (input("Enter your age         : "))
#create hobbies variable first
Hobbies = ["[0]","[1]","[2] "]
Hobbies[0] = input( "what is your first hobby? : ")
Hobbies[1] = input("what your is second hobby? : " )
Hobbies[2] = input("what your third hobby?       :  ")

Food = bool (input("what  mie ayam your favorit food ? Type y for yes, Leave Blank for No  : "))
Motto = input("what your quote       : ")

#display
print("Name : " ,Name)
print("Class : ", Class)
print("Study program : ", Major)
print("Age; ", Age)
print(" Hobbies : " , Hobbies)
print("Food : ",Food)
print("Motto : ", Motto)

print('nama type is : ',type(Name))
print('class type is: ',type(Class))
print('major type is : ',type(Major))
print('age type is : ',type (Age))
print( 'hobbies type is : ',type(Hobbies))
print('food type is : ',type(Food))
print('motto type is : ',type(Motto))