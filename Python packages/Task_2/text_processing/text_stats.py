def count_sentences(text):
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count

def count_paragraphs(text):
    paragraphs = text.split('\n')
    return len([p for p in paragraphs if p.strip()])

def average_word_length(text):
    words = text.split()
    if len(words) == 0:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)