#Entrada programa de descontos

print("Olá, vamos calcular se há algum desconto disponível para sua compra!\n")
valor_compra = float(input("Digite o valor total da sua compra:"))

#Processamento/verificando condições

if valor_compra >= 300.00:
    print("Um desconto de está 15% está disponível para sua compra!\n")
    valor_desconto = 0.15
elif valor_compra >= 200.00: 
    print("Um desconto de 10% está disponível para sua compra!\n")
    valor_desconto = 0.10
else:
    print("Um desconto de 5% está disponível para sua compra!\n")
    valor_desconto = 0.05 

#Processamento cálculos

desconto_final = valor_compra * valor_desconto
valor_final = valor_compra - desconto_final 

#Saída

print(f"Total da compra: R${valor_compra: .2f}")
print(f"Desconto aplicado: R$ {desconto_final: .2f}")
print(f"Total a pagar: R$ {valor_final: .2f}")