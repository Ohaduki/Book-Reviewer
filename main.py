import os
from readers import txt_reader, docx_extractor, new_format_reader
from excel_utils import sheet_writer
from docx import Document


def storage_system_txt(review, workbook):
    """
    This function gets a txt book review and enters it into the system.
    :param review: The book review.
    :param workbook: The workbook.
    """
    reviewed_book = txt_reader(review)
    sheet_writer(reviewed_book, workbook)


def storage_system_docx(review, workbook):
    """
    This function gets a docx book review and enters it into the system.
    :param review: The book review.
    :param workbook: The workbook.
    """
    new_book = new_format_reader(docx_extractor(review))
    sheet_writer(new_book, workbook)


def folder_search(directory, workbook):
    """
    This function gets a directory with reviews and enters it into the system.
    :param directory: The input directory.
    :param workbook: The workbook.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            storage_system_txt(directory + '\\' + file_name, workbook)
        elif file_name.endswith('.docx'):
            storage_system_docx(directory + '\\' + file_name, workbook)



def main():
    file_path = "C:\\Users\\ohad1\\Documents\\Not Uni\\Python, again\\BookReview"
    folder_search(file_path, file_path + '\\Book Reviews.xlsx')


if __name__ == '__main__':
    main()
