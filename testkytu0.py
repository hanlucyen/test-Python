
def any_lowercase1(s):
    for c in s:
        
        if c.islower():
            return True
        else:
            return False
print(any_lowercase1("ANNA"))

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
print(any_lowercase2("wfeq"))

def any_lowercase3(s):
    for c in s:
        flag=c.islower()
        return flag
print(any_lowercase3("anNA"))

def any_lowercase4(s):
    flag= False
    for c in s:
        flag=flag or c.islower()
    return flag
print(any_lowercase4("bNNNNNN"))

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True
print(any_lowercase5("aNnna"))
