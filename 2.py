a=0
b=1
total=0
result=0
while result < 4000000:
    result = a+b
    a=b
    b=result
    if result%2==0:
        total = total + result

print total
