
def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> int:
    return len(text)

def count_sentences(text: str) -> int:
    sentence = text.split('.')
    sentence = [s for s in sentence if s.strip()]
    return len(sentence)

def count_paragraphs(text: str) -> int:
    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]
    return len(paragraphs)

def longest_word(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def longest_sentence(text: str) -> str:
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return ""
    return max(sentences, key=len)

def longest_paragraph(text: str) -> str:
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    if not paragraphs:
        return ""
    return max(paragraphs, key=len)
