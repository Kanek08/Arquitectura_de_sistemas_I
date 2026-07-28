import requests

url = "https://pokeapi.co/"

try:
    respuesta = requests.get(url)

    print("====== METADATOS DE LA RESPUESTA ======\n")

    print("1. Código de estado:")
    print(respuesta.status_code)

    print("\n2. Headers:")
    for clave, valor in respuesta.headers.items():
        print(f"{clave}: {valor}")

    print("\n3. Body:")
    print(respuesta.text)

    print("\n4. Tiempo de respuesta:")
    print(respuesta.elapsed)

except requests.exceptions.RequestException as e:
    print("Error:", e)