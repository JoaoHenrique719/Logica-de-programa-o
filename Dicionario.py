meu_dicionario = {"nome":["João", "Ana"],
                  "idade":[19, 28],
                  "cidade":["Goiânia", "São Paulo"],
                  "profissao":["Ti","professora"],
                  "salario":[2300, 2200],
                  "cpf":["10000000012", "10000000034"]}

cpf_consultar = input("Informe o CPF do cliente:")

if cpf_consultar in meu_dicionario ["cpf"]:
    print(f"Cliente cadastrado.")
    
    indice = meu_dicionario["cpf"].index(cpf_consultar)
    
    for chave in meu_dicionario.keys():
        print(f"{meu_dicionario[chave][indice]}")
    
else:
    print("Cliente não cadastrado.")


