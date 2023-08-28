Daliy=float(input("daliy payment-"))
Weekly=float(input("weekly payment-"))
Monthly=float(input("Monthly payment-"))
Half_Monthly=float(input("Half Monthly Payment-"))
Days=(Daliy+Weekly+Monthly+Half_Monthly)
Payment=(Daliy+Weekly+Monthly)/3
if Monthly>=20 and Monthly<=30:
    print("Full Payment")
    print("Sallary 15000tk")
elif Half_Monthly>=10 and Half_Monthly<=15:
    print("Half Monthly payment")
    print("Sallary 7500tk")
elif Weekly>=3 and Weekly<=10:
    print("Weeekly Payment")
    print("Sallary 5000tk")
elif Daliy>=1 and Daliy<=3:
    print("Dailly Payment")
    print("Sallary 500tk")
else:
    print(Days)
    print(Payment)