#Simulador de caixa registradora

#ENTRADA DE DADOS:
while True:
    qntd_produtos_informados = int(input("Informe, com números, quantos produtos serão registrados: "))
    if qntd_produtos_informados < 1:
        print("Quantidade inválida! Tente novamente.")
    else:
        break

#listas
lista_produtos=[]
valores_produtos=[]
qntd_unidades=[]
subtotal_cada=[]

#PROCESSAMENTO:
#1)Registros
def registrar_produto(qntd_produtos_informados):
    for n_produtos in range(qntd_produtos_informados):
        nome_produto=input(f"Digite o nome do produto {n_produtos} que deseja registrar: ")
        lista_produtos.append(nome_produto)
    return lista_produtos

def registrar_valor_unidade(qntd_produtos_informados):
    for i in range(qntd_produtos_informados):
        preco_unidade=float(input(f"Digite o preço da unidade de {lista_produtos[i]}: "))
        valores_produtos.append(preco_unidade)
    return valores_produtos

def registrar_qntd_cada(qntd_produtos_informados):
    for i in range(qntd_produtos_informados):
        qntd_cada = int(input(f"Digite a quantidade de unidades de {lista_produtos [i]}: "))
        qntd_unidades.append(qntd_cada)
    return qntd_unidades

def calcular_subtotal():
    for i in range(len(qntd_unidades)):
        subtotal= valores_produtos[i] * qntd_unidades[i]
        subtotal_cada.append(subtotal)
    return subtotal_cada

#2)Definindo forma de pagamento:
def registrar_forma_pagamento():
    while True:
        forma_pagamento=int(input("Qual a forma de pagamento? Digite 1 para pagamento à vista e 2 para cartão de crédito: "))
        if forma_pagamento == 1:
            print("Pagamento à vista.")
            return forma_pagamento
        elif forma_pagamento == 2:
            print("Pagamento no crédito.")
            return forma_pagamento
        else:
            print("Forma de pagamento inválida! Tente novamente.")

#3)Descontos:
def calcular_desconto(total_bruto,forma_pagamento):
    desconto=float()
    if forma_pagamento==1 and total_bruto>200:
        numerador_p=int(15)
        print("Você teve desconto de 15%!")
        desconto= total_bruto * (numerador_p/100)
        return desconto
    elif forma_pagamento==1 and (total_bruto>=100 and total_bruto<=200):
        numerador_p=10
        print("Você teve desconto de 10%!")
        desconto= total_bruto * (numerador_p/100)
        return desconto
    else:
        print("Você não teve desconto!")
        return desconto
    
#4)Relatório Final
def exibindo_relatorio():
   print("==============================|     NOTINHA     |==============================")
   print("Produtos:")
   for i in range(len(lista_produtos)):
       print(f"{lista_produtos[i]} -> Qntd.Unidades: {qntd_unidades[i]} x R$ {valores_produtos[i]:.2f} = R$ {subtotal_cada[i]:.2f}")
   print("-------------------------------------------------------------------------------")
   print("Forma de pagamento:")
   if forma_pagamento == 1:
       print("Pagamento à vista.")
   else:
       print("Pagamento no crédito.")
   print("-------------------------------------------------------------------------------")
   print(f"Total antes do desconto: R$ {total_bruto:.2f}")
   print(f"Valor total com desconto: R${ total_final:.2f}")
   print(f"Valor descontado: R${desconto:.2f}")
   print(f"------------------------------|    TOTAL    |--------------------------------")
   print(f"Total final a pagar: R${total_final:.2f}")

#SAÍDA DE DADOS
#1)#Acompanhando funcionamento:
print("Os produtos registrados foram:" ,registrar_produto(qntd_produtos_informados))
print("O valor de cada unidade dos produtos registrados, em R$, é: ",registrar_valor_unidade(qntd_produtos_informados))
print("A quantidade de unidades por produto é:" ,registrar_qntd_cada(qntd_produtos_informados))
print("O subtotal de cada produto (quantidade de unidades x preço unidade), em R$, é: ",calcular_subtotal())

#1.5)Variáveis auxiliares:
total_bruto=sum(subtotal_cada)
forma_pagamento = registrar_forma_pagamento()
desconto=calcular_desconto(total_bruto,forma_pagamento)
valor_descontado=desconto
total_final=(total_bruto) - (desconto)

print("O valor total (bruto) da compra, em R$, é: ", f"{total_bruto:.2f}")
print("O valor total (com desconto), em R$, é:" ,f"{desconto:.2f}")

#2)Saída da notinha:
exibindo_relatorio()