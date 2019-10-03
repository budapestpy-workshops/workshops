import unittest
from selenium import webdriver


# The test class is a child of the unittest.TestCase class.
class NuclearDisasterTests(unittest.TestCase):
    # This function runs before all the test cases.
    def setUp(self) -> None:
        # The driver is a member of the class.
        self.driver = webdriver.Firefox(executable_path="bin/geckodriver")

    # This function runs after all the test cases.
    def tearDown(self) -> None:
        self.driver.close()

    def test_chernobyl_date(self):
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        search_field = self.driver.find_element_by_id("searchInput")
        search_field.send_keys("chernobyl disaster")
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        body_content = self.driver.find_element_by_id("bodyContent")
        paragraphs = body_content.find_elements_by_tag_name("p")
        self.assertTrue("26 April 1986" in paragraphs[2].text)

    # This test is expected to fail.
    @unittest.expectedFailure
    def test_chernobyl_us_spies(self):
        self.driver.get("https://wikipedia.org")
        search_field = self.driver.find_element_by_id("searchInput")
        search_field.send_keys("chernobyl disaster")
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        body_content = self.driver.find_element_by_id("bodyContent")
        paragraphs = body_content.find_elements_by_tag_name("p")
        self.assertTrue("US spies" in paragraphs[2].text)

    # This test is skipped, because the unittest framework does not give tools
    # which can be used to have different inputs, and once expected pass, once expected failure.
    @unittest.skip("This test is skipped, because the second fact, the US Spies would make it fail.")
    def test_chernobyl(self):
        for fact in ["26 April 1986", "US Spies"]:
            # The self.subTest can be used to parametrize these tests.
            with self.subTest(fact=fact):
                self.driver.get("https://wikipedia.org")
                search_field = self.driver.find_element_by_id("searchInput")
                search_field.send_keys("chernobyl disaster")
                submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
                submit_button.click()
                body_content = self.driver.find_element_by_id("bodyContent")
                paragraphs = body_content.find_elements_by_tag_name("p")
                self.assertTrue(fact in paragraphs[2].text)

    def test_fukushima(self):
        self.driver.get("https://en.wikipedia.org/wiki/Chernobyl_disaster")
        link = self.driver.find_elements_by_xpath("//a[@href='/wiki/Fukushima_Daiichi_nuclear_disaster']")[0]
        link.click()
        p = self.driver.find_element_by_css_selector(".mw-parser-output > p:nth-child(8)")
        self.assertIn("11 March 2011", p.text)
