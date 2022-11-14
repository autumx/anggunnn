print("BODY MASS INDEX")
weight = float(input("Weight :"))
height = float(input("Height :"))
m = 100
bmi = (weight/(height/m)**2)
print(bmi)
if bmi < 18.5 :
    print("Underwight")
if 18.5 < bmi < 24.9 :
    print("Normal Weight")
if 25 < bmi < 29.9 :
    print("Overweight")
if 30 < bmi < 34.9 :
    print("Obesity class I")
if 35 < bmi < 39.9 :
    print("Obesity Class II")
if bmi > 40 :
    print("Obesity Class III") 