import math
import calendar

# Módulos
# Exercício 1
x = math.cos(math.pi / 2) + math.sin(math.pi / 2)
print(x)

x = math.sqrt(3)
print(x)

x = math.log(10, 2)
print(x)

# Exercício 2
print("2018 " + ("" if calendar.isleap(2018) else "não ") + "é um ano bissexto" )
nome_dias = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]
print("22 de Maio de 1992 era um/uma " + nome_dias[calendar.weekday(1992, 5, 22)])
print("O mês de julho de 2000 começou em um/uma " + nome_dias[calendar.weekday(2000, 7, 1)])

# Variáveis e tipos
# Exercício 1
x = 1
y = 2.3
z = x + y
print("x é um " + type(x).__name__)
print("y é um " + type(y).__name__)
print("z é um " + type(z).__name__)

# Exercício 2
x = 1
y = 4
z = x / y
print("O valor de z é " + str(z))

# Exercício 3
x = 1.0
y = 4
z = x / y
print("O valor de z é " + str(z))

# Exercício 4
imc = 100.0 / (1.75 ** 2)
print("Meu IMC é " + str(imc))

# Operadores e Comparações
# Exercício 1
x = 7
print("x * 2 " + ("é" if (x * 2) > 10 else "não é") + " maior que 10")
print("x / 3 " + ("é" if (x / 3) < 5 else "não é") + " menor que 5")
print("x ao quadrado " + ("é" if (x ** 2) == 49 else "não é") + " igual a 49")

# Exercício 2
y = 3
print("y é menor que 10 e x é maior que 10? " + ("Sim" if y > 10 and x > 10 else "Não"))
print("y é maior ou igual a 3 ou x é igual a 8? " + ("Sim" if y >= 3 or x == 8 else "Não"))
print("y não é igual a 4? " + ("Sim" if y != 4 else "Não"))

# Exercício 3
print("Meu IMC " + ("está" if imc >= 18.5 and imc < 25 else "não está") + " dentro do padrão recomendado pela OMS")

# Strings
# Exercício 1
s = "Curso de graduação Universidade Univille Campus - Joinville!"
idx = s.find("Univille")
print(s[idx : idx + len("Univille")])
idx = s.find("Joinville")
print(s[idx : idx + len("Joinville")])

# Exercício 2
print(s[::-1])

# Listas
# Exercício 1
pib = [
    ["china", 23120],
    ["usa", 19360],
    ["india", 9447],
    ["japan", 5405],
    ["germany", 4150],
    ["russia", 4000],
    ["indonesia", 3243],
    ["brazil", 3219]
]
pib.append(["turquia", 1350])

# Dicionários
# Exercício 1
pib = {
    "china": 23120,
    "usa": 19360,
    "india": 9447,
    "japan": 5405,
    "germany": 4150,
    "russia": 4000,
    "indonesia": 3243,
    "brazil": 3219
}
print("Países dentro do dicionário pib:")
for pais in pib:
    print(pais)

# Exercício 2
soma = 0
for pais in pib:
    soma += pib[pais]
pib["total"] = soma
print(pib["total"])

# Controle de fluxo
# Exercício 1
imc_classificacoes = [
    ["Magreza grave", -1, 16],
    ["Magreza moderada", 16, 17],
    ["Magreza leve", 17, 18.5],
    ["Saudável", 18.5, 25],
    ["Sobrepeso", 25, 30],
    ["Obesidade Grau I", 30, 35],
    ["Obesidade Grau II", 35, 40],
    ["Obesidade Grau III", 40, -1]
]

for classificacao in imc_classificacoes:
    if (imc >= classificacao[1] or classificacao[1] == -1) and (imc < classificacao[2] or classificacao[2] == -1):
        print("Classificação IMC: " + classificacao[0])
        break