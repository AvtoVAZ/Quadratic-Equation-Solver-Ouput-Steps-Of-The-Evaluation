import math

alpha_srt = input("What is the value of alpha: ")
alpha = int(alpha_srt)
beta_str = input("Whats is the value of beta: ")
beta = int(beta_str)
gamma_str = input("What is the value of gamma: ")
gamma = int(gamma_str)
diakrinousa = (beta)*(beta)-(4*(alpha)*(gamma))

if diakrinousa < 0:
    print("False because D < 0")
else:
    print("Δ  = ",diakrinousa)
    sqrt_of_diakrinousa = math.sqrt(diakrinousa)
    print("√Δ = ",sqrt_of_diakrinousa)
    x = (-(beta)) / 2 * (alpha)
    if diakrinousa == 0:
        print("x  = ", x)
    x1_bigger0 = (-(beta) + math.sqrt(diakrinousa)) / (2 * (alpha))
    x2_bigger0 = (-(beta) - math.sqrt(diakrinousa)) / (2 * (alpha))
    if diakrinousa > 0:
        print("x1 = ", x1_bigger0)
        print("x2 = ", x2_bigger0)
#Made by Avtovaz
#My GitHub: https://github.com/AvtoVAZ


