"""

Status
-------
1) Need to update documentation ...


from in_library_browser import browser
b = browser.PubmedBrowser()
#Search for something
b.paint()


"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WileyBrowser():
    pass

class PubmedBrowser():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.ncbi.nlm.nih.gov/pubmed/")
        self.lib = get_library()

    def paint(self):
        """

        #TODO: We could also delete the elements we have already ...

        Currently paints PMIDs:
            - red, if not in library
            - green, if in library

        :return: None
        """

        PMID_CLASS_ID = 'rprtid'

        elements = self.driver.find_elements_by_class_name(PMID_CLASS_ID)
        all_pmids = []
        for elem in elements:
            temp_text = elem.text
            all_pmids.append(int(temp_text[6:]))

        #Now, is each in our library????

        has_docs = self.lib.has_docs(all_pmids)

        driver_local = self.driver
        for i, has_doc in enumerate(has_docs):
            cur_elem = elements[i]
            if has_doc:
                #new_str = "arguments[0].innerText = '%s'" % (cur_elem.text + " X")
                #self.driver.execute_script(new_str, cur_elem)
                driver_local.execute_script("arguments[0].setAttribute('style','Color:green')",cur_elem)
            else:
                driver_local.execute_script(
                    "arguments[0].setAttribute('style','Color:red')",
                    cur_elem)

def get_library():
    #Eventually I'd like to have a switch here for other options ...
    from mendeley import client_library
    cl = client_library.UserLibrary(verbose=True)
    return cl
