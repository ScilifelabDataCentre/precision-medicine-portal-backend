import re

def generate_url_from_title(title: str) -> str:
    max_url_length = 30

    title_lower = title.lower()
    white_space_cleaned_string = ' '.join(title_lower.split()).replace(' ', '-')
    special_character_cleaned_string = re.sub('[^A-Za-z0-9_.\\-~]', '-', white_space_cleaned_string)[:max_url_length]
    trailing_dashes_cleaned = re.sub('-+\\Z', '', special_character_cleaned_string)
    leading_dashes_cleaned = re.sub('\\A-+', '', trailing_dashes_cleaned)
    return leading_dashes_cleaned