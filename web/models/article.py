from uuid import uuid4
import re

DEBUG = False
BASE_URL = "http://www.precision-medicine-portal.scilifelab.se"
MAX_URL_PATH_LEN = 30
class Article():
    id: str
    name: str

    def __init__(self, title: str, content_url: str):
        self.id = str(uuid4())
        try:
            self.url = self.generate_url_path_from_title(title)
        except:
            raise NameError # TODO: Create custom error that's more descriptive.
        self.content_url = content_url
    
    def __str__(self) -> str:
        return f"#############\nid: {self.id}\nurl: {self.url}\ncontent_url: {self.content_url}\n#############"
    
    def generate_url_path_from_title(self, title: str) -> str:
        if len(title) < 1:
            raise NameError
        white_space_cleaned_string = ' '.join(title.split()).replace(' ', '-')
        special_character_cleaned_string = re.sub('[^A-Za-z0-9_.\\-~]', '-', white_space_cleaned_string)[:MAX_URL_PATH_LEN]
        trailing_dashes_cleaned = re.sub('-+\\Z', '', special_character_cleaned_string)
        leading_dashes_cleaned = re.sub('\\A-+', '', trailing_dashes_cleaned)
        return BASE_URL + '/' + leading_dashes_cleaned
    

