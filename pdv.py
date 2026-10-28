lista_de_vendas = []
lista_de_descontos = []

desconto_1 = 20
desconto_2 = 10

while True:
   valor_da_compra = float(input("Digite o valor da compra: "))
   while valor_da_compra < 0:
      print("Erro: o valor não pode ser negativo !")
      valor_da_compra = float(input("Digite o valor da compra: "))
      break
   lista_de_vendas.append(valor_da_compra)
   if valor_da_compra == 0:
       print("Sistema encerrado")
       break
   idade_do_cliente = int(input("Digite a sua idade: "))
   quantidade = len(lista_de_vendas)
   total = sum(lista_de_vendas)

   valor_final = valor_da_compra

   if idade_do_cliente >= 65:
      valor_desconto_l = (valor_da_compra * (desconto_1 / 100))
      resultado_1 = ((valor_da_compra - valor_desconto_l))
      lista_de_descontos.append(valor_desconto_l)
      print(f"Valor após desconto de idade: R$ {resultado_1:.2f}")

      if resultado_1 > 100:
       valor_desconto_2 = (resultado_1 * (desconto_2 / 100))
       resultado_2 = ((resultado_1 - valor_desconto_2))
       lista_de_descontos.append(valor_desconto_2)
       print(f"Valor após desconto de valor alto : R$ {resultado_2:.2f}")
   elif valor_da_compra > 100:
        valor_desconto_3 = valor_da_compra * (desconto_2 / 100)
        resultado_3 = valor_da_compra - valor_desconto_3
        print("Valor da compra: R$ {:.2f}".format(resultado_3))
   else:
       print(valor_da_compra)

quantidade_descontos = len(lista_de_descontos)
total_de_descontos = sum(lista_de_descontos)

print(f"Compras Registradas: {quantidade}")
print(f"Total de vendas : R$ {total:.2f}")
print(f"Quantidade de descontos concedidos: {quantidade_descontos}")
print(f"Total de descontos concedidos: R$ {total_de_descontos:.2f}")
