import docx
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import process_corpus11 as word
import process_corpus10 as pdf

def getText(textFileName):
    file = open(textFileName, 'r')
    return file.read()

def processFile(newCorpusDir):
    if not os.path.isdir(newCorpusDir):
        os.mkdir(newCorpusDir)
    txt1 = getText('sample_feed.txt')
    txt2 = pdf.getTextPDF('VirtualBoxTroubleshooting.pdf')
    txt3 = word.getTextWord('my_doc.docx')

    files = [txt1, txt2, txt3]
    for idx, f in enumerate(files):
        with open(newCorpusDir + str(idx)+'.txt', 'w') as fout:
            fout.write(f)

    newCorpus = PlaintextCorpusReader(newCorpusDir, '.*')

    print(newCorpus.words())
    print(newCorpus.sents(newCorpus.fileids()[1]))
    print(newCorpus.paras(newCorpus.fileids()[0]))

if __name__ == '__main__':
    processFile('my_corpus/')


