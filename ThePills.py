def contra(pri):
    if type(pri) == str and pri == "S" or type(pri) == str and pri == "s" or type(pri) == str and pri == "SIM" or type(pri) == str and pri == "Sim" or type(pri) == str and pri == "sim":
        print("Remédio não recomendado.")
        main()
    elif type(pri) == int and pri <8:
        print("Remédio não recomendado.")
        main() 


def sex(sex):
    if sex == "F" or sex == "Feminino" or sex == "feminino" or sex == "f":
        n = 1
    elif sex == "M" or sex == "Masculino" or sex == "masculino" or sex == "m":
        n = 2
    else:
        print("Sexo invalido")
        main()

    return n

def maior(id):
    if id < 18:
        n2 = 1
    else:
        n2 = 2

    return n2

def temp(pri):
    if pri >= 37 and pri < 37.9:
        calc = 1
    elif pri >= 38 and pri < 39.9:
        calc = 2
    elif pri >= 39.9:
        calc = 3
    else:
        print("Temperatura invalida")
        main()

    return calc
    
def full(pri,sec,ter):
    if pri == 1 and sec == 1 and ter == 1:
        div = 6
        return int(div)
    elif pri == 1 and sec == 1 and ter == 2:
        div = 4
        return int(div)
    elif pri == 1 and sec == 1 and ter == 3:
        div = 3
        return int(div)
    elif pri == 1 and sec == 2 and ter == 1:
        div = 4
        return int(div)
    elif pri == 1 and sec == 2 and ter == 2:
        div = 3
        return int(div)
    elif pri == 1 and sec == 2 and ter == 3:
        div = 2
        return int(div)
    elif pri == 2 and sec == 1 and ter == 1:
        div = 5
        return int(div)
    elif pri == 2 and sec == 1 and ter == 2:
        div = 4
        return int(div)
    elif pri == 2 and sec == 1 and ter == 3:
        div = 2
        return int(div)
    elif pri == 2 and sec == 2 and ter == 1:
        div = 4
        return int(div)
    elif pri == 2 and sec == 2 and ter == 2:
        div = 3
        return int(div)
    elif pri == 2 and sec == 2 and ter == 3:
        div = 1
        return int(div)

def calc_geral(pri,sec):
    result = pri // sec

    return result

def main():
    idade = int(input(f"Qual a idade do paciente?\n"))
    contra(idade)
    print("Digite apenas S (sim) e N (não).")
    diabetico =  input(f"O passiente é diabetico?\n")
    contra(diabetico)
    gravida = input(f"O paciente é gestante?\n")
    contra(gravida)
    peso = float(input(f"Qual o peso do paciente?\n"))
    temperatura = float(input(f"Qual a temperatura? \n"))
    sexo = input(f"Qual o sexo do paciente? (F/M)\n")

    calc = temp(temperatura)
    n = sex(sexo)
    n2 = maior(idade)
    div = float(full(n,n2,calc))

    result = round(calc_geral(peso,div))

    print(f"Devem ser tomados {result} gotas.")
    sair = int(input(f"Deseja sair do program?\n  1-Sim\n  2-Não\n"))
    if sair == 2:
        main()
    else:
        exit()

main()
