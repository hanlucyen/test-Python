print("enter password ")
print("Create password at least 8 characters long")
import string
import random
"""
#đây là password 1 kí tự được trả về
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
COMBINED_LIST = DIGITS + UPPERCASE + LOWERCASE + SPECIAL
password = "".join(random.sample(COMBINED_LIST,8))
password=random.choice(COMBINED_LIST)
print("This is your password : %s" % password)
print(password)
"""
LETTERS=string.ascii_letters
#print(LETTERS)
NUMBERS=string.digits
#print(NUMBERS)
PUNCTUATION=string.punctuation
#print(PUNCTUATION)
print("Make sure your password has at least one uppercase character, one lowercase letter, one special character, and one number.")
print("your password: ")
v=input()
print("your password: " ,v)

def passWord_Generator(length=8,chu=False,so=False,ky_tu=False):#tạo 1 hàm chứa độ dài ít nhất là 8 
    
    chuoi=None
    if chu and so and ky_tu:
        chuoi=''.join([LETTERS,NUMBERS,PUNCTUATION])
    elif(chu==True) and (so==True):
        chuoi=''.join([_LETTERS_,NUMBERS_])
        
    elif (chu==True) and (ky_tu==True):
        chuoi=''.join([_LETTERS_,PUNCTUATION_])
        
    elif (so==True) and (ky_tu==True):
        chuoi=''.join([_NUMBERS_,PUNCTUATION_])
    elif chu:
        chuoi=''.join(LETTERS)
    elif so:
        chuoi=''.join([NUMBERS])
    elif ky_tu:
        chuoi=f'{PUNCTUATION}'
    else:
        chuoi=''.join([LETTERS,NUMBERS,PUNCTUATION])
        
    chuoi=list(chuoi)
    
    random.shuffle(chuoi)#hàm sáo trộn
    random_password=random.choices(chuoi, k=8)#máy trả về ngẫu nhiên , k là số kí tự máy trả về cho password ngẫu nhiên 
    random_password=''.join(random_password)#kết nối các kí tự chung của password

    return random_password
    
   
    
print("Computer password: ",passWord_Generator())
               
