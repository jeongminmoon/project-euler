a = 600851475143
b = 3

while b < a:
    if a % b == 0:
        a = a / b
    else :
        b = b+2

print a
