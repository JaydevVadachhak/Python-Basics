def food(f):
    tip = 0.1*f
    f=f+tip
    fperson = f/num
    return fperson

def movie(m):
    return m/num

num = int(input("no of friends:"))
ftotal=float(input("food bill total:"))
mtotal=float(input("movie bill total:"))

x=food(ftotal)
y=movie(mtotal)


print("per person total is:",x+y)
