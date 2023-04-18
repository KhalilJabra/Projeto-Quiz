print("Seja muito bem vindo ao quiz")
resposta_usuario = input("Quer começar? (S/N) ")

if resposta_usuario != "S":
    print("Ahh que pena :( ")
    quit()

pontos = 0

print("Começando....")

print("Quem foi o pai da computação?  \n (A) Alan Turing   \n (B) Mark Zuckerberg \n (C) Bill Gates ")

reposta_1 = input("Resposta: ")

if reposta_1 == "A":
    print("Correto!")
    pontos = pontos + 1
else:
    print("Incorreto")

print("Quem criou o java? \n (A) Elon Musk \n (B) Terry Myerson  \n (C) James Gosling")
reposta_2 = input("Resposta: ")

if reposta_2 == "C":
    print("Correto")
    pontos = pontos + 1
else:
    print("Incorrento")


print("Quem criou o java? \n (A) Yukihiro Matsumoto \n (B) Guido van Rossum  \n (C) Larry Page")
reposta_3 = input("Resposta: ")

if reposta_3 == "B":
    print("Correto")
    pontos = pontos + 1
else:
    print("Incorrento")

print(f"Quiz acabou...Pontuação: {pontos}/3 ")

