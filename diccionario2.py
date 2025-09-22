import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Hábitos Atómicos",
        "autor": ["James Clear"],
        "géneros": ["Autoayuda", "Hábitos de identidad"]
    },
    "978-84-204-1625-5": {
        "título": "Pedro Páramo",
        "autor": ["Juan Rulfo"],
        "géneros": ["Novela de realismo mágico", "Ficción"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)