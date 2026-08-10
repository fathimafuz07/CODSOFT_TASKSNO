tasks=[]
print("TO-DO LIST")
while True:
    print("\n1.View 2.Add 3.Delete 4.Exit")
    choice=input("Choose").strip()
    if choice=="1":
        for i,t in enumerate(tasks,1):
            print(i,"-",t)
    elif choice=="2":
        task=input("Enter task:")
        tasks.append(task)
    elif choice=="3":
        num=int(input("Enter task number to delete:"))
        tasks.pop(num-1)
    elif choice=="4":
        break
    else:
        print("invalid choice,try again")
