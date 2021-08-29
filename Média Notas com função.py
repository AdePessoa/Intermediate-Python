# o usuário deverá digitar duas notas para o aluno. Na sequência, o programa irá calcular e exibir a média, 
# #informando se o aluno está aprovado (média maior ou igual a 7.0) ou reprovado.
def lernotas():
    n = float(input("Digite uma nota para o aluno: "))
    return n

def resultado (n1,n2):
    media = (n1+n2)/2
    print ("Nota 1: {}".format(n1))
    print ("Nota 2: {}".format(n2))
    print ("Média: {}".format(media) + "  ===>>  " + "Resultado: ", end="")
    if media >= 7:
        print ("Aprovado!")
    else:
        print ("Reprovado.")
        
a = lernotas ()
b = lernotas ()
resultado (a,b)