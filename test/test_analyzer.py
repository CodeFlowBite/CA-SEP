import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.text_analyzer import *

def test_count_words():
    texto = "This is a test."
    assert count_words(texto) == 4

def test_count_characters():
    texto = "This is a test."
    assert count_characters(texto) == 15

def test_count_sentences():
    texto = "This is a test. This is another test."
    assert count_sentences(texto) == 2

def test_count_paragraphs():
    texto = "This is a test.\n\nThis is another test."
    assert count_paragraphs(texto) == 2

def test_longest_word():
    texto = "This is a test."
    assert longest_word(texto) == "This" or longest_word(texto) == "test."

def test_longest_sentence():
    texto = "This is a test unique. This is another test."
    assert longest_sentence(texto) == "This is a test unique"

def test_longest_paragraph():
    texto = "This is a test.\n\nThis is another test."
    assert longest_paragraph(texto) == "This is another test."

if __name__ == "__main__":
    print("Running tests...")
    test_count_words()
    test_count_characters()
    test_count_sentences()
    test_count_paragraphs()
    test_longest_word()
    test_longest_sentence()
    test_longest_paragraph()
    print("All tests passed!")