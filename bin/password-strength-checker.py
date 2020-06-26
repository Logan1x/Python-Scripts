import string

def checkx():
    pass
    email = input('Enter the email:')
    if '@' in email and '.' in email:
        pass1()
    else:
        print('Check you email')
        checkx()


def pass1():
    invalidcharacters=set(string.punctuation)
    while True:
        password = input('Enter the password of atleast 10 characters length \n  ')
        if len(password) < 10 :
            print(" your password is less than 10 characters")
        
        if len(password)>= 10 :
            if (any(x.isdigit() for x in password)) and (any(x.islower() for x in password)) and any(char in invalidcharacters for char in password) and (any(x.isupper() for x in password)) :
                print('Good! You have created a strong password ')
                break
            else:
                print("Please enter Atleast, an upper case , lowercase , special character !@#$%^&*()? and digit")
            
            
            
               

if __name__== '__main__':
    checkx()
