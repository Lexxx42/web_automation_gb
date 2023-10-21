from typing import Annotated

from pytest import fixture

from login import get_my_posts


def test_1(login: Annotated[str, fixture]):
    res = get_my_posts(login)
    print(res)
    res_list = res.get('data')
    print(res_list)
    res_id_list = [item['id'] for item in res_list]
    assert 1234 in res_id_list, 'failed test1'
