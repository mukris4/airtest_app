# -*- encoding=utf8 -*-
__author__ = "dbk"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-
__author__ = "dbk"
__title__ = "test_airtest"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco= AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
def MY():

    poco("com.cmcc.cmvideo:id/image_share_button").click()
    sleep(2)

    # 复制链接
    poco("com.cmcc.cmvideo:id/btn_cancel").click()

MY();