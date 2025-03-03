# 🚀 Exercício 4: Dado o seguinte arquivo no formato JSON,
# leia seu conteúdo e calcule a porcentagem de livros em cada categoria
# em relação ao número total de livros. O resultado deve ser
# escrito em um arquivo no formato CSV como o exemplo abaixo.

# Saída:

# categoria,porcentagem
# Python,0.23201856148491878
# Java,0.23201856148491878
# PHP,0.23201856148491878

# PS: O percentual do exemplo acima esta errado, simplesmente pelo fato
# de que as pessoas fingem que não precisamos de matematica
# na programação =/

import json
import csv


def retrieve_books(file):
    return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def calculate_percentage_by_category(book_count_by_category, total_books):
    return [
        [category, round(((num_books * 100) / total_books), 2)]
        for category, num_books in book_count_by_category.items()
    ]


def write_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    # retrieve books
    with open("./exercicios-bloco/inputs/books.json", mode="r") as file:
        books = retrieve_books(file)

    # count by category
    book_count_by_category = count_books_by_categories(books)

    # calculate percentage
    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
        book_count_by_category, number_of_books
    )

    # write csv
    header = ["categoria", "percentagem"]
    with open("./exercicios-bloco/inputs/books_report.csv", mode="w") as file:
        write_csv_report(file, header, books_percentage_rows)
