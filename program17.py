##TRoy
##Name of Program

fname = raw_input("What is your first name ? ")
lname = raw_input("What is your last name? ")
age = input("How old are you? ")


print "Hello " + fname + " " + lname + " you are " + str(age) + " years old."

if age == 18:
    print "You are just old enough to vote"
elif age >18 and age <= 80:
     print "You are old enough to vote"
elif age > 80:
    print "You are too old to vote"
elif age > 0:
    print "You are not old enough to vote"
else:
    print "Invalid Input"
    
