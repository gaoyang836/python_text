# -*- encoding=utf8 -*-
__author__ = "gaoyang"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# poco(text="知乎").click()

poco(name="com.zhihu.android:id/input").click()

poco(name="com.zhihu.android:id/input").set_text('后宫·甄嬛传')

# poco(name="com.zhihu.android:id/magi_title", text='后宫·甄嬛传（电视剧）').click()

# poco(name="com.zhihu.android:id/magi_title")[0].click()

poco(name="com.zhihu.android:id/magi_title",  textMatches='^后宫·甄嬛传.*$').click()

# poco.swipe([0.0124, -0.0146], [0.0307, -0.0364])

poco.swipe([0.5, 0.8], [0.5, 0.2])

