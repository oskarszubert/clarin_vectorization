import os
import pandas as pd
from math import log
from sklearn.utils import shuffle


class Morphosyntactic:
    def __init__(self,path_to_data, classes_file):
        self.path_to_data = path_to_data
        self.vocabulary = {}
        self.idf_help_dict = {}
        self.number_of_documents = 0
        self.classes = self.create_dict_from_file(classes_file)

        self.subst = False
        self.depr = False
        self.num = False
        self.numcol = False
        self.adj = False
        self.adja = False
        self.adjp = False
        self.ajdc = False
        self.adv = False
        self.ppron12 = False
        self.ppron3 = False
        self.siebie = False
        self.fin = False
        self.bedzie = False
        self.algt = False
        self.preat = False
        self.impt = False
        self.imps = False
        self.inf = False
        self.pcon = False
        self.pant = False
        self.get = False
        self.pact = False
        self.ppas = False
        self.winien = False
        self.pred = False
        self.prep = False
        self.conj = False
        self.comp = False
        self.qub = False
        self.brev = False
        self.burk = False
        self.interj = False
        self.interp = False
        self.xxx = False
        self.jgn = False


    def create_dict_from_file(self, filename):     # classes will be represented by numbers, number will be taken from oder on file
        tmp_dict = {}
        ordinal_number = 0
        try:
            file = open(filename, 'r')
            for line in file:
                tmp_dict[  line.rstrip() ] = ordinal_number
                ordinal_number += 1
        except Exception as e:
            print(e)
            exit(f'Error! while reading {filename}.')

        return tmp_dict


    def filter_ctag(self, row):
        value = row['value']
        text = row['text']
        clear_text_list = []
        for element in text.split(';'):
            tag = element.split(':')
            if len(tag) == 2:
                if tag[1] == 'subst' and self.subst:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0])
                if tag[1] == 'depr' and self.depr:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0])
                if tag[1] == 'num' and self.num:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0])
                if tag[1] == 'numcol' and self.numcol:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0])
                if tag[1] == 'adj' and self.adj:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'adja' and self.adja:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'adjp' and self.adjp:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'ajdc' and self.ajdc:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'adv' and self.adv:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'ppron12' and self.ppron12:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'ppron3' and self.ppron3:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'siebie' and self.siebie:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'fin' and self.fin:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'bedzie' and self.bedzie:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'algt' and self.algt:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'preat' and self.preat:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'impt' and self.impt:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'imps' and self.imps:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'inf' and self.inf:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'pcon' and self.pcon:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'pant' and self.pant:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'get' and self.get:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'pact' and self.pact:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'ppas' and self.ppas:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'winien' and self.winien:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'pred' and self.pred:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'prep' and self.prep:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'conj' and self.conj:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'comp' and self.comp:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'qub' and self.qub:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'brev' and self.brev:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'burk' and self.burk:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'interj' and self.interj:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'interp' and self.interp:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'xxx' and self.xxx:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 
                if tag[1] == 'jgn' and self.jgn:
                    self.proceed_tag(tag[0])
                    clear_text_list.append(tag[0]) 

        if clear_text_list:
            clear_text_list_set = set(clear_text_list)
            for tag in clear_text_list_set:
                if tag in self.idf_help_dict:
                    self.idf_help_dict[tag] += 1
                else:
                    self.idf_help_dict[tag] = 1

            return [value, clear_text_list]


    def create_vocab_and_new_dataset_from_excel(self,path_to_dataset, vocab_size):
        new_dataset = []
        for dir in os.listdir(path_to_dataset):
            df = pd.read_excel( os.path.join(path_to_dataset,dir) )
            self.number_of_documents += df.shape[0]

            print(f'Processing {dir}')
            for row in df.iterrows():
                row = self.filter_ctag(row[1])
                if row:
                    new_dataset.append(row)

        vocabulary = self.save_vocabulary()
        self.prepare_proper_vocabulary(vocabulary=vocabulary,vocab_size=vocab_size)     # modify self.vocabulary

        return new_dataset


    def prepare_proper_vocabulary(self, vocabulary, vocab_size):
        self.vocabulary = {}
        for tag in vocabulary[:vocab_size]:
            self.vocabulary[ tag[0] ] = tag[1:]


    def save_vocabulary(self):
        vocabulary = []
        sorted_vocabulary = sorted(self.vocabulary.items(), key=lambda vocabulary: vocabulary[1], reverse=True)

        for token in sorted_vocabulary:
            token = list(token)
            token.append(  self.idf_help_dict[token[0]]  )
            token.append( self.calc_idf(self.idf_help_dict[token[0]]) )
            vocabulary.append(token)

        vocab_df = pd.DataFrame(vocabulary,columns=['lex','total_appears','number_of_appears','idf'])
        vocab_df.to_excel(os.path.join(self.path_to_data, 'vocabulary.xlsx'),index=False)

        return vocabulary


    def calc_idf(self, number_of_appears):
        return log(int(self.number_of_documents)/number_of_appears)


    def proceed_tag(self, tag):
        if tag in self.vocabulary:
            self.vocabulary[tag] += 1
        else:
            self.vocabulary[tag] = 1


    def vectorize_data(self, dataset):
        sorted_keys = list(self.vocabulary.keys())
        sorted_keys.sort()
        bow_dataset = []
        binary_dataset = []
        tf_dataset = []
        tf_idf_dataset = []
        for row in dataset:
            if not row[0] in self.classes:
                continue
 
            row_class = self.classes[ row[0] ]
            size_of_document = len( row[1] )

            vector_template = dict.fromkeys(sorted_keys,0)
 
            for token in row[1]:
                if token in vector_template:
                    vector_template[token] += 1

            binary_vector = self.create_binary_vector(vector = dict(vector_template))
            tf_vector = self.create_tf_vetor(vector = dict(vector_template), size_of_document=size_of_document)
            tf_idf_vector = self.create_tf_idf_vetor(vector = dict(tf_vector))


            bow_dataset.append( [row_class, vector_template] )
            binary_dataset.append( [row_class, binary_vector] )
            tf_dataset.append( [row_class, tf_vector] )
            tf_idf_dataset.append( [row_class, tf_idf_vector] )


        self.save_dataset_to_excel(dataset=bow_dataset, dir_name='bow', columns=list(sorted_keys))
        self.save_dataset_to_excel(dataset=binary_dataset, dir_name='binary', columns=list(sorted_keys))
        self.save_dataset_to_excel(dataset=tf_dataset, dir_name='tf', columns=list(sorted_keys))
        self.save_dataset_to_excel(dataset=tf_idf_dataset, dir_name='tf_idf', columns=list(sorted_keys))


    def save_dataset_to_excel(self, dataset, dir_name, columns):
        path = os.path.join(self.path_to_data,'datasets',dir_name)
        if not os.path.exists( path ):
            os.makedirs( path )

        tmp_dataset = []
        for row in dataset:
            tmp_vector = list(row[1].values() )
            tmp_vector.insert(0, row[0] )
            tmp_dataset.append( tmp_vector )
        
        columns.insert(0, 'value')
        df = pd.DataFrame(tmp_dataset,columns=columns)
        df = shuffle(df)


        print(f'Saving data into: {path}')
        df.to_excel(os.path.join(path,'data.xlsx'),index=False)
        df.iloc[0:0]
        dataset = []


    def create_binary_vector(self, vector):
        for tag in vector:
            if vector[tag]:
                vector[tag] = 1
        return vector


    def create_tf_vetor(self, vector, size_of_document):
        for tag in vector:
            if vector[tag]:
                vector[tag] = vector[tag]/size_of_document
        return vector


    def create_tf_idf_vetor(self, vector):
        for tag in vector:
            if vector[tag]:
                vector[tag] = vector[tag] * self.vocabulary[tag][2]
        return vector

