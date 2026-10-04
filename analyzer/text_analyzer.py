
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

if __name__ == "__main__":
    sample_text = """"
    This is a sample text. It contains multiple sentences. And even multiple paragraphs.
    
    This is the second paragraph. It also has sentences.

    This is the third paragraph. It has sentences too.
    """
    print(f"Word count: {count_words(sample_text)}")
    print(f"Character count: {count_characters(sample_text)}")
    print(f"Sentence count: {count_sentences(sample_text)}")
    print(f"Paragraph count: {count_paragraphs(sample_text)}")