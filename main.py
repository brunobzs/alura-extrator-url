# url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = " "

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

# Separa base e os parâmentros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_paramentros = url[indice_interrogacao+1:]
print(url_paramentros)

# Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_paramentro = url_paramentros.find(parametro_busca)
indice_valor = indice_paramentro + len(parametro_busca) + 1
indice_e_comercial = url_paramentros.find('&',indice_valor)
if indice_e_comercial == -1:
    valor = url_paramentros[indice_valor:]
else:
    valor = url_paramentros[indice_valor:indice_e_comercial]
print(valor)