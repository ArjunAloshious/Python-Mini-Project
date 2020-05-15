#_______________________________________________________________________________

#-----------------------------CALORIE TRACKER PROGRAM---------------------------
#_______________________________________________________________________________

print ("\n\n")
print ("\t\t\t\t\t\t\t\tHELLO !!!")
print ("\t\t\t\tWELCOME TO OUR CALORIE TRACKER PROGRAM...")
print ("\tWE PROVIDE YOU WITH INFO ON YOUR CALORIE BURN AFTER A GREAT WORKOUT!")
print ("\n")
#READING ALL VALUES

x=float(input("Enter your mass in kgs : "))
y=float(input("Enter your height in metres : "))
age=float(input("Enter your age : "))
gen=input("Enter your gender : ")


# CALCULATING THE BODY MASS INDEX RATIO

bmi=(x)/(y * y)
bm=float(bmi)
print ("\n")


if bm<18.5:
   print ("You are : Underweight")
elif bm>=18.5 and bm<=24.9:
   print ("You are Healthy")
elif bm>=24.9 and bm<=29.9:
   print ("You are : Overweight")
   print ("You need to work out more and lose weight")
   f=1
elif bm>=30:
   print ("You are : Overweight")
   print ("You need to work out more and lose weight")
   f=2
else:
   print ("Invalid Values Entered !")


# FOR PEOPLE WHO ARE OVERWEIGHT :-

if f==1 or f==2:
   print ("\n")
   if gen=="m" or gen=="M":
      b=float(input("Enter the number of minutes spent on treadmill : "))
      c=float(input("Enter your average heart rate during this : "))
      treadmill=(((age*0.02017)-(x*0.09036)+(c*.6309)-(55.0969))*b)/4.184
      d=float(input("Enter the number of minutes spent on elliptical : "))
      g=float(input("Enter your average heart rate during this : "))
      elliptical=(((age*0.02017)-(x*0.09036)+(g*0.06309)-(55.0969))*d)/4.184
      o=treadmill+elliptical
      print ("Total no. of calories burnt = ",o)

   if gen=="f" or gen=="f":
      b=float(input("Enter the number of minutes spent on treadmill : "))
      c=float(input("Enter your average heart rate during this : "))
      treadmill=(((age*0.074)-(x*0.05742)+(c*0.4722)-(20.4022))*b)/4.184
      d=float(input("Enter the number of minutes spent on elliptical : "))
      g=float(input("Enter your average heart rate during this : "))
      elliptical=(((age*0.074)-(x*0.05742)+(d*0.4722)-(20.4022))*c)/4.184
      o=treadmill+elliptical
      print ("Total no. of calories burnt = ",o)
 
print ("\n\n","\t\tThank You And Have A Healthy Day Ahead !!!")

#________________________________THE END________________________________________
#_______________________________________________________________________________