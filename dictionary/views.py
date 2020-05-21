from sanic.response import json


async def dic_list(request):
    """ return list of available dictionaries """
    return json({})


async def get_word_by_dic(request, dictionary_id, word):
    """ return list of words filtered by dictionary """
    return json({"return": "/<dictionary_id:int>/word/<word:string>/"})


async def get_word(request, word):
    """ return list of words """
    return json({"return": "/word/<word:string>"})
