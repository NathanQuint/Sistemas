#Questões Fundamentais
print(f"Bom dia,para conseguirmos realizar o seu empréstimo, precisamos das seguintes informações:") 

idade = int (input("Qual a sua idade? "))
salario = int (input ("Qual o seu salário? "))
anos_trabalho = int (input("Há quantos anos você trabalha? "))
emprestimo_pedido = float (input("Insira o valor do empréstimo que você pretende fazer: "))
tempo_pagar = int (input("Em quanto tempo você vai pagar pelo empréstimo? "))
parcela_emprestimo = emprestimo_pedido / tempo_pagar

# Regras Especiais
# Salario >= R$5000 (Aprovação Automatica)
# Idade <= 17 (Emprestimo Negado)
# Se a parcela comprometer mais de 30% da renda, o crédito é negado.


# Condicionais

if  idade >= 18:

    if  parcela_emprestimo < (salario * 0.30):
        
        if  salario >= 5000 and anos_trabalho >= 2:
            print ("Por conta da sua renda salarial ser igual ou maior que 5 mil reais, o seu empréstimo foi aprovado automáticamente. Parabéns e obrigado pela preferência!!")

        elif anos_trabalho <= 1:
            print("Infelizmente você não tem anos de trabalho suficiente para realizar um empréstimo conosco. Sentimos muito e até breve.")

        elif salario <= 1999:
            print("Infelizmente você não recebe salário o suficiente para realizar um empréstimo conosco. Sentimos muito e até breve.")

        elif salario >= 2000 and anos_trabalho >= 2:
            print("Empréstimo feito, obrigado pela preferência!")

    else:
        print("Infelizmente só podemos realizar um empréstimo com você, caso o valor de sua parcela não supere em 30% o seu salario atual. Sentimos muito e até breve.")
   
else:
    print("Infelizmente você não tem a idade minima necessária para realizar um empréstimo conosco. Sentimos muito e até breve.")

