def checkx():
    email = raw_input('Enter the email:')
    if '@' in email and '.' in email:
        pass1()
    else :
        print ('Check you email')
        checkx()

def pass1():
    password = raw_input('Enter the password ')
    special = '!@#$%^&*()?'
    if len(password) >= 8 and not password.islower() and not password.isupper() and not password.isalpha() and not password.isdigit() and any((c in special) for c in password):
        print ('Strong Password')
        return 1
    else:
        print ('Weak Password')	
	pass1()

checkx()
