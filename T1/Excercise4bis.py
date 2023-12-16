import re
from collections import Counter

def count_words(text):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word using Counter
    word_counts = Counter(words)
    
    return word_counts

# Example usage:
if __name__ == "__main__":
    input_text = str(input(" Text: "))
    
    word_counts = count_words(input_text)
    
    # Print the word counts
    for word, count in word_counts.items():
        print(f"'{word}': {count}")
