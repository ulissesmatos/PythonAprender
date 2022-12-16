janela = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
corredor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        

#codigo main
def busy(lado, poltrona, ocupado):
    int_poltrona = int(poltrona)
    int_poltrona -= 1
    if (lado == "j" or lado =="J") and ocupado == 1:
        if janela[int_poltrona] == 1:
            print("Vaga já ocupada!")
        else:
            janela[int_poltrona] = 1
            print(f"-> Vaga {int_poltrona+1} da Janela, vendida com sucesso\n")

    elif (lado == "c" or lado =="C") and ocupado == 1:
        if corredor[int_poltrona] == 1:
            print("Vaga já ocupada!")
        else:
            corredor[int_poltrona] = 1
            print(f"-> Vaga {int_poltrona+1} do corredor, vendida com sucesso\n")



def ocupadoLista():
    i = 0
    countJan = 0
    countCor = 0
    while i < 24:
        if janela[i] == 0:
            print ("Janela   " + str(i+1) + ": Livre")
        if janela[i] == 1:
            print("Janela   " + str(i+1) + ": Ocupado")
            countJan += 1
        if corredor[i] == 0:
            print ("Corredor " + str(i+1) + ": Livre")
        if corredor[i] == 1:
            print ("Corredor " + str(i+1) + ": Ocupado")   
            countCor += 1         
        i += 1

def qtdOcupacao():
    i = 0
    count_janela = 0
    count_corrredor = 0
    while i < 24:
        if janela[i] == 1:
            count_janela += 1
        if corredor[i] == 1:
            count_corrredor += 1
        i += 1
    if count_corrredor == 24:
        print(">>>>>>> Onibus lotado no lado: Corredor <<<<<<<")
    if count_corrredor >= 22 and count_corrredor <= 23:
        print(f"Onibus quase lotado há {count_corrredor} assentos no lado do corredor")
    if count_janela == 24:
        print(">>>>>>> Onibus lotado no lado: Janelas <<<<<<<")
    if count_janela >= 22 and count_corrredor <= 23:
        print(f"Onibus quase lotado há {count_janela} assentos no lado das janelas")
    if count_janela <= 21:
        print (f"Onibus com {count_janela} assentos de janela ocupados")
    if count_corrredor <= 21:
        print (f"Onibus com {count_corrredor} assentos de corredor ocupados\n")
    if count_corrredor == 0 and count_janela == 0:
        print("Todos as vagas estão livres\n")

while (True):
    print("O que você quer fazer?")
    inicio = input("1 - Vender | 2 - Mostrar Ocupação | 3 - Veificar Qtd. | 4 - Encerrar: ")
    if inicio == str("1"):
        print("Selecione uma poltrona: ")
        selecaoJanCor = input("J - Janela | C - Corredor: ")
        selecaoPoltrona = input("Qual Poltrona (1 a 24): ")
        busy(selecaoJanCor, selecaoPoltrona, 1)
    elif inicio == str("2"):
        print("Mapa de Ocupação:")
        ocupadoLista()
    elif inicio == str("3"):
        print("\nVerificando quantidade de vagas: ")
        qtdOcupacao()
    elif inicio == str("4"):
        print("Encerrando...")
        break