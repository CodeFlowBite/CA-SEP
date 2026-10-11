from analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    longest_word,
    longest_sentence,
    longest_paragraph
)

texto = """
Esto es un texto de prueba. Contiene varias oraciones y párrafos.
El objetivo es probar las funciones del analizador de texto. Cada función debe contar correctamente las palabras, caracteres, oraciones y párrafos. Además, debe identificar la palabra más larga, la oración más larga y el párrafo más largo.

Este es el segundo párrafo. 

La prueba debe ser exhaustiva para garantizar la precisión de los resultados.
"""

print("Número de palabras:", count_words(texto))
print("Número de caracteres:", count_characters(texto))
print("Número de oraciones:", count_sentences(texto))
print("Número de párrafos:", count_paragraphs(texto))
print("Palabra más larga:", longest_word(texto))
print("Oración más larga:", longest_sentence(texto))
print("Párrafo más largo:", longest_paragraph(texto))
