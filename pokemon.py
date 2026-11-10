pokemon = [{
    "nome" : "pikachu",
    "tipo" : "elétrico",
    "nivel" : "25",
    "hp": "100",
    }
    ]

# print("Dados do pókemon:")
# print(pokemon)
#print(f"Nome:", pokemon['nome'])
while True:
    nome = input("Qual o nome do seu pokémon?")
    tipo = input("Qual o tipo do seu pokémon?")
    nivel = int(input("Qual o nível do seu pokémon?"))
    hp = int(input("Quantos de vida tem o seu pokémon?"))
    
    novo_pokemon = {
        "nome": nome,
        "tipo": tipo,
        "nivel": nivel,
        "hp": hp
    }
    pokemon.append(novo_pokemon)
    print(novo_pokemon)
    print(f"{nome} adicionado com sucesso.")


    continuar = input("Continuar? Se sim, aperte S:")
    continuar.lower
    if continuar != "s":
        break

print(pokemon)

