import nltk
from nltk import word_tokenize, sent_tokenize  
from nltk.tokenize.treebank import TreebankWordDetokenizer
import soundfile as sf
import librosa
import os
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

nltk.download('words')
nltk.download('punkt')



# NER models
# English NER Model
EN_NER = spacy.load("en_core_web_lg")
EN_NER.add_pipe("merge_entities")

# Arabic NER Model 
tokenizer = AutoTokenizer.from_pretrained("Davlan/bert-base-multilingual-cased-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained("Davlan/bert-base-multilingual-cased-ner-hrl")
AR_NER = pipeline("ner", model=model, tokenizer=tokenizer)


#  Detokenization
detokenizer = TreebankWordDetokenizer()


custom_labels =["انيميا"]

def Tokenize(text:str):
      tokenized_text = [list(map(str.lower, word_tokenize(text))) 
            for sent in sent_tokenize(text)] 
      return tokenized_text
      

def Detokenize(tokenized_text:list):
      Anonmized_text= detokenizer.detokenize(tokenized_text)
      Labels = ["GPE", "PER", "LOC", "ORG"]
      encryption = ["Country", "Person", "Location", "Organization"]
      for i in range(len(Labels)):
              Anonmized_text = Anonmized_text.replace(Labels[i] , encryption[i])

      return Anonmized_text




def NER_finder(text:str , mode:str):
  
    tokenized_text= Tokenize(text)

    # Classify words (AR, EN):
    if mode == "fully":
            for i in range(len(tokenized_text[0])):
                print(tokenized_text[0][i])

                if(tokenized_text[0][i].isascii()):
                    doc = EN_NER(tokenized_text[0][i])
                    if (len(doc.ents) == 1) :
                        tokenized_text[0][i] = doc.ents[0].label_
                else:
                    tag= AR_NER(tokenized_text[0][i])
                    if len(tag) != 0:
                       tokenized_text[0][i]= tag[0]['entity'].split("-")[-1]

    elif mode == "personal_info":
            for i in range(len(tokenized_text[0])):
                print(tokenized_text[0][i])
                if(tokenized_text[0][i].isascii()):
                    doc = EN_NER(tokenized_text[0][i])
                    if (len(doc.ents) == 1) :
                        if ((doc.ents[0].label_) == "PER" ):
                            tokenized_text[0][i] = doc.ents[0].label_
                else:
                    tag= AR_NER(tokenized_text[0][i])
                    if len(tag) != 0:
                        if((tag[0]['entity'].split("-")[-1]) == "PER"):
                            tokenized_text[0][i]= tag[0]['entity'].split("-")[-1]

    elif mode == "medical_stuff":
        for i in range(len(tokenized_text[0])):
                print(tokenized_text[0][i])
                for j in range (len(custom_labels)):
                    # if(custom_labels[j].isascii()):
                    if tokenized_text[0][i] == custom_labels[j]:
                        tokenized_text[0][i] = "medical_info"

    encrypted_text = Detokenize(tokenized_text[0])
    return encrypted_text
      

text= "لما كنت في  Egypt احضرت  coffe من عمر"
print(NER_finder(text, "fully"))
print(NER_finder(text, "personal_info"))
