canditates = {1: "Ana", 2: "Bruno", 3: "Carla"}
votes = {1: 0, 2: 0, 3: 0}
invalidVotes = 0
totalVotes = 0
vencedor = []

while (True):
    canditate = int(input("Insira o código do candidato: "))
    vote = int(input("Insira os votos do candidato: "))

    if (vote == 0):
        break

    if (canditate not in canditates.keys()): 
        print("Candidato inválido")
        invalidVotes += vote
        continue
    
    if (vote < 0):
        print("Votos inválidos")
        invalidVotes += vote
        continue
    
    votes[canditate] += vote
    totalVotes += vote

for key, vote in votes.items():

    if (not vencedor):
        vencedor.append(key)
        continue

    if (vote > votes[vencedor[0]]):
        vencedor.clear()
        vencedor.append(key)
        continue

    if (vote == votes[vencedor[0]]):
        vencedor.append(key)

print("\n")
for key, canditate in canditates.items():
    vote = votes[key]
    print(f"O(a) candidato(a) {canditate} de código {key} teve {vote} votos e porcentagem de {round((vote / totalVotes), 2) * 100}%")

if (len(vencedor) != 1):
    print("\nOcorreu empate entre os candidatos: ")
    for i in vencedor:
        print(f"{canditates[i]} : {votes[i]} votos")
else: 
    print(f"\nO vencedor foi {canditates[vencedor[0]]} com {votes[vencedor[0]]} votos")

print(f"\nTiveram {invalidVotes} votos inválidos na eleição")