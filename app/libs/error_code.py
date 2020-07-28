"""
  @date 2020/7/28 11:32 下午
"""
__author__ = 'ilmostro'

from werkzeug.exceptions import HTTPException


class BizException(HTTPException):
    code = 400
    description = (
        'client is invalid!'
    )