#  BMI CALCULATOR


Weight= float(input ("enter your weight\t"))
Height=float(input ("enter your height in metres\t"))

print ('\n')

BMI=(Weight/(Height **2),) #weight in kg 
                           # height in metre
print ('\n')

for e in BMI:
    if e<18.5:
        print (" you are underweight")
        
    elif 18.5<=e<=24.9:
        print (" you are fit ")
     
    elif e >=25 and e<=29.9:
        print ("you are overweight")
     
    else :
        print (" you are obese ")
    

else:
 print ('\n\n')  
 print   ( "Be fit and live a healthy life")