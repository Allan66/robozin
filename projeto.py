

print(f"\nBot: Olá usuário, como se chama? ")
nome = str(input(f"\nVocê: "))
if nome == nome:
    print(f"\nBot: É um prazer", nome)
    print(f"\nBot: Qual a sua idade ?")

    idade = int(input(f"\nVocê: "))
if idade <= 17:
    print(f"\nBot:", nome, " Você possui apenas, ",
          idade, "anos, portanto, é menor de idade.")
    print(f"\nBot: Em qual região você reside ?")
    moradia = str(input(f"\nVocê: "))
else:
    print(f"\nBot:", nome, ", você tem", idade,
          "anos, então você é maior de idade.")
    print(f"\nBot: Em qual região você reside ?")

    moradia = str(input(f"\nVocê: "))
if moradia == moradia:
    print(f"\nBot: Certo,", nome, moradia, " deve ser um ótimo lugar!")

    resposta = input(
        f"\nBot:Você gosta de programar em Python? (S/N)").strip().upper()


if resposta == "S":
    print(f"\nBot: Que ótimo!", nome,
          "espero que continue aprendendo cada vez mais! Bons estudos de Python!")
else:
    if resposta == "N":
        print(f"\nBot: Isso é uma pena ", nome, "): ")
    else:
        print(f"\nBot: Você não digitou S ou")

print(f"\nBot:Muito Obrigado por interagir comigo!")
