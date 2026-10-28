# Sistema PDV
## Resumo

O objetivo desse sistema é registrar vendas de um estabelecimento aplicando seus devidos em cada devido caso, mostrar o total de uma compra e ao encerrar o sistema, apresentar o histórico do dia com total de vendas e descontos aplicados, apresentar a quantidade de vendas feitas e descontos aplicados.

## Como o sistema funciona ?

O sistema recebe duas entradas de dados: valor da compra e idade. O sistema recebe esses dados e faz as verificações de descontos se houverem. As condições de descontos são :

- idade maior que 65 aplica-se 20%
- Descontos já aplicados sobre a idade  acima de R$ 100,00 reais ganham mais 10% de descontos. 
- desconto de 10% em compras maiores que R$ 100,00 reais 

Se não houver nenhuma regra de condição de desconto atendida, exibi-se o valor da compra normal. 

## Como rodar o Programa ? 
Após baixar o arquivo do programa, verifque se sua máquina possui Python, se não, baixe na loja oficial da Microsoft Store ou no site ofical do Python. Após, abra em uma IDE compatível com Python e abra o terminal da máquina direto na IDE e execute o segiuinte comando:

##### python pdv.py
Na IDE ofical do Python basta clicar no botão de play ou usar o atalho do teclado que já roda direto o programa. 

## Tabela de exemplos para testar o programa:
| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---|---|---|---|---|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |