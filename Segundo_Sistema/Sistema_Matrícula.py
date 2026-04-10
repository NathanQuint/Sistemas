# Regras Especiais
## Nota >= 9 (Aprovação automática)
## Idade <18 (Negação automática)

idade = int(input("Qual a sua idade? "))
nota_prova = float(input("Qual foi sua nota? " ))
frequencia = int(input("Qual a sua porcentagem de frequência escolar? "))

#Condicionais

if  idade >= 18:
    
    if nota_prova >=9 and frequencia >= 75:
        print("Matrícula Aprovada automáticamente!")

    elif nota_prova >= 6 and frequencia >= 75:
        print("Matrícula aprovada.")
    
    elif frequencia < 75:
        print("Você não apresenta a frequência minima necessária.")
    
    elif nota_prova < 6:
        print("Você não tem a nota minima necessária.")
else:
    print("Você não tem a idade minima necessária, negação automatica.")

    


