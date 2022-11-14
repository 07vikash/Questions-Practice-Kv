"""Q1-->Write a Python program which will accept old salary of employee.
        Give 20% hike to the all the employees display the salary List?"""
'# map() question'
def hike(sal):
    sal=sal+sal*(20/100)
    return sal
print("enter value with space")
oldsallist=[ float(val) for val in input().split() if float(val)>0]
m=map(hike,oldsallist)
newsallist=list(m)
print("\nOld Sal List=",oldsallist)
print("\nNew Sal list=",newsallist)
