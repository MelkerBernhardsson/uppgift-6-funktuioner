def mathmatic(tal1,tal2,tal3):
    if tal3 == "+":
        tal4=tal1+tal2
        print(tal1,tal3,tal2,"=", tal4)
    elif tal3 == "-":
        tal4=tal1-tal2
        print(tal1,tal3,tal2,"=", tal4)
    elif tal3 == "*":
        tal4=tal1*tal2
        print(tal1,tal3,tal2,"=", tal4)
    elif tal3 == "/":
        tal4=tal1/tal2
        print(tal1,tal3,tal2,"=", tal4)


a=int(input("vad ar ditt forsta varde? "))
b=int(input("vad ar ditt andra varde? "))
c=input("vad ar ditt raknesatt?")

mathmatic(a,b,c)