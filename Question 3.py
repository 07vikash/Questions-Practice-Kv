"""Q3==> Write a Python Program which will accept list of numericals
         and Obtain their Squares and square roots"""
'''Using map() and anonymous functions lambda'''
print("Enter list values with separated by space:")
oldvals=[int(val) for val in input().split()]
print("Given Values=",oldvals)
sqrvals=list(map(lambda val:val**2,oldvals))
d1=dict(zip(oldvals,sqrvals))
sqrtval=list(map(lambda val:val**0.5,oldvals))
d2=dict(zip(oldvals,sqrtval))
print("Square Values:")
for v,k in d1.items():
    print("\t{}-->{}".format(v,k))
print("-"*50)
print("Square root value")
for v,k in d2.items():
    print("\t{}-->{}".format(v,round(k,2)))
print("="*50)