#Instructions
#Create an empty list named misspelled_words.
#Write a for loop that:
#iterates over tokenized_story,
#uses an if statement that returns True if the current token is not in tokenized_vocabulary and if so, appends the current token to misspelled_words.
#Print misspelled_words.

#In this code, we're going to explore how to build a basic spell checker. Spell checkers work by comparing each word in a passage of text to a set of correctly spelled words. In this mission, we will learn:

#how to work with plain text files to read in a vocabulary of correctly spelled words,
#more string methods for working with and processing text data,
#how to create functions to make the components of our spell checker more reusable.


def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)
