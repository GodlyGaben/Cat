def rl2(s):
    x=s[:2]
    s1=s[2:]
    return s1 + x
print (rl2("Hello"))
print (rl2("java"))
print (rl2("Hi"))
