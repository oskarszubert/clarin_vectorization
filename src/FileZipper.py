import os
import shutil

class FileZipper:
    def __init__(self):
        pass

    def zip_all_dir(self, path_to_data, path_to_result):
        for dir in os.listdir(path_to_data):
            shutil.make_archive(os.path.join(path_to_result,dir),
                                'zip',
                                os.path.join(path_to_data,dir)
                                )
            print('Zipped:',dir)


    def unzip_all_files_from_dir(self, path_to_data, path_to_result):
        for dir in os.listdir(path_to_data):
            if '.zip' in dir:
                new_name = os.path.join(path_to_result, dir.replace('.zip', ''))

            shutil.unpack_archive(  os.path.join(path_to_data,dir),
                                    new_name,
                                    'zip'
                                    )
            print('UnZipped:',dir)
