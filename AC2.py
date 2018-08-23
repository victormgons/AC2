#Nomes:
#Victor Mateus, Matheus Tavares, Valéria Pereira
#RAs:
#1800124, 1800282, 1800382

import sys
import csv
 
def addContact():
    print("Adicionar um registro")
    agenda = open("contactsList.csv",'a')
    nome = input("Nome do Contato: ").lower().capitalize()
    telefone = input("Digite o telefone: ")
    print("Contato salvo com nome: ",nome," e numero ",telefone)
    agenda.write(nome)
    agenda.write(",")
    agenda.write(telefone)
    agenda.write("\n")
    agenda.close()
    showOptions()
	
def listConacts():
    print("Lista de Contatos\n")
    agenda = open("contactsList.csv")
    for rows in agenda:
        print(rows)
    agenda.close()
    showOptions()

def invalidOption():
    print("Opcão incorreta!")
    showOptions()

def showOptions():
    print("\nSelecione uma opção:")
    print("1 - Adicionar um novo contato")
    print("2 - Listar os contatos da agenda")
    print("3 - Buscar um contato")
    print("4 - Deletar um contato")
    print("5 - Sair do programa")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        addContact()
    elif opcao == 2:
        listConacts()
    elif opcao == 3:
        #findContact()
        print("Função não terminada!")
    elif opcao == 4:
        #deleteContact()
        print("Função não terminada!")
    elif opcao == 5:
        sys.exit()
    else:
        invalidOption()

def welcome():
    print("Bem Vindo a Agenda")
    showOptions()

welcome()
