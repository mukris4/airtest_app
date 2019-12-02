# -*- encoding=utf8 -*-
__author__ = "dbk"
__title__ = "test_airtest"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco= AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
shell(  "am start -n com.cmcc.cmvideo/com.cmcc.cmvideo.MainActivity")
def VRshare():
    # 点击VR专区
    sleep(2)
    poco(text="VR专区").click()
    sleep(2)
    poco("com.cmcc.cmvideo:id/image_share_button").click()
    sleep(2)
 
    #复制链接 
    copylink=poco(text="复制链接")
#print(copylink.exists())
 
    copylink.click()
VRshare();
