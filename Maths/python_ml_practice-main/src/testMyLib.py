import MyLib as ml

basic = int(input("Enter the basic:"))
salary = basic + ml.CalDa(basic) + ml.CalHra(basic) + ml.CalIncrement(basic, ml.CalDa(basic))

print("New salary with Increment is ", salary)