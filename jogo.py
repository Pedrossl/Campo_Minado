import random
from termcolor import colored
from sty import fg, bg, ef, rs
import csv

score = 0
nrmLinhas = 8
nrmColunas = 10
bombas = 0
bomba = []
jogo = []



dificuldade = 0
escolhidol = 0
escolhidoc = 0
nome = ''

pontuacao = {}

#bla = {'Nome': nome, 'Score': score}


def contar_simbolo(matriz, casinhas):
    cont = 0
    for linha in matriz:
        for casa in linha:
            if casa == casinhas:
                cont += 1
    return cont


def nomeJogador():
    global nome
    global dificuldade
    nome = input('Qual seu nome ? ')
    print(f'Certo {nome} vamos ver se voce é bom mesmo!!')

def escolhaDificuldade():
    global dificuldade
    while True:
        print('Digite 1 para' + fg.green + ' facil'+ fg.rs)
        print('Digite 2 para' + fg.yellow + ' medio'+ fg.rs)
        print('Digite 3 para' + fg.red + ' dificil'+ fg.rs)
        dificuldade = int(input('Escolha a dificuldade: '))
        if dificuldade == 1 or dificuldade == 2 or dificuldade == 3:
            break
        else:
            print("Escolha uma dificuldade valida")

def matrizAposta():
    for i in range(nrmLinhas):
        jogo.append([])
        for j in range(nrmColunas):
            jogo[i].append('#')

def visualJogo():
    print()
    mostrarNumeros()
    print('  +------------------------------+')
    for i,linha in enumerate(jogo, start=0):
        print(f'{i} |', end = "")
        for casa in linha:
         print(f' {casa} ', end ="")
        print("|")
    print('  +------------------------------+')
    print("    0  1  2  3  4  5  6  7  8  9")   
    
def mostrarNumeros():
    numBombas = 0   

    if bomba[escolhidol][escolhidoc] != '*':
            
        if escolhidol > 0 and bomba[escolhidol - 1][escolhidoc] == '*': 
            numBombas += 1
        
        if escolhidol < len(bomba) - 1 and bomba[escolhidol + 1][escolhidoc] == '*':
            numBombas += 1
            
        if escolhidoc < len(bomba[0]) - 1 and bomba[escolhidol][escolhidoc + 1] == '*':
            numBombas += 1
            
        if escolhidoc > 0 and bomba[escolhidol][escolhidoc - 1] == '*':
            numBombas += 1

        if escolhidol < len(bomba) - 1 and escolhidoc < len(bomba[0]) - 1 and bomba[escolhidol + 1][escolhidoc + 1] == '*':
            numBombas += 1

        if escolhidol > 0 and escolhidoc < len(bomba[0]) - 1 and bomba[escolhidol - 1][escolhidoc + 1] == '*':
            numBombas += 1

        if escolhidol < len(bomba) - 1 and escolhidoc > 0 and bomba[escolhidol + 1][escolhidoc - 1] == '*':
            numBombas += 1

        if escolhidol > 0 and escolhidoc > 0 and bomba[escolhidol - 1][escolhidoc - 1] == '*':
            numBombas += 1 
    
    if escolhidol > 0:
        jogo[escolhidol - 1][escolhidoc] = f'{numBombas}'
    if escolhidol < len(jogo) - 1:
        jogo[escolhidol + 1][escolhidoc] = f'{numBombas}'
    if escolhidoc > 0:
        jogo[escolhidol][escolhidoc - 1] = f'{numBombas}'
    if escolhidoc < len(jogo[0]) - 1:
        jogo[escolhidol][escolhidoc + 1] = f'{numBombas}'
    if escolhidol < len(jogo) - 1 and escolhidoc < len(jogo[0]) - 1:
        jogo[escolhidol + 1][escolhidoc + 1] = f'{numBombas}'
    if escolhidol > 0 and escolhidoc < len(jogo[0]) - 1:
        jogo[escolhidol - 1][escolhidoc + 1] = f'{numBombas}'
    if escolhidol < len(jogo) - 1 and escolhidoc > 0:
        jogo[escolhidol + 1][escolhidoc - 1] = f'{numBombas}'
    if escolhidol > 0 and escolhidoc > 0:
        jogo[escolhidol - 1][escolhidoc - 1] = f'{numBombas}'


    print(jogo[escolhidol][escolhidoc])              

def inicioJogo():
    for i in range(nrmLinhas):
        bomba.append([])
        for j in range(nrmColunas):
            bomba[i].append('#')
    campoBombas()

def campoBombas():
 global bombas
 if dificuldade == 1:
     bombas = 10
 elif dificuldade == 2:
     bombas = 25
 elif dificuldade == 3:
     bombas = 50
 
 for i in range(bombas):
    while True:
        x = random.randint(1, nrmColunas - 1)
        y = random.randint(0, nrmLinhas - 1)
        if bomba[y][x] == '#':
            bomba[y][x] = '*'
            break

def visualJogoBomba():
    print()
    print('  +------------------------------+')
    for i,linha in enumerate(bomba, start=0):
        print(f'{i} |', end = "")
        for casa in linha:
         print(f' {casa} ', end ="")
        print("|")
    print('  +------------------------------+')
    print("    0  1  2  3  4  5  6  7  8  9") 

    
    
def escolha():
    global escolhidol
    global escolhidoc
    global score
    while True:
            ganharJogo()
            linha = int(input('Escolha uma linha (1-8): ')) 
            coluna = int(input('Escolha uma coluna (1-10): '))
            escolhidol = linha
            escolhidoc = coluna
            
            if linha < 0 or linha >= nrmLinhas or coluna < 0 or coluna >= nrmColunas:
                return print('Esolha um local valido')
            
            elif escolhidoc == '' or escolhidol == '':
                return print('escolha um valor')
            
            elif bomba[escolhidol][escolhidoc] == '*':
                visualJogoBomba()
                print(fg.red + 'BOOM!!' + fg.rs)    
                break

            elif bomba[escolhidol][coluna] == '+':
                return print('escolha um local que não foi escolhido')
            
            else:
                bomba[linha][coluna] = '+'
                jogo[linha][coluna] = '+'
                

                visualJogo()
                ganharJogo()
                
                if dificuldade == 1:
                    score += 200
                elif dificuldade == 2:
                    score += 300
                elif dificuldade == 3:
                    score += 400
                    
                
                
                print(f'Score ===> {score}')
                        
        
            
    

def ganharJogo():
    num_hashes = contar_simbolo(jogo, '#')

    if num_hashes == 0:
        print(fg.green +'PARABENS VOCE GANHOU!!!!'+ fg.rs)
        

nomeJogador()
escolhaDificuldade()
inicioJogo()
matrizAposta()

while True:
        
        if bomba[escolhidol][escolhidoc] == '*':
            print('Voce perdeu!!!')
            break
        print('1 -- Jogar')
        print('2 -- Ver ScoreBoard')
         
        ecolher = int(input('O Que desejas fazer ?'))
        

        if ecolher == 1:
            escolha()
        if ecolher == 2:
            print('alo')
            break

