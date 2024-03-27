pesoPayaso = 112
pesoMunheca = 75

pedidoPayasos = int(input("Digite la cantidad de payasos a comprar: "))
pedidoMunhecas = int(input("Digite la cantidad de muñecas a comprar: "))

pesoTotalPedidoPayasos = pedidoPayasos*pesoPayaso
pesoTotalPedidoMunhecas = pedidoMunhecas*pesoMunheca
pesoTotalPedido = (pesoTotalPedidoPayasos + pesoTotalPedidoMunhecas)/1000

print("El peso total del último pedido es: ", pesoTotalPedido, "Kg")