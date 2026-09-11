n_motors = int(input("how many motors are carrying the packages? "))
n_kg = int(input("how many kilograms are the packages? "))
if n_kg/n_motors<=12:
    print("The motors can carry the packages.")
else:
    print("The motors cannot carry the packages.")
    
