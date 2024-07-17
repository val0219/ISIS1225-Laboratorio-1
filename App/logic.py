"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import config as cf
import os
import csv
from DataStructures import set as set
assert cf

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_logic():
    """
    Inicializa el catálogo de libros. Crea un conjunto vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {
        "books": None,
        "tags": None,
        "book_tags": None,
    }

    # definicion de arreglos
    catalog["books"] = set.new_set()
    catalog["tags"] = set.new_set()
    catalog["book_tags"] = set.new_set()
    return catalog


# Funciones para la carga de datos

def load_books(app, filename):
    """
    Carga los libros del archivo. Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    books = app.get("books")
    booksfile = os.path.join(cf.data_dir, filename)
    app["books"] = set.load_set(books, booksfile)
    if empty_books(app):
        return None
    else:
        return book_size(app)


def load_tags(app, filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tags = app.get("tags")
    tagsfile = os.path.join(cf.data_dir, filename)
    app["tags"] = set.load_set(tags, tagsfile)

    if set.is_empty(tags):
        return None
    else:
        return set.size(tags)


def load_books_tags(control, filename):
    """
    Carga los tags de los libros del archivo y los agrega a la lista
    de tags. Siga el mismo procedimiento que en la carga de libros.
    """
    # TODO: Mods Lab 1, integrar vista y modelo
    pass

# Funciones de consulta


def book_size(catalog):
    return set.size(catalog["books"])


def tag_size(catalog):
    return set.size(catalog["tags"])


def book_tag_size(catalog):
    return set.size(catalog["book_tags"])


def empty_books(catalog):
    books = catalog.get("books")
    return set.is_empty(books)


def empty_tags(catalog):
    tags = catalog.get("tags")
    return set.is_empty(tags)


def empty_book_tags(catalog):
    book_tags = catalog.get("book_tags")
    return set.is_empty(book_tags)
