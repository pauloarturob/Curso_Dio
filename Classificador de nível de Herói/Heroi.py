# Coletando o nome e a experiência do herói
print("veja abaixo os niveis de cada Herói:\n "
      """
      Ate 1.000 = Ferro
      1.001 e 2.000 = Bronze
      2.001 e 5.000 = Prata
      5.001 e 7.000 = Ouro
      7.001 e 8.000 = Platina
      8.001 e 9.000 = Ascendente
      9.001 e 10.000= Imortal
      Acima de 10.001 = Radiante\n""")

nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

# Verificando o nível do herói com base no XP
if xp < 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibindo a saída com o nível do herói
print(f"O Herói de nome {nome} está no nível de {nivel}.")
