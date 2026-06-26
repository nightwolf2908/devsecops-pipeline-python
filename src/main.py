from typing import Any

import requests


# Ahora especificamos que es un dict con llaves str y valores Any
def fetch_user_data(user_id: int) -> dict[str, Any]:
    """Simula la obtención de datos de un usuario desde una API externa."""
    url: str = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        # También tipamos la variable interna
        data: dict[str, Any] = response.json()
        return data
    return {}


if __name__ == "__main__":
    user_info = fetch_user_data(1)
    if user_info:
        print(f"Usuario encontrado: {user_info.get('name')}")
    else:
        print("No se pudo obtener la información del usuario.")
