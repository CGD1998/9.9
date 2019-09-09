from flask import jsonify
from first import app

from helper import is_isbn_or_key
from yushu_book import YuShuBook

print('id为'+str(id(app))+'的app路由注册')

@app.route('/book/search/<q><page>')
def search(q, page):
    """
    q:普通关键字 or isbn(一组数字）--如何鉴别
    page:strat count
    :return:
    """
    # isbn13 13个0-9的数字组合
    # isbn10 不怎么用，含有一些' _'

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)

