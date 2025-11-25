#IS324
import math

def mm1(lam,mu):
    Wq = lam/(mu*(mu-lam))
    return Wq

def mg1_queue(lam, mu):
    sigma2 = float(input("Enter service time variance σ²: "))
    sigma = sigma2 ** 0.5
    Wq = ((lam * sigma)**2 + (lam / mu)**2) / (2 * lam * (1 - lam / mu))
    return Wq

def my_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def mmk(lam, mu, k):
    a = lam / mu
    rho = lam / (k * mu)
    sum_terms = 0
    for n in range(k):
        sum_terms += (a ** n) / my_factorial(n)
    last_term = (a ** k) / (my_factorial(k) * (1 - rho))
    P0 = 1 / (sum_terms + last_term)
    numerator = (a ** k) * mu
    denominator = my_factorial(k - 1) * ((k * mu) - lam) ** 2
    Wq2 = (numerator / denominator) * P0
    return Wq2

def main_menu():
    while (True):
        lam = int(input("Enter arrival rate: "))
        mu = int(input("Enter Service rate: "))

        if lam <= 0:
            print("Error , lambda must be greater than 0.")
            return

        print("*****************")
        print("****Queueing System Calculator ****")
        print("1- M/M/1 System ")
        print("2- M/M/k System ")
        print("3- M/G/1 System ")
        print("4- Exit")
        print("*****************")

        try :
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice you must choose a number from 1-4")
            continue

        if choice == 1:
          if mu <= lam:
             print("error, mu must be greater than lambda, the system isn't steady")
             return
          Wq=mm1(lam,mu)
          print(f"M/M/1 Wating Time Wq: {Wq:.4f}\n")

        elif choice == 2:
            k=int(input("enter number of servers :"))
            if k <= 0:
                print("error,Number of servers k must be positive.")
                return
            if lam>=k*mu:
                print("error, mu*k must be greater than lambda, the system isn't steady")
                continue
            Wq=mmk(lam,mu,k)
            print(f"M/M/K Wating Time Wq : {Wq:.4f}\n")

        elif choice == 3:
            if mu <= lam:
                print("error, mu must be greater than lambda, the system isn't steady")
                return
            Wq=mg1_queue(lam,mu)
            print(f"M/G/1 Wating Time Wq : {Wq:.4f}\n")

        elif choice == 4:
            print("exit")
            break
        else:
            print("Invalid choice you must choose a number from 1-4")
main_menu()
