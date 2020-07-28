"""
  @date 2020/7/27 11:04 下午
"""
__author__ = 'ilmostro'

from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import BizException
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def register():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        pormise = {
            ClientTypeEnum.EMAIL: __register_user_by_email
        }
        pormise[form.type.data]()
    else:
        raise BizException
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
