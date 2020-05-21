from sanic import Blueprint

from .views import dic_list, get_word, get_word_by_dic

dic_bp_v1 = Blueprint('dictionary', url_prefix='/dictionary', version="v1")

dic_bp_v1.add_route(
    dic_list,
    '/',
    methods=["GET"]
)

dic_bp_v1.add_route(
    get_word_by_dic,
    '/<dictionary_id:int>/word/<name:string>/',
    methods=["GET"]
)

dic_bp_v1.add_route(
    get_word,
    '/word/<name:string>',
    methods=["GET"]
)
