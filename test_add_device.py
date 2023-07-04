import allure
import pytest

from project.device import Device
import logging as logger

@allure.feature("设备的增删改查")
class Testadddevice:

    def setup (self):
        self.device = Device()

    def tearDown(self):
        #关闭会话
        self.session.close()

    @allure.title("新建设备")
    @pytest.mark.parametrize('name,label,description',[
        ['yjy1','test _tag','test1'],
        ['yjy2', 'test _tag','test2'],
        ['yjy3', 'test _tag','test3'],
        # ['yjy4', 'test _tag','test2'],
        # ['yjy5', 'test _tag','test2']
                             ])
    def test_add_device(self,name,label,description):

        r = self.device.add(name,label,description)
        logger.info(r)
        assert r

    @allure.title("删除设备")
    @pytest.mark.parametrize('name', [
        ["yjy1"],
        ["yjy2"],
        # ["yjy3"],
        # ["yjy4"],
        # ["yjy5"]
    ])
    def test_delete_device(self,name):
        r = self.device.delete(name[0])
        print(r)
        assert r

    @allure.title("查询设备")
    @pytest.mark.parametrize('name', [
        ["yjy3"],
    ])
    def test_retrive_device(self, name):
        response = self.device.retrive(name[0])
        print(self.device.print_info(response))



    @allure.title("修改设备")
    @pytest.mark.parametrize('name, rename, retype', [
        ["yjy3", 'yjy4', 'default'],
    ])
    def test_update_device(self, name, rename, retype):
        r = self.device.update(name, rename, retype)
        print(r)



