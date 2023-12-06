from nltk.tokenize import word_tokenize
from os import system
from time import sleep


#/////////////VARIAVEIS GLOBAIS//////////////

#application_path = os.path.dirname(sys.executable)
#print(application_path)

#/////////////FUNÇÕES DE ANIMAÇÃO////////////
def starting_animation():
    system("color B")
    print("\tCONNECTING TO THE I.S.C.F. MAINFRAME\n")
    slowprint(".")
    sleep(0.5)
    slowprint(".")
    sleep(0.5)
    slowprint(".")
    sleep(0.5)
    
    print("\n\tCONNECTION AUTENTIFIED\n\n")
    sleep(0.7)
    print("User:")
    sleep(0.5)
    slowprint(">*********")
    print("\nPassword:")
    sleep(0.5)
    slowprint(">*******")
    print('\n')
    
    print("\tSeja bem vindo, <REDACTED>!\n")
    sleep(0.7)

#////////////PAUSE FUNCTION//////////////////

def pausa_de_impressão():
    print("Pressione qualquer tecla para continuar...")
    if(input()):
        return 0

#////////////IMPRESSÃO LENTA/////////////////

def slowprint(texto, atraso =0.2):
    for c in texto:
        print(c,end='', flush=True)
        sleep(atraso)
        
#//////VERIFICADOR DO ARQUIVO DE AJUDA///////     
def help_verifier():
    try:
        myfile=open("help_file/help.txt","r",encoding="utf-8")
    except:
        print("ERRO: ARQUIVO DE AJUDA NÃO ENCONTRADO")
        pausa_de_impressão()
        exit(-1)
#////////////SWITCHER DE ENTRADA/////////////
def entrada(comando):
    switcher = {
    "exit": 0,
    "help": 1,
    "open": 2,
    "clear": 3,
    "access_code": 4 
    }
    return switcher.get(comando,-1)

#///////////FUNÇÕES DO SWITCHER//////////////

#EXIT
def exit_funct():
    print("\n\n\n\tCONNECTION TERMINATED")
    print("\n\n\t\tI.S.C.F.\n\tPELA SEGURANÇA DE TODOS\n\n\n")
    pausa_de_impressão()

#HELP
def help():
    try:
        file=open("help_file/help.txt","r",encoding="utf-8")
        file_text = file.read()
        print(file_text)
        print("\n\n\n\n")
    except:
        print("ERRO: Arquvio de ajuda não encontrado")
        
#OPEN 
def open_file(arquivo):
    try:
        file=open("files/"+arquivo, "r", encoding="utf-8")
        file_text = file.read()
        print("\n\n"+file_text+"\n\n")
    except:
        print("\n\n\tERRO: Arquivo não encontrado\n\n")
    return 0

#error message
def error(string):
    print(string)
    exit(-1)


#/////////////FUNÇÃO PRIMCIPAL//////////////
def main():
    i=1
    starting_animation()
    help_verifier()
    while (i):
        print("///////////I.M.I Remote Terminal System////////////\n")
        print("\nQuery>", end = " ")       
        comando = input()
        vet = []
        vet = word_tokenize(comando)
        
        value = entrada(vet[0])
        if value == 0:
            exit_funct()
            break 
        if value == 1:
            help()
        if value == 2:
            if len(vet) == 2:
                open_file(vet[1])
            else: print("\n\nERRO: ARQUIVO NECESSÁRIO\nMétodo de uso: open \"nome_do_arquivo.txt\"\n\n")
        if value == 3:
            system("cls")
        if value == 4:
            print("\n\nINCORRECT CODE\n\n\n")
        if value == -1:
                print("\n\nCOMANDO NÃO RECONHECIDO\n\n\n")


    
    
    return 0


#INICIO DA EXECUÇÃO

main()
