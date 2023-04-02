def tapi(n):
    print("+" + ("-"* (n-1))+ "+")
    for i in range(n, -1, -1):
        for j in range(n+1):
            if i == j:
                print("+", end = "")
            else:
                print("#", end="")      
        print()
    print("+" + ("-"* (n-1))+ "+")  

tapi(10)




"""def afficher_tapis_diagonal(n):
    for i in range(n, -1, -1):
        for j in range(n+1):
            if i == j:
                print("+", end="-")
            else:
                print("#", end="+")
        print()
afficher_tapis_diagonal(20)"""