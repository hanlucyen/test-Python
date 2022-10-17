import os
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join ( mame, name)
        if os.path.isfile (path):
            print (path)
        else:
            walk (path)

fout=open('hello.py')
print(os.path.abspath('hello.py'))
print(walk(python))
