import requests
import readtime 
from collections import Counter
from nltk.corpus import stopwords

text= input("write the text here: ")   # I prefer to take the text as input.
def word_counter(text):                 # this is for the word counter.
    words=text.split()
    return len(words)

def numberofletters(text):  #total number of letters
    count=0
    for i in text:
        if(i.isalpha()):
            count+=1
    return count

def longest_word(text):   # longest word in the text
    count=dict()
    words=text.split()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    max_value=0
    max_word=""
    for i in count:
        if  count[i]>max_value:
            max_word=i
            max_value=count[i]
    return max_value
            
def average_length(text):   # average length of the words in the text
    words=text.split()
    word_count=len(words)
    avg= [len(i) for i in words]
    if len(avg)==0:
        result_avg=0
    else:
       result_avg= (float(sum(avg))/words_count)
    return result_avg 

def estimate_reading_time(text):  #estimation for reading time in seconds
    result=readtime.of_text(text,wpm=5)
    timing= result.seconds
    return timing
    
#BONUS 
def median_Word(text):   #finding the median word's lenght
    words=text.split()
    count=len(words)
    if (count%2)!=0:
        result_float=float(count/2)
        result=int(result_float)
    else:
        result=count/2
    medianword=words[result]
    return len(medianword)

#BONUS
def medianbylength(text):  #sort all words by length and then find the median word's length
    words=text.split()
    upd_list=sorted(words, key=len)
    count=len(words)
    if (count%2)!=0:
        result_float=float(count/2)
        result=int(result_float)
    else:
        result=count/2
    medianwordlen=upd_list[result]
    return len(medianwordlen)    

#BONUS
def top_five(text):     #five most common words
    words=text.split()
    counter=Counter(words)
    most_occur=Counter.most_common(5)
    return most_occur  #this returns a list with their counts

#BONUS
def detect_language(text):
    languages_ratios = {}
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements) 
    most_rated_language = max(languages_ratios, key=languages_ratios.get)
    if most_rated_language=='english':
         return 'en'
    else if most_rated_language=='turkish':
        return 'tr'

def printfivecommon(text,i):
    tup=top_five(text)
    word=tup[i]
    return word[i-1]


task = { "wordCount": word_counter(text)  , "letters": numberofletters(text) , "longest": longest_word(text) ,"avgLength": average_length(text):  
,"duration":estimate_reading_time(text) , "medianWordLength": medianbylength(text) ,"medianWord:" median_Word(text) , "language": detect_language(text) }
resp = requests.post(' http://localhost:8080/analyze', json=task)

#task2 is for top 5 common words.
task2={ "topfive": printfivecommon(text,0),  printfivecommon(text,1),  printfivecommon(text,2),  printfivecommon(text,3),  printfivecommon(text,4)}
resp2=requests.post(' http://localhost:8080/analyze/thefivecommon', json=task)