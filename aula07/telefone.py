# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def searchPartName(contacts):
    partName = input("Procurar por? ").lower()
    filteredContacts = {}
    for key, value in contacts.items():
        if partName in value.lower():
            filteredContacts[key] = value
    print(filteredContacts)

def addContact(dic):
    number = input("Número do contacto a adicionar? ")
    name = input("Nome do contacto a adicionar? ")
    dic[number] = name
    print("O contacto", number, ":", name, "foi adicionado.")

def delContact(dic):
    number = input("Número do contacto a remover? ")
    removed = dic.pop(number)
    print("O contacto", number, ":", removed, "foi removido.")

def searchNumber(dic):
    number = input("Número do contacto a procurar? ")
    name = dic.get(number, False)
    if(name == False):
        print("O contacto não existe")
    else:
        print("O nome do contacto associado ao número", number, "é", name, end=".")
        print()



def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
        elif op == "R":
            delContact(contactos)
        elif op == "N":
            searchNumber(contactos)
        elif op == "P":
            searchPartName(contactos)
        else:
            print("Não implementado!")


# O programa começa aqui
main()

