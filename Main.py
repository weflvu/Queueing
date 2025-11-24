#IS324
import math
lam = int(input("Enter arrival rate: "))
mu = int(input("Enter Service rate: "))

def main_menu():
    while (True):
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
            print("Invalid choice")
            continue
        if lam>mu:
            print("Invalid lambda must be less than mu system not stedy")
            continue
        if choice == 1:
          Wq=mm1(lam,mu)
          print(f"M/M/1 Wating Time Wq: {Wq:.4f}\n")

        elif choice == 2:
            k=int(input("Enter number of servers :"))

            if lam>k*mu:
                print("Invalid lambda must be less than k*mu system not stedy")
                continue
                Wq=mmk(lam,mu,k)
                print(f"M/M/K Wating Time Wq : {Wq:.4f}\n")

        elif choice == 3:
            Wq=mg1_queue(lam,mu)
            print(f"M/G/1 Wating Time Wq : {Wq:.4f}\n")
        elif choice == 4:
            print("exit")
            break

def mm1(lam,mu):
    # Wq = λ/μ(μ-λ)
    Wq = lam/(mu*(mu-lam))

    # Output
    print("\n--- Results for M/M/1 ---")
    print(f"Wq (Waiting time in queue) = {Wq:.4f}")



def mg1_queue(lam, mu):
    # σ² input
    sigma2 = float(input("Enter service time variance σ²: "))
    sigma = sigma2 ** 0.5

    # Wq = [ (λσ)^2 + (λ/μ)^2 ] / [ 2λ(1 - λ/μ) ]
    Wq = ((lam * sigma)**2 + (lam / mu)**2) / (2 * lam * (1 - lam / mu))

    print(f"\nWq (Waiting time in queue) = {Wq:.4f}")

 #m/m/k
def my_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def mmk(lam, mu, k):
    # VALIDATION
    if lam <= 0:
        print("Error: λ must be greater than 0.")
        return

    if mu <= lam:
        print("Error: μ must be greater than λ.")
        return

    if k <= 0:
        print("Error: Number of servers k must be positive.")
        return

    if lam >= k * mu:
        print("Error: System is unstable because λ ≥ kμ.")
        return

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

    print("\n--- Results for M/M/k ---")
    print(f"Wq (Waiting time in queue) = {Wq2:.4f}")
main_menu()
