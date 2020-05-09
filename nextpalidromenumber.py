cases = int(input("no of test cases: "))
case =0;
while(case < cases):
    num =  int(input("enter a number"))
    while True :
        if(str(num) == str(num)[::-1]):
            print(num)
            break
        num += 1
    case += 1



