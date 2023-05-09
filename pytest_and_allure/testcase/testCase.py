#encoding=utf-8
import allure
import pytest
from pytest_and_allure.common.common1 import red_exc_lis,read_yaml

#类前置
@pytest.fixture(scope="class",autouse=True)
def my_class_fixture():
    print('类前置')
    yield
    print('类后置')

# 测试用例01
class TestCe:
    @pytest.mark.parametrize('student',read_yaml(yaml_name='data1.yaml'))
    def test_case0001(self, student):
            name = student['name']
            age = student['age']
            sex = student['sex']
            assert age <30

    # @allure.feature('信息模块allure.feature')
    # @allure.story('信息子模块—年龄模块allure.story')
    @allure.title('测试用例标题1----判断年龄allure.title')
    @allure.step('用例测试年龄2')
    @pytest.mark.parametrize('name,age', [['佳木斯',24], ['武学',36],['华盛顿',55]])
    def test_case0002(self,name,age):
        with allure.step('用例步骤：*1.输入姓名：{},*2.输入年龄：{},*3.开始判断年龄'.format(name,age)):
            assert age<40

    @pytest.mark.skip("这个用例跳过不执行，无条件跳过")
    def test_case0003(self):
        assert 1==1
        print("这个用例不执行的,无条件跳过")

    @pytest.mark.parametrize('school,address', [['佳木斯大学', '黑龙江省佳木斯市'], ['武汉大学', '湖北省武汉市'],['华盛顿大学','美国华盛顿州']])
    # @pytest.skipif(school='华盛顿大学',reason='不在中国')
    def test_case0004(self, school, address):
        print(school)
        print(address)
        assert '大学' in school and '美国' not in address

    @pytest.mark.parametrize('no_num,name,age',red_exc_lis('D:\\test_txt1.xls',0))
    def test_case0005(self,no_num,name,age):
        print("输出姓名---：%s" %name)
        print("输出年龄---：%s" % age)
        assert name != '白居易' and age >= 30

# 测试用例02
class TestNum:
    @pytest.fixture(scope='function',autouse=True)
    def my_function_fixture_(self):
        print("用例前置")
        yield
        print("用例后置")

    count_num = 20
    @pytest.mark.skipif(count_num<20,reason='小于20时跳过不执行')
    def test_case0007(self):
        print('007此时执行了，008就跳过了')
        assert 20==20

    @pytest.mark.skipif(count_num>=20,reason='大于等于20时跳过不执行')
    def test_case0008(self):
        print('008此时执行了，007就跳过了')
        assert 3==4

    def avg_numcase009(self):
        print('这个是默认时无法识别执行的')
        assert 2==4