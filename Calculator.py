def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
n1=float(input("first num: "))
op=input("pick operation: " \
"\n+" \
"\n-" \
"\n*" \
"\n/\n")
n2=float(input("next num: "))
result=dict.get(op)(n1,n2)
print(f"Result: {result}")
ke=input("Type y to continue with this num or e to exit: ")
while ke=="y":
    op=input("pick operation: " \
    "\n+" \
    "\n-" \
    "\n*" \
    "\n/\n")
    n2=float(input("next num: "))
    result=dict.get(op)(result,n2)
    print(f"Result: {result}")
    ke=input("Type y to continue with this num or e to exit: ")
