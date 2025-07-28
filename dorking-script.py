from googlesearch import search

# Consulta que se quiere buscar
query = "site:.com inurl:admin login AND user"

# Realizamos la búsqueda con google
for url in search(query, num_results=10):  # 'num_results' especifica cuántos resultados queremos
    print(url)
