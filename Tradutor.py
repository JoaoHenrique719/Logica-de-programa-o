tradutor = {
    "cadeira" : "chair",
    "cachorro" : "dog",
    "gato" : "cat",
    "amor" : "love",
    "perdido": "lost"
}
print("Bem-vindo ao dicionário da EFG.")

while True:

    print("1.para traduzir uma palavra.")
    print("2.Cadastrar uma palavra.")
    print("0.Sair do programa.")
    opcao = int(input(""))

    if opcao == 1:
        palavra_busca = input("Digite uma palavra que deseja saber a tradução:")

        for palavra in tradutor:

            if palavra_busca.lower() == palavra.lower():
                print(f"A tradução da palavra é:{tradutor[palavra]}")
    elif opcao == 2:
        palavra_cadastro = input("Digite a palavra em pôrtugues para cadastrar:")
        palavra_cadastro.lower

        if not palavra_cadastro in tradutor:
            traducao_cadastro = input("Qual a tradução para inglês:")
            traducao_cadastro.lower
            tradutor[palavra_cadastro] = traducao_cadastro
            print("Palavra cadastrada com sucesso.")
            

    elif opcao == 0:
        print("Programa encerrando.")
        break

    else:
        print("Coloque uma opção válida.")
