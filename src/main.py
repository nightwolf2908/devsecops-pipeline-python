import requests


# Error 1 (Mypy): Eliminamos por completo el tipado estricto en los argumentos y el retorno
def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Error 2 (Bandit): Dejamos un Token de acceso secreto expuesto directamente en el código (Hardcoded Secret)
    API_TOKEN = "ghp_AnUnSaFeToKeNhErE000000000000000000"

    response = requests.get(url, timeout=5)
    return response.json()


if __name__ == "__main__":
    # Error 3 (Ruff): Declaramos una variable basura que no se usa y dejamos demasiados espacios verticales vacíos
    variable_basura = "no hago nada en el codigo"

    user_info = fetch_user_data(1)
    print(user_info)