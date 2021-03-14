from behave import *
from selenium import webdriver


@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'open facebook homepage')
def openHomepage(context):
    context.driver.get('https://www.facebook.com')

@then(u'verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//img[contains(@class,'fb_logo _8ilh')]").is_displayed()
    assert status is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()