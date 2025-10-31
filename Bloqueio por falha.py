entrada = input().strip()

# Separa corretamente pelas vírgulas
tentativas = [item.strip().lower() for item in entrada.split(",")]

falhas = 0

for t in tentativas:
    if t == "falha":
        falhas += 1
        if falhas >= 3:
            print("Conta Bloqueada")
            break
    else:
        falhas = 0
else:
    print("Acesso Normal")
