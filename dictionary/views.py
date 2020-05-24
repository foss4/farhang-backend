from utils.decorators import cache

from .models import Word
from .repository import DictionaryRepositoryInstance, WordRepositoryInstance


@cache
async def dic_list(request):
    """ return list of available dictionaries """
    results = await DictionaryRepositoryInstance.get_all_dictionaries(
        request.app.pool
    )
    return [
        {
            "id": key,
            "name": value
        } for key, value in dict(results).items()
    ]


@cache
async def get_word_by_dic(request, dictionary_id, name):
    """ return list of words filtered by dictionary """
    word = Word(name=name, dictionary=dictionary_id)
    results = await WordRepositoryInstance.find_by_name_and_dictionary(
        word,
        request.app.pool
    )
    return [
        {
            "name": item["name"],
            "meaning": item["meaning"],
            "dictionary": item["fa_name"]
        } for item in results
    ]


@cache
async def get_word(request, name):
    """ return list of words """
    word = Word(name=name)
    results = await WordRepositoryInstance.find_by_name(
        word,
        request.app.pool
    )
    return [
        {
            "name": item["name"],
            "meaning": item["meaning"],
            "dictionary": item["fa_name"]
        } for item in results
    ]
