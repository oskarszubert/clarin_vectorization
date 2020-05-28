from Morphosyntactic import *


PATH_TO_DATASET = '../data/datasets'
PATH_TO_GEN = '../gen'
PATH_TO_DATA = '../data'
VOCAB_SIZE = 100

if __name__ == '__main__':
    classes_file = 'dataset_classes.txt'
    morfo = Morphosyntactic(path_to_data=PATH_TO_GEN, classes_file=os.path.join(PATH_TO_DATA,classes_file) )

    morfo.subst = False
    morfo.depr = False
    morfo.num = False
    morfo.numcol = False
    morfo.adj = False
    morfo.adja = False
    morfo.adjp = False
    morfo.ajdc = False
    morfo.adv = False
    morfo.ppron12 = False
    morfo.ppron3 = False
    morfo.siebie = False
    morfo.fin = False
    morfo.bedzie = False
    morfo.algt = False
    morfo.preat = False
    morfo.impt = False
    morfo.imps = False
    morfo.inf = False
    morfo.pcon = False
    morfo.pant = False
    morfo.get = False
    morfo.pact = False
    morfo.ppas = False
    morfo.winien = False
    morfo.pred = False
    morfo.prep = False
    morfo.conj = False
    morfo.comp = False
    morfo.qub = False
    morfo.brev = False
    morfo.burk = False
    morfo.interj = False
    morfo.interp = False
    morfo.xxx = False
    morfo.jgn = False

    dataset = morfo.create_vocab_and_new_dataset_from_excel(path_to_dataset=PATH_TO_DATASET, vocab_size=VOCAB_SIZE)

    filename = str(VOCAB_SIZE) + '_data_'
    morfo.vectorize_data(dataset,filename)
