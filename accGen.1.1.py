#get user email address
email = input("What is your email address:? ").strip()

#get pet name
petname = input("What is your pets name:? ").strip()

#get birth year
birthyear = input("When was you born:? ").strip()

#get city
city = input("What city was you born in:? ").strip()

#get colour
colour = input("What is your favourite colour:? ").strip()

#get age
age = input("What is your age:? ").strip()

#get firstname
firstname = input("What is your first name:? ").strip()

#get lastname
secondname = input("What is your second name:? ").strip()

#slice our user name
user = email[email.index(""):email.index("@")]

#slice out domain name
domain = email[email.index("@")+1::1]

#format message
message = """Username:{}
Domain:{}"""
passwordmessage = """Possible passwords:
pass1 - {}{}
pass2 - {}{}
pass3 - {}{}
pass4 - {}{}
Pass5 - {}{}"""

#display output message
output = message.format(user,domain)
print(output)
passwordoutput = passwordmessage.format(petname,birthyear,city,birthyear,colour,age,secondname,birthyear,firstname,city)
print(passwordoutput)
