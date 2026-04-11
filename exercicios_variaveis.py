# 1. Verificação de maior idade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais 
# (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou 
# tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".


# idade = int(input('Idade: '))
# autorizacao = input('True ou False: ')
# participar = (autorizacao == bool('True') or idade >= 18) and ' Pode participar' or 'não pode participar'


# print(participar)

# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".


# peso = float(input('Peso (kg): '))
# altura = float(input('Altura (m): '))


# imc = peso / (altura ** 2)

# classificacao = (imc >= 18.5 and imc <= 24.9) and 'Peso normal' or 'Fora da faixa'

# print(classificacao)





# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

#  


# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.


# valor = float(input('Valor da compra: '))
# vip = input('Cliente VIP? (True/False): ')

# final = (valor > 100 or vip == 'True') and valor * 0.9 or valor

# print(final)


# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e 
# pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.


# idade = int(input('idade:'))
# peso = float(input('peso:'))

# doar = (idade >= 16 and idade <= 69 and peso >= 50) and 'pode doar' or 'não pode doar'

# print (doar)



# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar 
# sábado/domingo como fechado.


# dia = int(input('Dia (1-7): '))
# hora = int(input('Hora (0-23): '))

# aberta = (dia >= 1 and dia <= 5 and hora >= 9 and hora <= 18) and 'Aberta' or 'Fechada'

# print(aberta)


# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".


 
# matematica = float(input('mat: '))
# portugues = float(input('port: '))

# resultado = (mat >= 6 and port >=6) and ' aprovado' or 'reprovado'


# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input('Ano: '))

bissexto = ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)) and 'Ano bissexto' or 'Ano não bissexto'

print(bissexto)

# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.


idade = int(input('Idade: '))

faixa = (idade < 12 and 'Criança') or (idade >= 12 and idade <= 17 and 'Adolescente') or (idade >= 18 and 'Adulto')

print(faixa)




# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.


temp = float(input('Temperatura: '))
umidade = float(input('Umidade: '))

alerta = (temp > 35 or umidade > 70) and 'Alerta' or 'Condições normais'

print(alerta)