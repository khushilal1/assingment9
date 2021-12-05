# Global and Local Variables
# local variablrs  are thosew variable which is define locally
# chnaging the global variable from from the local plac eby using the global keyword
# global keyword

def f():
    global s
    print(s)
    s=s+"i am mohan"
    print(s)
s="hello guys"
f()
print(s)


def k():
    global s  #use oof the global keyword 
    s=s+" and javascript"
    print(s)
s="i love python"
k()
print(s)

#Using global and local variables
a = 1
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():

    a = 2
print('Inside g() : ', a)
# Uses global keyword to modify global 'a'
def h():
    global a
a = 3
print('Inside h() : ', a)

# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
