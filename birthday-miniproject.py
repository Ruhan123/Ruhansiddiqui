dict ={}
while True:
    print("------Happy birthday-----")
    print("1.show birthday detail")
    print("2, Added birthdat list")
    print("3.exit")
    choice=int(input("enter choice"))
    if choice==1:
        if len(dict.keys())==0:
            print(" nothing show detail")
        else:
             name=input("enter name to show for birthday")
             birthday=dict.get(name,"not found")
             print(birthday)
    elif choice==2:
        name=input("enter name")
        date=input("enter birth date")
        dict[name]=date
    elif choice==3:
        break
    else:
        print("choose valid option")
