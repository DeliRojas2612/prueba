






def main():
    SALARIO_MIN=1000000
    SUB_ALIM=120000
    SUB_TRANS=80000
    BONO = 50000
    nombre = input("digite nombre ")
    salario =int(input("digite salario ") )
    diastrabajados = int(input("digite dias trabajados ")  )
    sueldoapagar = calcularsueldo(salario,diastrabajados)
    if salario<(SALARIO_MIN * 2 ):
        sueldoapagar =sueldoapagar + SUB_ALIM + SUB_TRANS
    else:
        sueldoapagar = sueldoapagar + BONO

    print(f"mi nombre:  {nombre}  mi sueldo: {sueldoapagar:.0f}")


def calcularsueldo(sal , diast):
    
    sueldoapagar =(sal/30)*(diast)
    return sueldoapagar
    


if __name__=="__main__":
    main()


