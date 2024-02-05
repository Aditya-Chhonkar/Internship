#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
import pandas as pd 

def f1(string):
    newstring = re.sub(r'[ ,.]', ':', string)
    return newstring


# In[54]:


data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)


df['SUMMARY'] = df['SUMMARY'].str.replace(r'[^a-zA-Z\s]', '')

print(df)


# In[ ]:





# In[11]:


f1('Python Exercises, PHP exercises.')


# In[12]:


def f2(text):
    pattern = re.compile(r'\b\w{4,}\b')
    long_words = pattern.findall(text)
    return long_words


# In[14]:


f2("My name is Aditya")


# In[15]:


def f3(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    length_words = pattern.findall(text)
    return length_words


# In[17]:


f3("My name is Aditya and I am learning data scs")


# In[21]:


def f4(string):
    pattern = re.compile(r'\([^()]*\)')
    new_strings = [pattern.sub('', s) for s in string]
    return new_strings


# In[22]:


f4(["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"])


# In[23]:


def f5(text):
    pattern = re.compile(r'\s*\([^()]*\)\s*')
    newtext = pattern.sub('', text)
    return newtext

with open('sample_text.txt', 'r') as file:
    text = file.read()


newtext = remove_parentheses_area(text)

with open('sample_text_modified.txt', 'w') as file:
    file.write(modified_text)

print("Text with parentheses area removed and saved to 'sample_text_modified.txt'.")


# In[24]:


def f6(text):
    words = re.findall('[A-Z][^A-Z]*', text)
    return words

sample_text = "ImportanceOfRegularExpressionsInPython"
result = f6(sample_text)
print("Output:", result)


# In[25]:


def f7(text):
    modified_text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    return modified_text


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = f7(sample_text)
print("Output:", result)


# In[27]:


def f8(text):
    modified_text = re.sub(r'(?<=[A-Z\d])(?=[A-Z][a-z\d])', ' ', text)
    return modified_text


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = f8(sample_text)
print("Output:", result)


# In[28]:


url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)

df['first_five_letters'] = df['Country'].str[:5]

print(df.head())


# In[31]:


def f11(text):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    if pattern.match(text):
        return True
    else:
        return False


test_strings = ["Hello_World123", "123abc", "hello world", "Hello123_!"]
for string in test_strings:
    print(f"{string}: {f11(string)}")


# In[32]:


def f12(string, number):
    return string.startswith(str(number))


test_string = "123abc"
test_number = 123
print(f"Does '{test_string}' start with {test_number}? {f12(test_string, test_number)}")


# In[34]:


def f13(ip_address):
    components = ip_address.split('.')
    
    stripped_components = [str(int(component)) for component in components]
    
    modified_ip_address = '.'.join(stripped_components)
    
    return modified_ip_address

ip_address = "192.168.001.001"
modified_ip_address = f13(ip_address)
print("Modified IP address:", modified_ip_address)


# In[35]:


def f14(filename):
    with open(filename, 'r') as file:
        text = file.read()


    pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b')

    match = pattern.search(text)
    
    if match:
        return match.group()
    else:
        return None

filename = 'sample_text.txt'
date_string = f14(filename)
if date_string:
    print("Date string:", date_string)
else:
    print("Date string not found.")



# In[36]:


def f15(text, searched_words):
    found_words = []
    for word in searched_words:
        if word in text:
            found_words.append(word)
    return found_words


sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
found_words = f15(sample_text, searched_words)
print("Found words:", found_words)


# In[37]:


def f16(text, word):
    location = text.find(word)
    return location if location != -1 else None


sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'
word_location = f16(sample_text, searched_word)
if word_location is not None:
    print(f"The word '{searched_word}' is found at index:", word_location)
else:
    print(f"The word '{searched_word}' is not found in the text.")


# In[38]:


def f17(text, pattern):
    substrings = re.findall(pattern, text)
    return substrings


sample_text = 'Python exercises, PHP exercises, C# exercises'
search_pattern = 'exercises'
result = f17(sample_text, search_pattern)
print("Substrings found:", result)


# In[39]:


def f18(text, substring):
    occurrences = []
    start_position = 0
    while True:
        position = text.find(substring, start_position)
        if position == -1:
            break
        occurrences.append((substring, position))
        start_position = position + 1
    return occurrences


sample_text = 'Python exercises, PHP exercises, C# exercises'
search_substrings = ['exercises', 'PHP']
for substring in search_substrings:
    occurrences_positions = f18(sample_text, substring)
    if occurrences_positions:
        print(f"Occurrences of '{substring}':")
        for occurrence, position in occurrences_positions:
            print(f"  Found '{occurrence}' at position {position}")
    else:
        print(f"'{substring}' not found in the text.")


# In[40]:


from datetime import datetime

def f19(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    formatted_date = date_obj.strftime('%d-%m-%Y')
    
    return formatted_date

date_str = '2024-02-05'
formatted_date = f19(date_str)
print("Original date:", date_str)
print("Formatted date:", formatted_date)


# In[41]:


def f20(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)
    return decimal_numbers


sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
result = f20(sample_text)
print("Decimal numbers with precision of 1 or 2:", result)


# In[42]:


def f21(text):
    for index, char in enumerate(text):
        if char.isdigit():
            print(f"Character '{char}' found at position {index + 1}")

sample_text = "Hello 123 World"
print("Sample Text:", sample_text)
print("Numbers and their positions:")
f21(sample_text)


# In[43]:


def f22(text):
    numeric_values = re.findall(r'\d+', text)
    max_numeric_value = max(map(int, numeric_values))
    return max_numeric_value

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
result = f22(sample_text)
print("Maximum numeric value:", result)


# In[44]:


def f23(text):
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return modified_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = f23(sample_text)
print("Output:", result)


# In[45]:


text = "GhhhhstgnnhnKKKgggddhhdhdh"
pattern = re.compile(r'[A-Z][a-z]+')

matches = pattern.findall(text)
print(matches)


# In[47]:


def f25(text):
    modified_sentence = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    return modified_sentence


sample_text = "Hello hello world world"
result = f25(sample_text)
print("Output:", result)


# In[48]:


def f26(text):
    pattern = re.compile(r'^.*[a-zA-Z0-9]$')
    if pattern.match(text):
        return True
    else:
        return False

test_strings = ["Hello123", "Python!", "123456", "abc_", "test 123"]
for string in test_strings:
    print(f"{string}: {f26(string)}")


# In[50]:


def f27(text):
    pattern = re.compile(r'\#\w+')
    hashtags = pattern.findall(text)
    return hashtags


sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
result = f27(sample_text)
print("Extracted hashtags:", result)


# In[51]:


def f28(text):
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')
    cleaned_text = pattern.sub('', text)
    return cleaned_text


sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
result = f28(sample_text)
print("Cleaned text:", result)


# In[52]:


def f29(filename):
    with open(filename, 'r') as file:
        text = file.read()

    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')

    dates = pattern.findall(text)
    return dates

filename = 'sample_text.txt'
extracted_dates = f29(filename)
print("Extracted dates:", extracted_dates)


# In[53]:


def f30(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    modified_text = pattern.sub('', text)
    return modified_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result = f30(sample_text)
print("Output:", result)


# In[ ]:




