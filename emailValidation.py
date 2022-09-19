print("Welcome to Email Validation Program")
k=0
j=0
d=0
emale = input("Enter Email : ")
if len(emale)>=6:
    if emale[0].isalpha():
        if ("@" in emale) and (emale.count("@")==1):
            if (emale[-4]==".") ^ (emale[-3]=="."):
                for i in emale:
                    if i==i.isspace():
                        k=1
                    elif (i.isalpha()):
                        if i==i.upper():
                            j=1
                    elif (i.isdigit()):
                        continue
                    elif (i=="_") or (i==".") or (i=="@"):
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Space Detected - Wrong Email")
            else:
                print("Invalid Email")
        else:
            print("Wrong Email 3")
    else:
            print("Wrong email 2")
else:
    print("Wrong Email 1")