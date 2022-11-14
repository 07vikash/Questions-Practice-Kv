'''Q2==> Write a python program which will accept the numericals and obtain
         their squares and square roots?'''
"Using normal function and map()"
def sqr(val):
    "This function used for square of value"
    return val**2

def sqrt(val):
    "This function used for root Square"
    return val**(1/2)

print("Enter list value separated by space:")
oldval=[int(val) for val in input().split() if val.isdigit()]
newsqr=list(map(sqr,oldval))
newsqrt=list(map(sqrt,oldval))
print("\nOld Value=",oldval)
print("\nNew Square Value=",newsqr)
print("\nNew Root Square Value=",newsqrt)