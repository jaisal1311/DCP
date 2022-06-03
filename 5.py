
# fn to return f as pair that is fn() itself
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# fn takes pair as param and return car(pair) that is first value of (a,b)
def car(pair):
    def return_car(a, b):
        return a
    return pair(return_car)
    
# fn takes pair as param and return cdr(pair) that is last value of (a,b)
def cdr(pair):
    def return_cdr(a, b):
        return b
    return pair(return_cdr)
    
    
print(car(cons(3, 4)))
