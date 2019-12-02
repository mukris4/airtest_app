__author__ = "H"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-

__title__ = "test_airtest"
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco= AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
shell(  "am start -n com.cmcc.cmvideo/com.cmcc.cmvideo.MainActivity")

auto_setup(__file__)
def MY():
    sleep(2)
    poco(text="VR专区").click()
    sleep(2)
    poco("com.cmcc.cmvideo:id/image_share_button").click()
    sleep(2)

    # 复制链接
    poco("com.cmcc.cmvideo:id/btn_cancel").click()

MY();