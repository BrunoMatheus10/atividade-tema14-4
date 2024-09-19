# Função para calcular o pagamento com base nas horas trabalhadas e no valor por hora
def pagamento(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

# Leitura das horas trabalhadas e do valor por hora do usuário
horas = float(input("Digite as horas trabalhadas: "))
valor = float(input("Digite o valor por hora: "))

# Exibição do valor a ser pago
print("Valor a ser pago: ",pagamento(horas, valor))
