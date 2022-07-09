import re
from docx import Document
from word2number import w2n
from book import Book

TXT_BOOK_READ_REGEX = r"(?P<title>.*) by (?P<author>.*)\nSummary: (?P<summary>.*)\nPrice: (?P<price>\d+)\nCategory:" \
                  r" (?P<category>.*)\nAge: (?P<min_age>\d*)-(?P<max_age>\d*)"


def txt_reader(loc):
    """
    Receives a txt file with the first review format and returns a book class
    :param loc: The directory of the review
    """
    new_review = open(loc, "r")
    match = re.match(TXT_BOOK_READ_REGEX, new_review.read())
    groups = match.groupdict()
    new_book = Book(groups['title'], groups['author'], groups['summary'], groups['price'], groups['category'],
                    groups['min_age'], groups['max_age'])
    return new_book


DOCX_BOOK_READ_REGEX = r"Name: [\"|“](?P<title>.*)[\"|”]\nAuthor: (?P<author>.*)\nDescription:"\
        r"(?P<summary>.*)\nPrice: (?P<price>.*)\nShelf: (?P<category>.*)\nAge: (?P<age_range>.*)"

AGES_DICT = {
    "kids": (0, 10),
    "teenagers": (11, 19),
    "adults": (20, 120),
}


def new_format_reader(text):
    """
    This function receives a string in the new format, extracts it and returns a book class
    :param text: the string
    :return:
    """
    match = re.match(DOCX_BOOK_READ_REGEX, text)
    groups = match.groupdict()
    new_book = Book(groups['title'], groups['author'], groups['summary'], w2n.word_to_num(groups['price']), groups['category'],
                    AGES_DICT[groups['age_range'].lower()][0], AGES_DICT[groups['age_range'].lower()][1])
    return new_book


def docx_extractor(loc):
    """
    This function recieves a word file and returns a string
    :param loc: The word file location
    """
    document = Document(loc)
    fulltext = []
    for para in document.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)
