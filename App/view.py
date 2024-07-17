"""
 * Copyright 2024, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import sys
import logic
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
dataFolder = "GoodReads"


def new_logic():
    """
    Se crea una instancia de la aplicacion
    """
    app = logic.new_logic()
    return app


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    # TODO: Mods Lab 1, agregar la opcion 3.

    print("0- Salir")


def load_books(app):
    """
    Carga los libros
    """
    books = logic.load_books(app,
                             "GoodReads/books-small.csv")
    return books


def load_tags(app):
    """
    Carga los Tags
    """
    tags = logic.load_tags(app,
                           "GoodReads/tags.csv")
    return tags


def load_books_tags(app):
    """
    Cargar los Tags de libros
    """
    booksTags = logic.load_books_tags(app,
                                      "GoodReads/book_tags-small.csv")
    return booksTags


# Se crea la controlador asociado a la vista
app = new_logic()

# main del ejercicio
if __name__ == "__main__":

    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        printMenu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            print("Cargando información de libros....")
            books = load_books(app)
            print("Total de libros cargados: " + str(books) + "\n")

        elif int(inputs[0]) == 2:
            print("Cargando información de tags....")
            tags = load_tags(app)
            print("Total de tags cargados: " + str(tags) + "\n")

        # TODO: Mods Lab 1, agregar la funcion opt 3 -> ladBookTags().
        elif int(inputs[0]) == 3:
            pass

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
