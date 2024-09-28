from text_processing.word_count import wordCount
from text_processing.text_stats import count_sentences, count_paragraphs, average_word_length
from text_processing.string_operations import reverse_string, to_uppercase, to_lowercase, is_palindrome

text = str(input("Enter a text: "))

count = wordCount(text)

sentence_count = count_sentences(text)
paragraph_count = count_paragraphs(text)
avg_word_length = average_word_length(text)

rev_str = reverse_string(text)
upr_case = to_uppercase(text)
lwr_case = to_lowercase(text)
is_palin = is_palindrome(text)

print(f"\nNumber of words: {count}")

print(f"\nNumber of sentences: {sentence_count}")
print(f"Number of paragraphs: {paragraph_count}")
print(f"Average word length: {avg_word_length:.2f}")

print(f"\nOriginal String: {text}")
print(f"Reversed String: {rev_str}")
print(f"Uppercase String: {upr_case}")
print(f"Lowercase String: {lwr_case}")
print(f"Is Palindrome: {is_palin}")