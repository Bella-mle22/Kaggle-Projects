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

#In this code, we're going to explore how to customize the functions we write to improve the spell checker we built from the previous mission. As our code becomes more modular and separated into functions, it can often become harder to debug. We'll explore how to debug our code in this mission using the errors the Python interpreter returns.

#Recall that our spell checker works by:

#reading in a file of correctly spelled words, tokenizing it into a list and assigning it to the variable vocabulary,
#reading in, cleaning, and tokenizing the piece of text we want spell checked,
#comparing each word (token) in the piece of text with each word in vocabulary and returning the ones that weren't found.
#The file dictionary.txt contains a sequence of correctly spelled words, which we'll use to seed the vocabulary. The file story.txt is a piece of text containing some misspelled words. In the following code cell, we added the spell checker we wrote so far from the previous mission.


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


#Instructions
#Modify the tokenize() function:



def tokenize(text_string, special_characters, clean=False):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
#Use an if statement to check if clean is True. If so:
     #Clean text_string using clean_text and assign the returned string to a variable.
     #Tokenize this new string variable using the split() method and assign the returned list to a variable.
     #Return this list.
# Answer code
def tokenize(text_string, special_characters, clean=False):
    # If `clean` is `True`.
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    #Outside the if statement, write the code that's executed if clean is False:
    #Tokenize text_string using the split() method and assign the returned list to a variable.
    #Return this list.
    # If `clean` not equal to `True`, no cleaning.
    story_tokens = text_string.split(" ")
    return(story_tokens)
#Outside the tokenize() function:
#Use the tokenize() function to clean and tokenize story_string and assign the result to tokenized_story.
#Use the tokenize() function to tokenize vocabulary and assign the result to tokenized_vocabulary.
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
#Finally, loop over in tokenized_story, check if each element is in tokenized_vocabulary, and add to misspelled_words if it isn't.
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
