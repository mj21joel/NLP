import re

# 1. Extract domain names (not full URL)
def extract_domains(text):
    return re.findall(r'https?://(?:www\.)?([\w.-]+\.\w+)', text)
print("1. Domains:", extract_domains("Visit https://www.iitbhu.ac.in for details."))

# 2. Extract Gmail and Yahoo emails
def extract_emails(text):
    return re.findall(r'[\w\.-]+@(gmail\.com|yahoo\.com)', text)
print("2. Emails:", extract_emails("Send updates to abc123@yahoo.com and x.y.z@gmail.com"))

# 3. Find hashtags (with digits/underscores)
def extract_hashtags(text):
    return re.findall(r'#\w+', text)
print("3. Hashtags:", extract_hashtags("Today's highlights: #IndvsPak_2025 #Go_India #Cricket123"))

# 4. Extract Twitter mentions (ignore extra characters)
def extract_mentions(text):
    return re.findall(r'@\w+', text)
print("4. Mentions:", extract_mentions("@dr_singh! you were amazing @Minister@India"))

# 5. Extract decimal numbers
def extract_numbers(text):
    return re.findall(r'\d+\.\d+|\d+', text)
print("5. Numbers:", extract_numbers("The price increased from 45.60 to 99.99 in 3 days"))

# 6. Extract all special characters
def extract_special_chars(text):
    return re.findall(r'[^a-zA-Z0-9\s]', text)
print("6. Special Chars:", extract_special_chars("Whoa!! COVID-19 has changed the world @2020 #History"))

# 7. Validate vehicle registration numbers (AA11BB1234 format)
def validate_vehicle_number(number):
    return bool(re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', number))
print("7. Vehicle Number Valid:",
      validate_vehicle_number("UP32GH1234"), validate_vehicle_number("up32gh1234"))

# 8. Normalize repeated characters
def normalize_repeated(text):
    return re.sub(r'(.)\1+', r'\1', text)
print("8. Normalized Text:", normalize_repeated("Ammmaaazing wooorrrkkk!!!"))

# 9. Find 10-digit mobile numbers (starting with 6–9, preceded by + or 0)
def extract_mobile_numbers(text):
    return re.findall(r'(?:\+91|0)[6-9]\d{9}', text)
print("9. Mobile Numbers:", extract_mobile_numbers("Call me at +919990001234 or 09990004567"))

# 10. Extract proper nouns (capitalized words not at start of sentence)
def extract_proper_nouns(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    proper_nouns = []
    for sent in sentences:
        words = sent.split()
        if len(words) > 1:
            for word in words[1:]:
                if word.istitle():
                    proper_nouns.append(word)
    return proper_nouns
print("10. Proper Nouns:", extract_proper_nouns("Delhi is the capital of India. Narendra Modi is the Prime Minister."))


