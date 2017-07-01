password = raw_input('Enter the password ')
special = '!@#$%^&*()?'
if len(password) >= 8 and not password.islower() and not password.isupper() and not password.isalpha() and not password.isdigit() and any((c in special) for c in password):
    print'password is strong'
else:
    print 'Weak Password'
