import re
import nltk
from nltk.corpus import brown
from collections import Counter, defaultdict
nltk.download('brown')
nltk.download('punkt')

# ---------------- Q1. Preprocessing and Tokenization ----------------
def preprocess_brown_news():
    # Load news category
    sentences = brown.sents(categories='news')
    
    # Join words back to text
    text = " ".join([" ".join(sent) for sent in sentences])
    
    # Lowercasing
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize into sentences and words
    sent_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)
    
    # Report
    print("Q1. Report:")
    print("Total sentences:", len(sent_tokens))
    print("Total words:", len(word_tokens))
    print("Vocabulary size:", len(set(word_tokens)))
    
    return word_tokens

# ---------------- Q2. Building N-grams ----------------
def generate_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

def print_top_ngrams(tokens):
    bigrams = generate_ngrams(tokens, 2)
    trigrams = generate_ngrams(tokens, 3)
    
    bigram_counts = Counter(bigrams)
    trigram_counts = Counter(trigrams)
    
    print("\nQ2. Top 20 Bigrams:")
    for pair, count in bigram_counts.most_common(20):
        print(pair, ":", count)
    
    print("\nQ2. Top 20 Trigrams:")
    for trio, count in trigram_counts.most_common(20):
        print(trio, ":", count)
    
    return bigram_counts, trigram_counts

# ---------------- Q3. Conditional Probabilities ----------------
def bigram_prob(w1, w2, bigram_counts, unigram_counts):
    return bigram_counts.get((w1, w2), 0) / unigram_counts.get(w1, 1)

def trigram_prob(w1, w2, w3, trigram_counts, bigram_counts):
    return trigram_counts.get((w1, w2, w3), 0) / bigram_counts.get((w1, w2), 1)

# ---------------- Q4. Sentence Probability ----------------
def sentence_probability(sentence, unigram_counts, bigram_counts, trigram_counts, total_words):
    words = nltk.word_tokenize(sentence.lower())
    
    # Bigram model
    prob_bigram = 1.0
    for i in range(len(words)-1):
        prob_bigram *= bigram_prob(words[i], words[i+1], bigram_counts, unigram_counts)
    
    # Trigram model
    prob_trigram = 1.0
    for i in range(len(words)-2):
        prob_trigram *= trigram_prob(words[i], words[i+1], words[i+2], trigram_counts, bigram_counts)
    
    return prob_bigram, prob_trigram

# ---------------- MAIN EXECUTION ----------------
tokens = preprocess_brown_news()

# Unigrams
unigram_counts = Counter(tokens)

# Q2: Generate bigrams & trigrams
bigram_counts, trigram_counts = print_top_ngrams(tokens)

# Q3: Example conditional probabilities
print("\nQ3. Example Conditional Probabilities:")
print("P('the' | 'in') =", bigram_prob("in", "the", bigram_counts, unigram_counts))
print("P('of' | 'one', 'the') =", trigram_prob("one", "the", "of", trigram_counts, bigram_counts))

# Q4: Sentence probability
sentence = "the president of the company"
p_bigram, p_trigram = sentence_probability(sentence, unigram_counts, bigram_counts, trigram_counts, len(tokens))

print("\nQ4. Sentence Probability:")
print("Sentence:", sentence)
print("Bigram Model Probability:", p_bigram)
print("Trigram Model Probability:", p_trigram)
