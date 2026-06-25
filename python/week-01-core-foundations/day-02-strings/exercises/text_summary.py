# ==================================================================================
# Text Summary - Analyzes a paragraph of text, counts characters and words,
# searches for a specific keyword, and generates a truncated preview.
# ==================================================================================

print("\n==========================================")
print("          TEXT PREVIEW & ANALYZER         ")
print("==========================================\n")

# Get raw paragraph input and search keyword
raw_text = input("Enter your paragraph: ")
search_word = input("Enter a keyword to search for: ").strip()

# Clean the text and counts
text = raw_text.strip()
char_count = len(text)
word_count = len(text.split())

# check capitalization and keyword occurrences
is_starts_with_capital = text[0].isupper()
keyword_count = text.lower().count(search_word.lower())
is_contains_keyword = keyword_count > 0

# Extract a 35 character preview with "..."
preview = text[:35] + "..."

# Print the metrics and preview
print("\n" + "=" * 45)
print("                TEXT METRICS              ")
print("=" * 45)

print(f"Original Characters: {char_count}")
print(f"Word Count:          {word_count}")
print(f"Starts with Capital: {is_starts_with_capital}")
print(f"Keyword '{search_word}' Count: {keyword_count} (Found: {is_contains_keyword})")
print("-" * 45)
print(f"Text Preview:\n{preview}")

print("=" * 45 + "\n")