#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest, time
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities


class AppiumTests(unittest.TestCase):
    def setUp(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'iOS'
        # desired_caps['platformVersion'] = '9.0'
        # desired_caps['deviceName'] = 'iPhone 6s'
        # desired_caps['app'] = '/Users/chenchenzheng/github/appium/python-client/test/apps/UICatalog.app.zip'
        # desired_caps['noReset'] = 'false'


        desired_caps = desired_capabilities.get_desired_capabilities('whistler.app')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):

        self.driver.quit()

    # def test_lock(self):
    #     el = self.driver.find_element_by_id('ButtonsExplain')
    #
    #     self.assertIsNotNone(el)
    #     self.driver.lock(0)
    #     self.assertRaises(NoSuchElementException, self.driver.find_element_by_id, 'ButtonsExplain')
    #     sleep(10)

        # # this does not seem to ever unlock, so the assertion fails
        # el = self.driver.find_element_by_id('ButtonsExplain')
        # self.assertIsNotNone(el)
    def test_GogglePal_login(self):
        
        self.driver.get_window_size();
        # 3. SWIPE        
        # Perform swipe gesture on home screen- swipe(startX, startY, endX, endY, duration)
        self.driver.swipe(300, 200, 1, 200, 500)
        # action.tap(e1).perform()
        time.sleep(1)
        self.driver.swipe(300, 200, 1, 200, 500)
        time.sleep(1)
        startedButton = self.driver.find_element_by_name('Get Started')
        startedButton.click();
        # action.tap(startedButton).perform()
        time.sleep(1)
        
        facebookButton = self.driver.find_element_by_name('Log in with Facebook')
        digitsButton = self.driver.find_element_by_name('Login with phone number')
        
        self.assertTrue(facebookButton)
        self.assertTrue(digitsButton)

    # def test_shake(self):
    #     # what can we assert about this?
    #     self.driver.shake()

    # def test_hide_keyboard(self):
    #     el = self.driver.find_element_by_name('TextFields, Uses of UITextField')
    #     el.click()

    #     # get focus on text field, so keyboard comes up
    #     el = self.driver.find_element_by_class_name('UIATextField')
    #     el.set_value('Testing')

    #     el = self.driver.find_element_by_class_name('UIAKeyboard')
    #     self.assertTrue(el.is_displayed())

    #     self.driver.hide_keyboard(key_name='Done')

    #     self.assertFalse(el.is_displayed())

    # def test_hide_keyboard_presskey_strategy(self):
    #     el = self.driver.find_element_by_name('TextFields, Uses of UITextField')
    #     el.click()

    #     # get focus on text field, so keyboard comes up
    #     el = self.driver.find_element_by_class_name('UIATextField')
    #     el.set_value('Testing')

    #     el = self.driver.find_element_by_class_name('UIAKeyboard')
    #     self.assertTrue(el.is_displayed())

    #     self.driver.hide_keyboard(strategy='pressKey', key='Done')

    #     self.assertFalse(el.is_displayed())

    # def test_hide_keyboard_no_key_name(self):
    #     el = self.driver.find_element_by_name('TextFields, Uses of UITextField')
    #     el.click()

    #     # get focus on text field, so keyboard comes up
    #     el = self.driver.find_element_by_class_name('UIATextField')
    #     el.set_value('Testing')

    #     el = self.driver.find_element_by_class_name('UIAKeyboard')
    #     self.assertTrue(el.is_displayed())

    #     self.driver.hide_keyboard()
    #     sleep(10)

    #     # currently fails.
    #     self.assertFalse(el.is_displayed())


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
