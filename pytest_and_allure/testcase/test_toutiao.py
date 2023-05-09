#encoding=utf-8
import json
import allure
import pytest
from pytest_and_allure.common.common1 import red_exc_lis
# from py_unittest_ddt_request.base.base_page import Req_class

@allure.feature('头条')
class Test_toutiao:
    @pytest.mark.parametrize('a,b,c,d,e,f,g,h,i,j,k',red_exc_lis('D:\\api_data.xls',0))
    @allure.title('头条接口用例')
    def test_toutiao_api(self,a,b,c,d,e,f,g,h,i,j,k):
        allure.dynamic.description('标题：'+b+'\n预期：'+h)
        with allure.step('用例描述：{}这是自定义的用例简述'.format(b)):
            print(a,b)
            assert 'success' in h or len(g)>0
            # my_header = {
            #     'User-Agent': 'Apache-HttpClient/4.5.13 (Java/1.8.0_131)',
            #     'Content-Type': 'application/json'
            # }
            # print(a[5])
            # self.sq = Req_class().requests_type(method=e,data=json.dumps(g),headers=my_header,url=f)
            # assert h in self.sq.text
    def test_other(self):
        pass

# if __name__ == '__main__':
#     pytest.main(['-sv',])
