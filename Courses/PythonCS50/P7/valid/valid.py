import validators

email = input("What is your email? ")

# this lbiary enables the checking of email validation insrtead of using regexes
# ie for a regex command re we whouldve needed to use ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
# to validated the correct email were as we just import a library in this case
if validators.email(email):
    print("Valid")
else:
    print("Invalid")