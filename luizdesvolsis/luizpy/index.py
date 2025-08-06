from quarto import Quarto
quarto1 = Quarto(101, "Casal", 200.00, True)
quarto1.exibir_detalhes()
quarto1.reservar()
quarto1.exibir_detalhes()
quarto1.liberar()
quarto1.alterar_preco(250.00)
quarto1.exibir_detalhes()