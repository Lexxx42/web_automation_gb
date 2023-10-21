from typing import Annotated

from pytest import fixture

from login import get_post


def test_1(login: Annotated[str, fixture]):
    res = get_post(login)
    res_list = res.get('data')
    res_id_list = [item['id'] for item in res_list]
    assert 1234 in res_id_list, 'failed test1'
