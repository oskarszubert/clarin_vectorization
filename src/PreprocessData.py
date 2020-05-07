import os
import pandas as pd
import xml.etree.ElementTree as ET


class PreprocessData:
    def __init__(self, path_to_data):
        df = pd.read_excel( os.path.join(path_to_data,'Gatunki_kategoryzacja_Podsumowanie.xlsx') )
        self.dict_for_class = {}
        for i in range( df.shape[0] ):
            adress = df.loc[i,'Adres'].replace('http://','')
            adress = adress.replace('/html','')
            adress = adress.replace('/','')
            self.dict_for_class[adress] = df.loc[i,'GATUNEK']


    def move_data_to_excel(self, path_to_data,path_to_result):
        for dir in os.listdir(path_to_data):
            print('Preparing: '+ dir)
            if dir in self.dict_for_class:
                classify = self.dict_for_class[dir]
                tmp_list = []
                path = os.path.join(path_to_data,dir)
                for file in os.listdir( path ):
                    dom = ET.parse(os.path.join(path,file))
                    post = self.read_lex_from_xml(dom)
                    if post: # some documents are empty
                        tmp_list.append([classify,post])

                single_blog_df = pd.DataFrame(tmp_list,columns=['value','text'])
                single_blog_df.to_excel(os.path.join(path_to_result, dir+'.xlsx'),index=False)


    def read_lex_from_xml(self, dom):
        post = []
        chunk_list = dom.findall('chunk')
        for chunk in chunk_list:
            sentence_list = chunk.findall('sentence')
            for sentence in sentence_list:
                token_list = sentence.findall('tok')
                for token in token_list:
                    lex = token.find('lex')
                    base = lex.find('base')
                    ctag = lex.find('ctag')
                    post.append( str(base.text+':'+ctag.text.split(':')[0]) )
        return ';'.join(post)
