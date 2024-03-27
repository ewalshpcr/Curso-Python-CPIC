interesAnual = (4/100)
montoADepositar = float(input("Digite el monto de dinero a depositar en la cuenta de ahorro: "))

print(f"""Los ahorros del primer año son: {montoADepositar + (montoADepositar*interesAnual)}, 
          del segundo año son: {montoADepositar + ((montoADepositar*interesAnual)*2)} 
          y del tercer año son: {montoADepositar + ((montoADepositar*interesAnual)*3)}""")