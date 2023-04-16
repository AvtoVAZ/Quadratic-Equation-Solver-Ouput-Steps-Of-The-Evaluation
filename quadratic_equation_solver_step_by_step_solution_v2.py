# Importing the library
import math
# Asking the user the value of Alpha
a = int(input("What is the value of a [a*(x**2)]: "))
# Asking the user the value of Beta
b = int(input("Whats is the value of b [b*x]: "))
# Asking the user the value of Gamma
c = int(input("What is the value of c [c]: "))
print("===================================================")
print("a = ",a)
print("b = ",b)
print("g = ",c)
print("===================================================")
# Calculating the value of the Discriminant by separating the equation into separate parts
# It is separated so the output can print each step of the calculating process
discriminant1 = ((b)**2)
discriminant2 = ((a) * (c))
discriminant3 = (4 * (discriminant2))
discriminant4 = ((discriminant1) - (discriminant3))
# Printing the output of Δ into different parts of the calculation
print("Δ  = (",b,")^2 - 4 * (",a,") * (",c,")")
print("Δ  = (",(discriminant1),") - 4 * (",(discriminant2),")")
print("Δ  = (",(discriminant1),") - (",discriminant3,")")
print("Δ  = ",discriminant4)
print("===================================================")
# Setting the basic rules for the procedure of the calculation of the values of x1/2 using the value of the discriminant
if discriminant4 < 0:
    # If the value of the Discriminant is smaller than 0 (Δ < 0) the process of calculating the equation cannot be continued
    print("The equation cannot be solved because Δ < 0. No possible roots.")
    print("===================================================")
# If the value of Δ is greater or equal to 0 (Δ ≥ 0) the process of calculating the equation can be continued
else:
    # Calculating the square root of Δ
    sqrt_of_discriminant4 = math.sqrt(discriminant4)
    # Printing the square root of √Δ
    print("√Δ = ",sqrt_of_discriminant4)
    print("===================================================")
    # If the Discriminant is greater than 0 the evaluation of x1,x2 will be proceeded
    if discriminant4 > 0:
        # Separating the equation of x1 into different parts
        # The value of x1 is also being calculated
        x1_arithmitis1 = ((-(b)) + (math.sqrt(discriminant4)))
        x1_paronomastis1 = ((a) * 2)
        x1_apotelesma1 = ((x1_arithmitis1) / (x1_paronomastis1))
        # Printing the value of x1 and the different parts of the calculation process
        print("x1 = ((-",b,") + √(",discriminant4,")) / (2 * (",a,"))")
        print("x1 = (",x1_arithmitis1,") / (",x1_paronomastis1,")")
        print("x1 = ",x1_apotelesma1)
        print("===================================================")
        # Separating the equation of x2 into different parts
        # The value of x2 is also being calculated
        x2_arithmitis1 = ((-(b)) - (math.sqrt(discriminant4)))
        x2_paronomastis1 = ((a) * 2)
        x2_apotelesma1 = ((x2_arithmitis1) / (x2_paronomastis1))
        # Printing the value of x2 and the different parts of the calculation process
        print("x2 = ((-",b,") - √(",discriminant4,")) / (2 * (",a,"))")
        print("x2 = (",x2_arithmitis1,") / (",x2_paronomastis1,")")
        print("x2 = ",x2_apotelesma1)
        print("===================================================")
    # If the Discriminant is equal to 0 (Δ = 0) the process of solving the equation will result to only one possible root
    if discriminant4 == 0:
        # Separating the equation of x into different parts
        # The value of x is also being calculated
        x_arithmitis1 = (-(b))
        x_paronomastis1 = (2 * (a))
        x_apotelesma1 = (x_arithmitis1) / (x_paronomastis1)
        # Printing the value of x and the different parts of the calculation process
        print("x  = (-",b,") / (2 * (",a,"))")
        print("x  = (",x_arithmitis1,") / (",x_paronomastis1,")")
        print("x  = ",x_apotelesma1)
        print("===================================================")
# Made by Avtovaz
# My GitHub: https://github.com/AvtoVAZ







