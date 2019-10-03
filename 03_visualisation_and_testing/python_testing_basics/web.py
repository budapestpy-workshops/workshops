import pytest
from selenium import webdriver


# This decorator makes the following function definition a pytest fixture.
# We will use this to open only one browser for the two test functions,
# and do not close the browser window and reopen again.
# Read more about the pytest fixtures: https://docs.pytest.org/en/latest/fixture.html
@pytest.fixture(scope='module')  # the scope will tell to use this fixture for the whole module
def driver():
    driver = webdriver.Firefox(executable_path="bin/geckodriver")
    # You can read more about the yield keyword on the https://docs.python.org
    yield driver  # This returns the driver to the tests and after the tests did run continue with closing the browser
    # This part always runs, even when the test fails.
    driver.close()


# This decorator marks the test to be parametrized. The parametrized argument will be called
# 'fact', and it will be fed once with the date, once with the 'US Spies' string.
@pytest.mark.parametrize(
    "fact",
    [
        "26 April 1986",
        # This input data is marked so it is expected to fail, so the whole test will pass if there
        # is an assertion error in this second case.
        pytest.param("US Spies", marks=pytest.mark.xfail),
    ],
)
# The driver is the above defined pytest fixture and the fact is the parameter used for testing.
def test_chernobyl_fact(driver, fact):
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    search_field = driver.find_element_by_id("searchInput")
    search_field.send_keys("chernobyl disaster")
    search_button = driver.find_element_by_id("searchButton")
    search_button.click()
    body_content = driver.find_element_by_id("bodyContent")
    paragraphs = body_content.find_elements_by_tag_name("p")
    assert fact in paragraphs[2].text


def test_fukushima(driver):
    driver.get("https://en.wikipedia.org/wiki/Chernobyl_disaster")
    link = driver.find_elements_by_xpath("//a[@href='/wiki/Fukushima_Daiichi_nuclear_disaster']")[0]
    link.click()
    p = driver.find_element_by_css_selector(".mw-parser-output > p:nth-child(8)")
    assert "11 March 2011" in p.text
