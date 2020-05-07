import os

from PreprocessData import *
from FileZipper import *
from ClarinNlprest2 import *

PATH_TO_DATA = '../data'
PATH_TO_RESULT = '../gen'


def create_directory(path_to_dir):
    if not os.path.exists( path_to_dir ):
        os.makedirs( path_to_dir )


def prepare_dataset(path_to_data, path_to_result):
    create_directory(path_to_data)
    path_to_text = os.path.join(path_to_data,'blogi_txt')
    path_to_zip = os.path.join(path_to_result,'zip')
    create_directory(path_to_zip)
    path_to_xml_zip = os.path.join(path_to_result,'xml_zip')
    create_directory(path_to_xml_zip)
    path_to_xml = os.path.join(path_to_result,'xml')
    create_directory(path_to_xml)
    path_to_final_result = os.path.join(path_to_data,'datasets')
    create_directory(path_to_final_result)

    zip_handler = FileZipper()
    zip_handler.zip_all_dir(path_to_data=path_to_text,path_to_result=path_to_zip)

    clarin = ClarinNlprest2(source_path=path_to_zip,
                            save_to_dir=path_to_xml_zip,
                            url='http://ws.clarin-pl.eu/nlprest2/base',
                            task='wcrft2',
                            user='test@test.com')
    clarin.tokenize_directory()
    zip_handler.unzip_all_files_from_dir(path_to_data=path_to_xml_zip,path_to_result=path_to_xml)

    prc_data = PreprocessData(path_to_data=path_to_data)
    prc_data.move_data_to_excel(path_to_data=path_to_xml,path_to_result=path_to_final_result)


if __name__ == '__main__':
    prepare_dataset(path_to_data = PATH_TO_DATA,
                    path_to_result = PATH_TO_RESULT
                    )
