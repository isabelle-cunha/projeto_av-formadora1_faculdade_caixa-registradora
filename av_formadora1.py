#perguntar quantos produtos serão registrados [x]
#para cada produto,solicitar: nome do produto, preço unitario e quantidade comprada. [x]
#calcular o subtotal de cada produto (preço x quantidade)[x]
#somar ao total geral da compra [x]
#peguntar a forma de pagamento: 1 (a vista), 2(cartão de credito)[x]

#aplicar descontos no total geral conforme: 
#total acima de 200 reais a vista (15% de desconto)
#total entre 100reais e 200reais a vista (10% de desconto)
#cartão de credito (sem desconto)

#exibir relatório final contendo:
#lista dos produtos (nome,qntd,preço uunitário,subtotal)
#total antes do desconto
#valor do desconto aplicado
#valor total final a pagar

#requisitos mínimos:
#usar laço de repetição para registrar os produtos[x]
#uso de variáveis para controle do total e desconto[x]
#uso de estrutura condicional para aplicação das regras[x]
#saída formatada e clara.[]

#entrada de dados
while True:
    qntd_produtos_informados = int(input("Informe, com números, quantos produtos serão registrados: "))
    if qntd_produtos_informados < 1:
        print("Quantidade inválida! Tente novamente.")
    else:
        break


lista_produtos=[]
valores_produtos=[]
qntd_produtos=[]
subtotal_cada=[]


#processamento  
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
        qntd_produtos.append(qntd_cada)
    return qntd_produtos

def calcular_subtotal():
    for i in range(len(qntd_produtos)):
        subtotal= valores_produtos[i] * qntd_produtos[i]
        subtotal_cada.append(subtotal)
    return subtotal_cada

def registrar_subtotal(subtotal_cada):
    total_bruto=float(0)
    for i in range(len(subtotal_cada)):
        total_bruto = total_bruto + (subtotal_cada[i])
        #python f'{var:.2f}'= javascript var.toFixed(2)
    return f'{total_bruto:.2f}'

#Definindo forma de pagamento:
def registrar_forma_pagamento():
    while True:
        forma_pagamento=int(input("Qual a forma de pagamento? Digite 1 para pagamento à vista e 2 para cartão de crédito: "))
        if forma_pagamento == 1:
            pagamento='à vista'
            print('Forma de pagamento:' ,pagamento)
            break
        elif forma_pagamento == 2:
            pagamento='cartão de crédito'
            print('Forma de pagamento:' ,pagamento)
            break
        else:
            print("Forma de pagamento inválida.")

       
  
#saída de dados
print("Os produtos registrados foram:" ,registrar_produto(qntd_produtos_informados))
print("O valor de cada unidade dos produtos registrados é:" ,registrar_valor_unidade(qntd_produtos_informados))
print("A quantidade de unidades por produto é:" ,registrar_qntd_cada(qntd_produtos_informados))
print("O subtotal de cada produto (quantidade de unidades x preço unidade) é:" ,calcular_subtotal())
print("O valor total bruto da compra é: R$",registrar_subtotal(subtotal_cada))