# Lendo o número de casos de teste
N = int(input(10))

# Processando cada caso de teste
for _ in range(N):
    # Lendo os valores A e B
    A, B = input().split()

    # Verificando se B corresponde aos últimos dígitos de A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")
    
    print(A, B)