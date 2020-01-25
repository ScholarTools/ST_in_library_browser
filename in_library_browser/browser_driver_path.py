import requests
#import wget
import zipfile
import os

#A work in progress ...

#https://stackoverflow.com/questions/59602984/browser-for-python-selenium-or-other-remote-control-library-without-manual-d?noredirect=1#comment105408159_59602984

def driver_root():
    temp = os.path.dirname(__file__)

def driver_path():
    pass

def download_driver():
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # download the zip file using the url built above
    #urllib.request.urlretrieve('url', 'path')


    #latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall() # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)