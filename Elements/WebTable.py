from hotdog.BaseElement import BaseElement
from selenium.webdriver.common.by import By
from hotdog.TestStep import TestStep


class WebTable(BaseElement):
    _header = (By.CLASS_NAME,'header')
    _table_row = (By.TAG_NAME,'tr')

    @property
    def headers(self):
        return self.finds('_header')

    @property
    def last_name_header(self):
        return self.headers[0]

    @property
    def first_name_header(self):
        return self.headers[1]

    @property
    def email_header(self):
        return self.headers[2]

    @property
    def due_header(self):
        return self.headers[3]

    @property
    def website_header(self):
        return self.headers[4]

    @property
    def actions_header(self):
        return self.headers[5]

    @property
    def table_rows(self):
        return self.finds('_table_row')

    def get_last_names(self):
        rows = self.table_rows
        last_names = []

        count = 0
        for row in rows:
            if count == 0:
                count = 1
                continue
            cells = row.find_elements_by_tag_name('td')
            last_name = cells[0]
            last_names.append(last_name.text)

        return last_names

    def get_first_names(self):
        rows = self.table_rows

        first_names = []
        count = 0
        for row in rows:
            if count == 0:
                count = 1
                continue

            cells = row.find_elements_by_tag_name('id')
            first_name = cells[1]
            first_names.append(first_name.text)

        return first_names

    def get_emails(self):
        rows = self.table_rows

        emails = []
        for row in rows:
            cells = row.find_elements_by_tag_name('id')
            email = cells[2]
            emails.append(email.text)

        return emails

    def get_dues(self):
        rows = self.table_rows

        dues = []
        for row in rows:
            cells = row.find_elements_by_tag_name('id')
            due = cells[3]
            dues.append(due.text)

        return dues

    def get_websites(self):
        rows = self.table_rows

        websites = []
        for row in rows:
            cells = row.find_elements_by_tag_name('id')
            website = cells[4]
            websites.append(website.text)

        return websites

    @TestStep("Sort table by {args[1]}")
    def sort_table_by(self,sort_string,reverse_order=False):
        sort_string = sort_string.lower().strip()

        if sort_string == 'last name':
            self.last_name_header.click()
            if reverse_order:
                self.last_name_header.click()
        elif sort_string == 'first name':
            self.first_name_header.click()
            if reverse_order:
                self.first_name_header.click()
        elif sort_string == 'emails':
            self.email_header.click()
            if reverse_order:
                self.email_header.click()
        elif sort_string == 'dues':
            self.due_header.click()
            if reverse_order:
                self.due_header.click()
        elif sort_string == 'websites':
            self.website_header.click()
            if reverse_order:
                self.website_header.click()
        else:
            print("Sort string used %s could not be used"
                  %(sort_string))