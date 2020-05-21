from sanic.response import json

from .models import Word
from .repository import DictionaryRepositoryInstance, WordRepositoryInstance


async def dic_list(request):
    """ return list of available dictionaries """
    results = await DictionaryRepositoryInstance.find_by_name_and_dictionary(
        request.app.config.get("pool")
    )
    return json(dict(results))


async def get_word_by_dic(request, dictionary_id, name):
    """ return list of words filtered by dictionary """
    word = Word(name=name, dictionary=dictionary_id)
    results = await WordRepositoryInstance.find_by_name_and_dictionary(
        word, request.app.config.get("pool")
    )
    return json(dict(results))


async def get_word(request, name):
    """ return list of words """
    word = Word(name=name)
    results = await WordRepositoryInstance.find_by_name_and_dictionary(
        word,
        request.app.config.get("pool")
    )
    return json(dict(results))
