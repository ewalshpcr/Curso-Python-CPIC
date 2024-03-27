precioBarraDePan = 3.49
descuentoBarraDePanAnhejo = 0.60
precioBarraDePanAnhejo = precioBarraDePan - (precioBarraDePan*descuentoBarraDePanAnhejo)

barrasDePanAnhejo = int(input("Digite la cantidad de barras de pan añejo que desea: "))

print(f"""Precio del pan del día es: {precioBarraDePan}€, 
          precio del pan añejo es {round(precioBarraDePanAnhejo, 2)}€ (60% de descuento), 
          precio total de la compra es: {round(barrasDePanAnhejo*precioBarraDePanAnhejo, 2)}€""")