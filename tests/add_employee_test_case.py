import unittest
from random import randint

from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select


class AddEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\kose_\Desktop\PortnovSchool\SeleniumWithPython\ellie_2018\DriversforBrowsers\chromedriver.exe')
        self.driver.get('http://hrm.seleniumminutes.com/')
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        empId = randint(120000,999999)
        emptitle = 'QA Engineer'
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        sleep(2)

        welcome_text = driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_text)

    # Click the add button
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('btnAdd').click()

    # Enter the first and last name
        driver.find_element_by_id('firstName').send_keys("john")
        driver.find_element_by_id('lastName').send_keys("pablo")

    # Enter and remember the empID
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)

    # Save the Employee
        driver.find_element_by_id('btnSave').click()
    #Adding a job title
        driver.find_element_by_link_text('Job').click()
        driver.find_element_by_id('btnSave').click()
        Select(driver.find_element_by_id('job_job_title')).select_by_visible_text(emptitle)
        driver.find_element_by_id('btnSave').click()


    # Go to PIM page
        driver.find_element_by_id('menu_pim_viewEmployeeList').click()
    # todo ati : may need to come back

    # Search by employeeID
        driver.find_element_by_id('empsearch_id').send_keys(empId)
        driver.find_element_by_id('searchBtn').click()
    # Expected; 1 record back
        lst = driver.find_elements_by_xpath("//td[3]/a")
        self.assertTrue(len(lst) == 1)

    # Expected Correct Name and empID
        firstName = driver.find_element_by_xpath("//td[3]/a").text
        lastName = driver.find_element_by_xpath("//td[4]/a").text
        jobTitle = driver.find_element_by_xpath("//td[5]").text

        messages = "Expected the table to contain first name '{0}' but instead the value was '{1}'"
        self.assertEqual("john", firstName, messages.format("john", firstName))
        self.assertEqual("pablo", lastName)
        self.assertEqual(emptitle, jobTitle)



if __name__ == '__main__':
    unittest.main()
