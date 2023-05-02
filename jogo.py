import random
from sty import fg, bg, ef, rs
import csv
from datetime import datetime

score = 0
nrmLinhas = 8
nrmColunas = 10
bombas = 0
bomba = []
jogo = []
derrotado = False
venceu = False
data = datetime.now()
dataBonita = data.strftime("%d/%m/%Y %H:%M")


dificuldade = 0
escolhidol = 0
escolhidoc = 0
nome = ''

pontuacao = {}


def contar_simbolo(matriz, casinhas):
    cont = 0
    for linha in matriz:
        for casa in linha:
            if casa == casinhas:
                cont += 1
    return cont

def salvar_pontos():
   with open('pontuacao.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for nome, score in pontuacao.items():
        writer.writerow([nome, score, dataBonita])
    csvfile.close()

def mostrar_pontos():
    with open('pontuacao.csv', newline='') as csvfile:
        lerArquivo = csv.reader(csvfile)
        next(lerArquivo)
        dados = [linha for linha in lerArquivo]
    dados_ordenados = sorted(dados, key=lambda x: int(x[1]), reverse=True)
    print() 
    print(bg.blue + 'ScoreBoard'+ bg.rs)
    print()
    for nome, score, dataBonita in dados_ordenados:
        print(ef.italic + f"{nome} ===> {score} pontos {dataBonita}" + rs.italic)
    
def nomeJogador():
    global nome
    nome = input('Qual seu nome ? ').capitalize()
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
            if casa == '+':
                print(fg.yellow + f' {casa} ' + fg.rs, end ="")
            elif casa.isdigit():
                print(fg.green + f' {casa} ' + fg.rs, end ="")
            else:
                print(f' {casa} ' , end ="")
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


    #print(jogo[escolhidol][escolhidoc])              

def inicioJogo():
    for i in range(nrmLinhas):
        bomba.append([])
        for j in range(nrmColunas):
            bomba[i].append('#')
    campoBombas()

def campoBombas():
 global bombas
 if dificuldade == 1:
     bombas = 0
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
    for i, linha in enumerate(bomba, start=0):
        print(f'{i} |', end="")
        for casa in linha:
            if casa == '*':
                print(fg.red + f' {casa} ' + fg.rs, end="")
            elif casa == '+':
                print(fg.yellow + f' {casa} ' + fg.rs, end="")
            else:
                print(f' {casa} ', end="")
        print("|")
    print('  +------------------------------+')
    print("    0  1  2  3  4  5  6  7  8  9")   
    
def escolha():
    global escolhidol
    global escolhidoc
    global score
    global derrotado
    global venceu
   
    while True:
        num_hashes = contar_simbolo(jogo, '#')

        if num_hashes == 0:
            while True:
                print(fg.green + 'PARABENS!!!!! VOCE GANHOU!!!!!!' + fg.rs)  
                salvar = input("Digite 's' se desejas salvar sua pontiação ou 'n' caso não queira: ")
                venceu = True
                if salvar == 's' or salvar == 'S':
                    pontuacao[nome] = score
                    salvar_pontos()
                    break
                else:
                    print('Okkk até mais!!')
                    break
            break
        else:
            linha = int(input('Escolha uma linha (0-7): ')) 
            coluna = int(input('Escolha uma coluna (0-9): '))
            escolhidol = linha
            escolhidoc = coluna
            
            if linha < 0 or linha >= nrmLinhas or coluna < 0 or coluna >= nrmColunas:
                return print('Esolha um local valido')
            
            elif escolhidoc == '' or escolhidol == '':
                return print('escolha um valor')
            
            elif bomba[escolhidol][escolhidoc] == '*':
                visualJogoBomba()
                print(bg.red + '      ***!!BOOM!!***      ' + bg.rs)  
                derrotado = True  
                while True:
                    salvar = input("Digite 's' se desejas salvar sua pontiação ou 'n' caso não queira: ")
                    if salvar == 's' or salvar == 'S':
                        pontuacao[nome] = score
                        salvar_pontos()
                        break
                    else:
                        print('Okkk até mais!!')
                        break
                break

                

            elif bomba[escolhidol][coluna] == '+':
                return print('escolha um local que não foi escolhido')

            
            else:
                bomba[linha][coluna] = '+'
                jogo[linha][coluna] = '+'
                

                visualJogo()
                
                if dificuldade == 1:
                    score += 200
                elif dificuldade == 2:
                    score += 300
                elif dificuldade == 3:
                    score += 400
                
                print(f'Score ===> {score}')
                        

nomeJogador()
escolhaDificuldade()
inicioJogo()
matrizAposta()

#  JOGO  #
while True:

    if venceu == True: 
        print()
        print('1 -- Ver ScoreBoard')
        print('2 -- Sair')
        print()
        decidir = int(input('O Que desejas fazer ? '))    
        if decidir == 1:
            mostrar_pontos()
        if decidir == 2:
            print("Até mais!! Volte sempre!!")
            break
    
    elif derrotado == True:
        print()
        print('1 -- Ver ScoreBoard')
        print('2 -- Ver campo com as bombas')
        print('3 -- Sair')
        print()
        selecionar = int(input('O Que desejas fazer ? ')) 
        if selecionar == 1:
            mostrar_pontos()
        if selecionar == 2:
            visualJogoBomba()        
        if selecionar == 3:
            print("Até mais!! Volte sempre!!")
            break
    else :   
        print()
        print('1 -- Jogar')
        print('2 -- Ver ScoreBoard')
        print('3 -- Sair')
        print()
        ecolher = int(input('O Que desejas fazer ? '))

        if ecolher == 1:
            escolha()
        if ecolher == 2:
            mostrar_pontos()
        if ecolher == 3:
           print("Até mais!! Volte sempre!!")
           break

