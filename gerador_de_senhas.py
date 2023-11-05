#Gerador de senhas aleatórias usando a biblioteca secrets
'''
O módulo secrets é usado para gerar números aleatórios 
criptograficamente fortes, adequados para o gerenciamento 
de dados, como senhas, autenticação de conta, tokens de 
segurança e segredos relacionados.
'''

import numpy as np
import secrets

numero_de_senhas = int(input('Qual o número de senhas que deseja criar? '))
numero_de_caracteres = int(input('Qual o número de caracteres que a senha deve ter? '))

#Array de caracteres que serão utlizados para a geração das senhas
caracteres = np.array(['a','b','c','d','f','g','h','i',
                'j','k','l','m','n','p','q','r',
                's','t','v','w','x','y','z',
                'A','B','C','D','F','G','H','I',
                'J','K','L','M','N','P','Q','R',
                'S','T','V','W','X','Y','Z',
                '!','@','#','$','%','&','*','(',')','[',']','{','}',
                '<','>',',','.',':',';','/','1','2','3','4','5','6','7','8','9'])

#Cria um array de valores que vai receber os números aletórios
values = np.array([])

#Preenche o array values com os números aletórios gerados pelo sistema operacional 
#Esses valores i's serão utilizados para selecionar um elemento i do array caracteres
for n in range(numero_de_senhas*numero_de_caracteres):
    random_number = secrets.randbelow(len(caracteres))
    values = np.append(values, random_number)

#Cria um array de que vai receber as senhas aleatórias
palavras = np.array([])
senha = ''

for i in range(len(values)):
    senha = senha + caracteres[int(values[i])]
    if (i + 1) % numero_de_caracteres == 0:
        #Assim que atingir o número de caracteres que deseja na senha, a senha é adionada no array de senhas
        palavras = np.append(palavras, senha)
        senha = ''

#Imprimi as senhas
for password in palavras:
    print(password)       

