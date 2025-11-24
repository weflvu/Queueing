#IS362
import math
lam = int(input("Enter arrival rate: "))
mu = int(input("Enter Service rate: "))

#m/m/1
def mm1():
    # Wq = λ/μ(μ-λ)
    Wq = lam/mu(mu-lam)

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
    
#----------------------------------
    #m/m/k
    def my_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def mmk(lambda_rate, mu_rate, k):
    # VALIDATION
    if lambda_rate <= 0:
        print("Error: λ must be greater than 0.")
        return

    if mu_rate <= lambda_rate:
        print("Error: μ must be greater than λ.")
        return

    if k <= 0:
        print("Error: Number of servers k must be positive.")
        return

    if lambda_rate >= k * mu_rate:
        print("Error: System is unstable because λ ≥ kμ.")
        return

    a = lambda_rate / mu_rate
    rho = lambda_rate / (k * mu_rate)

    sum_terms = 0
    for n in range(k):
        sum_terms += (a ** n) / my_factorial(n)

    last_term = (a ** k) / (my_factorial(k) * (1 - rho))
    P0 = 1 / (sum_terms + last_term)

    numerator = (a ** k) * mu_rate
    denominator = my_factorial(k - 1) * ((k * mu_rate) - lambda_rate) ** 2
    Wq2 = (numerator / denominator) * P0

    print("\n--- Results for M/M/k ---")
    print(f"Wq (Waiting time in queue) = {Wq2:.4f}")
# ---------------------------
#m/g/1
def mg1_queue(lam, mu):
    # σ² input
    sigma2 = float(input("Enter service time variance σ²: "))
    sigma = sigma2 ** 0.5

    # Wq = [ (λσ)^2 + (λ/μ)^2 ] / [ 2λ(1 - λ/μ) ]
    Wq = ((lam * sigma)**2 + (lam / mu)**2) / (2 * lam * (1 - lam / mu))

    print(f"\nWq (Waiting time in queue) = {Wq:.4f}")
#----------------------------------
    
def main_menu():
    while (True):
        print("*****************")
        print("****Queueing System Calculator ****")
        print("1- M/M/1 System ")
        print("2- M/M/k System ")
        print("3- M/G/1 System ")
        print("4- Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:



        elif choice == 2:
            k=int(input("Enter number of servers :"))


        elif choice == 3:



        elif choice == 4:
            print("exit ")
            break


main_menu()
