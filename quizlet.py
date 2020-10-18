from requests_html import HTMLSession
from box import Box
import box
import json
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def FindFlashcard(flashcards: box.box_list.BoxList, match: str):
    similar = lambda a, b: SequenceMatcher(None, a, b).ratio()
    data = max(list(zip([similar(match, x.term) for x in flashcards], [x for x in range(len(flashcards))])))
    flashcard = flashcards[data[1]]
    flashcard.update({'similarity': data[0]})
    return flashcard

def QuizletParser(link: str):
    session = HTMLSession()
    data = json.loads(BeautifulSoup(session.get(link).content, features="lxml").find_all('script')[-6].string[44:-152])
    flashcards = []
    for i in list(data['termIdToTermsMap'].values()):
        i = {
            'index': i['rank'],
            'id': i['id'],
            'term': i['word'],
            'definition': i['definition'],
            'setId': i['setId'],
            'image': i['_imageUrl'],
            'termTts': 'https://quizlet.com'+i['_wordTtsUrl'],
            'termTtsSlow': 'https://quizlet.com'+i['_wordSlowTtsUrl'],
            'definitionTts': 'https://quizlet.com'+i['_definitionTtsUrl'],
            'definitionTtsSlow': 'https://quizlet.com'+i['_definitionSlowTtsUrl'],
            'lastModified': i['lastModified'],
        }
        flashcards.append(i)

    output = {
        'title': data['set']['title'],
        'flashcards': flashcards,
        'author': {
            'name': data['creator']['username'],
            'id': data['creator']['id'],
            'timestamp': data['creator']['timestamp'],
            'lastModified': data['creator']['lastModified'],
            'image': data['creator']['_imageUrl'],
            'timezone': data['creator']['timeZone'],
            'isAdmin': data['creator']['isAdmin'],
        },
        'id': data['set']['id'],
        'link': data['set']['_webUrl'],
        'thumbnail': data['set']['_thumbnailUrl'],

        'timestamp': data['set']['timestamp'],
        'lastModified': data['set']['lastModified'],
        'publishedTimestamp': data['set']['publishedTimestamp'],
        'authorsId': data['set']['creatorId'],
        'termLanguage': data['set']['wordLang'],
        'definitionLanguage': data['set']['defLang'],
        'description': data['set']['description'],
        'numTerms': data['set']['numTerms'],
        'hasImages': data['set']['hasImages'],
        'hasUploadedImage': data['hasUploadedImage'],
        'hasDiagrams': data['set']['hasDiagrams'],
        'hasImages': data['set']['hasImages'],

    }
    return Box(output)