# Quizlet API
This is a python API for fetching data from quizlet.
To install this api, simply add the `quizlet.py` file to your project.

---

## Requirements:
```
requests-html
python-box
beautifulsoup4
```

---

## Usage:

#### Here is an example of the quizlet api being used in python 3:
```py
>>> from quizlet import QuizletParser
>>> q = QuizletParser('https://quizlet.com/158478531/python-flash-cards/')
>>> q.title # returns the title
'python'
>>> q.description # returns the quizlet description
'python test 1 computer science'
```
Getting author information:
```py
>>> q.author.name # author's username
'Steven_Howard11'
>>> q.author.image # author's profile picture
'https://gimg.quizlet.com/-iEEBpKVXBvA/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclm4enq4MrgowWWFPaoKADePHvjMw/photo.jpg?sz=150'
>>> q.author.timeZone # author's timezone
'America/New_York'
```
Getting a flashcard
```py

>>> q.flashcards[0].term # gets the first flashcard's term 
'algorithm'
>>> q.flashcards[0].defintion # gets the first flashcard's definition
'A set of specific steps for solving a category of problems'
```

<hr width=50>

#### Searching for flashcards:

```py
>>> from quizlet import QuizletParser, FindFlashcard
>>> q = QuizletParser('https://quizlet.com/158478531/python-flash-cards/')
>>> flashcard = FindFlashcard(q.flashcards, match='Programs are commonly referred to as')  # finds the flashcard most similar to the input
>>> flashcard.similarity  # calculates how similar the identified flashcard is to the input
1.0
>>> flashcard.term  # gets the identified term
'Programs are commonly referred to as'
>>> flashcard.defintion  # gets the identified definition
'software'
```

---

# Objects:

- [`QuizletParser(link)`](https://github.com/daijro/python-quizlet#quizletparserlink-str)
- [`QuizletParser(link).author`](https://github.com/daijro/python-quizlet#quizletparserlinkauthor)
- [`QuizletParser(link).flashcards`](https://github.com/daijro/python-quizlet#quizletparserlinkflashcards)
- [`FindFlashcard(flashcards, match)`](https://github.com/daijro/python-quizlet#findflashcardflashcards-list-match-str)

<hr width=100>

## `QuizletParser(link: str)`

Core developer interface for python-quizlet.

<hr width=70>

#### `.title`

Get the quizlet set title

*Return type:	`str`*

<hr width=30>

#### `.description`

Get the quizlet set description

*Return type:	`str`*

<hr width=30>

#### `.id`

Get the quizlet set description

*Return type:	`int`*

<hr width=30>

#### `.thumbnail`

Get the quizlet set thumbnail URL

*Return type:	`str` (returns `NoneType` when thumbnail is not avaliable)*
<hr width=30>

#### `.numTerms`

Get the amount of flashcards in the set

*Return type:	`int`*

<hr width=30>

#### `.hasImages`

Gets if or if there is not images in the quizlet set

*Return type:	`bool`*

<hr width=30>

#### `.hasUploadedImage`

Gets if or if there is not uploaded images in the quizlet set

*Return type:	`bool`*

<hr width=30>

#### `.hasDiagrams`

Gets if or if there is not diagrams in the quizlet set

*Return type:	`bool`*

<hr width=30>

#### `.timestamp`

Get the timestamp for the quizlet set

*Return type:	`int`*

<hr width=30>

#### `.lastModified`

Get the timestamp for when the quizlet set was last modified

*Return type:	`int`*

<hr width=30>

#### `.publishedTimestamp`

Get the timestamp for when the quizlet set was published

*Return type:	`int`*

<hr width=30>

#### `.authorsId`

Get the author's ID


*Return type:	`int`*

<hr width=30>

#### `.termLanguage`

Get the language that the terms are written in (English is "en")

*Return type:	`str`*

<hr width=30>

#### `.definitionLanguage`

Get the language that the defintions are written in (English is "en")

*Return type:	`str`*

<hr width=30>

## `QuizletParser(link).author`

Gets the quizlet set's author's data

<hr width=70>

#### `.author.name`

Get the username of the author

*Return type:	`str`*

<hr width=30>

#### `.author.id`

Get the user ID of the author

*Return type:	`int`*

<hr width=30>

#### `.author.timestamp`

Get the timestamp of the author's account

*Return type:	`int`*

<hr width=30>

#### `.author.lastModified`

Get the timestamp of when the author's account was last modified

*Return type:	`int`*

<hr width=30>

#### `.author.image`

Gets the author's profile picture URL

*Return type:	`str`*

<hr width=30>

#### `.author.image`

Gets the author's profile picture URL

*Return type:	`str`*

<hr width=30>

#### `.author.timezone`

Gets the timezone of the author

*Return type:	`str`*

<hr width=30>

#### `.author.isAdmin`

Gets if or if not the author is a quizlet admin

*Return type:	`bool`*

<hr width=30>

## `QuizletParser(link).flashcards`

Documentation for how to use the flashcard items

<hr width=70>

#### `.flashcards[index].index`

Gets the index of the flashcard in the list

*Return type:	`int`*

<hr width=30>

#### `.flashcards[index].id`

Gets the id of the flashcard

*Return type:	`int`*

<hr width=30>

#### `.flashcards[index].term`

Gets the quizlet flashcard term/question

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].definition`

Gets the quizlet flashcard definition/answer

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].setId`

Gets the ID of the quizlet set

*Return type:	`int`*

<hr width=30>

#### `.flashcards[index].image`

If there is an image, return the image URL

*Return type:	`str` (returns `NoneType` when image is not avaliable)*

#### `.flashcards[index].termTts`

Gets the text-to-speech URL for the term/question

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].termTtsSlow`

Gets the slower text-to-speech URL for the term/question

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].definitionTts`

Gets the text-to-speech URL for the definition/answer

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].definitionTtsSlow`

Gets the slower text-to-speech URL for the definition/answer

*Return type:	`str`*

<hr width=30>

#### `.flashcards[index].lastModified`

Gets when the flashcard was last modified

*Return type:	`int`*

<hr width=30>

## `FindFlashcard(flashcards: list, match: str)`

Documentation for how to use the flashcard searcher

<hr width=70>

The `FindFlashcard(flashcards, match)` function will simply return a `QuizletParser(link).flashcards` object, but with an added `.similarity` to show how similar identified flashcard is to the match input.


#### `.similarity`
Returns how similar the identified term is to the `match`.

*Return type:	`float`*
