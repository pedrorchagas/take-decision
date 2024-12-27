from time import sleep
from random import choice
print("Bem-vindo ao tomador de decisões \n(o aplicativo que te ajuda a tomar decisões complicadas baseada na sorte)\n\n")

question = input(print("Por favor, me diga qual decisão está precisando tomar?"))

print("Entendi, então vamos lá!")
print("\nPensando...\n")
sleep(2)

responses = [True, False]
response = choice(responses)
if response:
    response = "Sim"
else:
    response = "Não"

print("\nFinalmente cheguei a resposta!\n")
print(f"a resposta para a sua pergunta: {question} é:\n{response}")