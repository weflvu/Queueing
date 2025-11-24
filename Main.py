#IS362
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
        choice = int(input("Enter your choice: "))

        if choice == 1:



        elif choice == 2:
            k=int(input("Enter number of servers :"))


        elif choice == 3:



        elif choice == 4:
            print("exit ")
            break

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
main_menu()
