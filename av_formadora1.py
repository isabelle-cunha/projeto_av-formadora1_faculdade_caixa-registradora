#perguntar quantos produtos serão registrados [x]
#para cada produto,solicitar: nome do produto, preço unitario e quantidade comprada. [x]
#calcular o subtotal de cada produto (preço x quantidade)
#somar ao total geral da compra
#peguntar a forma de pagamento: 1 (a vista), 2(cartão de credito)

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
#usar laço de repetição para registrar os produtos
#uso de variáveis para controle do total e desconto
#uso de estrutura condicional para aplicação das regras
#saída formatada e clara.

#entrada de dados
qntd_produtos_informados=int(input("Informe, com números, quantos produtos serão registrados: "))
forma_pagamento=int(input("Qual a forma de pagamento? Digite 1 para pagamento à vista e 2 para cartão de crédito: "))
lista_produtos=[]
valores_produtos=[]
qntd_produtos=[]

#processamento  
def registrar_produto(qntd_produtos_informados):
    for n_produtos in range(qntd_produtos_informados):
        nome_produto=input(f"Digite o nome do produto {(n_produtos)}: ")
        lista_produtos.append(nome_produto)
    return lista_produtos
       
def registrar_valor_unidade(qntd_produtos_informados):
    for i in range(qntd_produtos_informados):
        valor_unidade=float(input(f"Digite o valor de {lista_produtos[i]}: "))
        valores_produtos.append(valor_unidade)
    return valores_produtos
    
def registrar_qntd_cada(qntd_produtos_informados):
     for n_qntd in range(qntd_produtos_informados):
        qntd_cada = int(input(f"Digite a quantidade de cada {lista_produtos [n_qntd]}: "))
        qntd_produtos.append(qntd_cada)
     return qntd_produtos


       
  
#saída de dados
print(registrar_produto(qntd_produtos_informados))
print(registrar_valor_unidade(qntd_produtos_informados))
print(registrar_qntd_cada(qntd_produtos_informados))
