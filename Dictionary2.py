# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 01:00:04 2019

@author: Ahmed
"""
import nltk
import string
import pandas

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import re
calcium_Disease_Dictionary ={
'DM':['MYOTONIC DYSTROPHY 1 '],
'HI':['Harlequin Fetus '],
'HT':['Hashimoto Disease '],
'afib':['Atrial Fibrillation '],
'anaphylaxi':['anaphylaxis '],
'anemia':['Anemia '],
'append':['Appendicitis '],
'arb':['BESTROPHINOPATHY , AUTOSOMAL RECESSIVE '],
'arrest':['Cardiac Arrest '],
'arthriti':['Arthritis '],
'asthma':['Asthma '],
'asthmat':['Asthma '],
'ate':['Ataxia Telangiectasia '],
'bad':['Brachial Amyotrophic Diplegia '],
'bald':['Alopecia '],
'bend':['Decompression Sickness '],
'bo':['Dermatofibrosis lenticularis disseminata '],
'bronchiti':['Bronchitis '],
'bronchospasm':['Bronchial Spasm '],
'card':['Sex Differentiation Disorders '],
'cardiomyopathi':['Cardiomyopathies '],
'chf':['Congestive heart failure '],
'chilblain':['Chilblains'],
'ckd':['Chronic Kidney Diseases '],
'cold':['Common Cold ', 'Upper Respiratory Infections '],
'coliti':['Colitis '],
'coma':['Comatose '],
'copd':['Copd', 'Chronic obstructive pulmonary disease of horses '],
'curb':['Curb'],
'dehydr':['Dehydration '],
'di':['Deafness , Sensorineural , And Male Infertility '],
'diabet':['Diabetes', 'Diabetes Mellitus '],
'diseas':['Disease', 'Disease '],
'disord':['Disease '],
'door':['Digitorenocerebral Syndrome '],
'dysfunct':['DYSFUNCTION - SKIN DISORDERS '],
'er':['Amelogenesis imperfecta nephrocalcinosis '],
'fed':['Fish-Eye Disease '],
'fibril':['Fibrillation '],
'fibromyalgia':['Fibromyalgia '],
'flash':['Photopsia '],
'flu':['Influenza '],
'gastriti':['Gastritis '],
'glass':['Chromosome 2q32-Q33 Deletion Syndrome '],
'gout':['Gout '],
'hit':['Heparin-induced thrombocytopenia '],
'hive':['Urticaria '],
'htn':['Hypertensive disease '],
'hypertens':['Hypertensive disease '],
'hyperthyroid':['Hyperthyroidism '],
'hyponatremia':['Hyponatremia '],
'ib':['Irritable Bowel Syndrome '],
'incontin':['Incontinence '],
'infect':['Infection'],
'laryng':['Acute laryngitis ', 'Laryngitis '],
'let':['Lupus erythematosus tumidus '],
'lupu':['Lupus Vulgaris ', 'Lupus Erythematosus , Discoid ', 'Lupus Erythematosus '],
'lvh':['Left Ventricular Hypertrophy '],
'march':['Hydranencephaly with Renal Aplasia-Dysplasia '],
'mastocytosi':['Mastocytosis '],
'me':['Meckel syndrome type 1 '],
'med':['MICROCEPHALY , EPILEPSY , AND DIABETES SYNDROME '],
'mg':['MUNGAN SYNDROME '],
'migrain':['Migraine Disorders '],
'mod':['Diabetes Mellitus , Non-Insulin-Dependent '],
'multi':['Multiple Chronic Conditions '],
'myocard':['Myocarditis '],
'neuropathi':['Neuropathy '],
'obes':['Obesity '],
'pac':['Atrial Premature Complexes '],
}

calcium_Mental_Dysfunction_Dictionary ={
'anorgasmia':['Orgasm incapacity'],
'anxieti':['Anxiety'],
'anxiou':['Anxiety'],
'anxious':['Anxiety'],
'apathi':['Apathy'],
'block':['Mental blocking'],
'confus':['Confusion'],
'delus':['Delusions'],
'dementia':['Dementia'],
'depress':['Mental Depression', 'Depressive disorder'],
'disori':['Disorientation'],
'drowsi':['Somnolence'],
'forget':['Forgetting'],
'hallucin':['Hallucinations'],
'hyper':['Hyperactive behavior'],
'hyperact':['Hyperactive behavior'],
'insan':['Insanity'],
'moodi':['Mood swings'],
'nightmar':['Nightmare', 'Nightmares'],
'ocd':['Obsessive-Compulsive Personality', 'Obsessive-Compulsive Disorder'],
        
}

calcium_ADR_Dictionary = {
    'ach':['Pain'],
    'agit':['Agitation'],
    'angina':['Angina Pectoris'],
    'apnoea':['Apnea'],
    'ataxia':['Ataxia'],
    'bloat':['Abdominal bloating'],
    'breathless':['Dyspnea'],
    'burn':['Burning sensation'],
    'catch':['Catch - Finding of sensory dimension of pain'],
    'charm':['charmed'],
    'chill':['Chills'],
    'confus':['Clouded consciousness'],
    'constip':['Constipation'],
    'cough':['Coughing'],
    'cramp':['Muscle Cramp', 'Cramping sensation quality'],
    'diarrhoea':['Diarrhea'],
    'discomfort':['Malaise ', 'Actual Discomfort'],
    'dizzi':['Vertigo'],
    'dizzy':['Vertigo'],
    'dull':['Dull pain'],
    'exanthem':['Exanthema'],
    'exhaust':['Exhaustion'],
    'faint':['Syncope'],
    'fatigu':['Fatigue'],
    'fever':['Fever'],
    'feverish':['Fever'],
    'fit':['Seizures'],
    'flush':['Flushing'],
    'forget':['Forgetful'],
    'ga':['gastrointestinal gas'],
    'gasp':['Gasping for breath'],
    'giddi':['giddy mood'],
    'hangov':['Hangover from any Alcohol or Other Drugs substance', 'Hangover from alcohol'],
    'headach':['Headache'],
    'heartburn':['Heartburn'],
    'hive':['Welts'],
    'hoars':['Hoarseness'],
    'hungri':['Hunger'],
    'ill':['Malaise '],
    'imbal':['Imbalance'],
    'indigest':['Dyspepsia'],
    'insomnia':['Sleeplessness'],
    'jerk':['Spasmodic movement'],
    'lazi':['Laziness'],
    'letharg':['Lethargy'],
    'lethargi':['Lethargy'],
    'lighthead':['Lightheadedness'],
    'lightheaded':['Lightheadedness'],
    'malais':['Malaise'],
    'miser':['Depressed'],
    'nausea':['Nausea'],
    'nauseat':['Nausea'],
    'nauseou':['Nausea'],
    'nervou':['Nervousness'],
    'nervous':['Nervousness'],
    'nightmar':['Nightmares'],
    'numb':['Numbness'],
    'oedema':['Edema'],
    'pain':['Pain'],
}
def formulate():
    posts1= pandas.read_excel('askapatientLisinopril.xlsx')
    posts2= pandas.read_excel('askapatientAtenolol.xlsx')
    postsTemp = pandas.DataFrame()
    postsTemp = pandas.concat([posts1 ,posts2])
    del postsTemp['duration']
    del postsTemp['date']
    posts = pandas.DataFrame()
    postsTemp=postsTemp.fillna('X')
    col={}
    for i in postsTemp:
        l=[]
        for j in postsTemp[i]:
            if (str(postsTemp[i].dtype)=='object'):
                l.append(j)
            else:
                l.append(j.strip())
        col[i]=l
    df = pandas.DataFrame.from_dict(col)
    for i in range(len(df)):
        if df.at[i,'comments'][0]=='X' and df.at[i,'reason'][0]=='X' and df.at[i,'sideEffect'][0]=='X':
            continue
        elif df.at[i,'gender'][0]=='X'or str(df.at[i,'age'])=='X':
            continue
        else:
            posts.at[i,'Content']=''
            if not df.at[i,'Content']=='X': 
                posts.at[i,'Content']=" "+df.at[i,'comments']
            if not df.at[i,'reason']=='X': 
                posts.at[i,'Content']+=" "+df.at[i,'reason']
            if not df.at[i,'sideEffect']=='X': 
                posts.at[i,'Content']+=" "+df.at[i,'sideEffect']
            
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u'\xa0','')
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u"\u2019","")
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u'\xef',"")
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u'\u2026',"")
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u'\u2014',"")
            posts.at[i,'Content']=posts.at[i,'comments'].replace(u'\U0001f641',"")
            posts.at[i,'Content'] =str(posts.at[i,'comments'])
            if df.at[i,'gender'][0]=='F':
                posts.at[i,'gender']='Female'
            else:
                posts.at[i,'gender']='Male'
            posts.at[i,'age']=df.at[i,'age']
    posts.to_excel('askapatient.xlsx', header=True, index=False)
        
    return col,posts

#posts=pandas.read_excel('askapatient.xlsx')
#col,posts=formulate()
def TFIDF():
    posts = pandas.read_excel('askapatient.xlsx')
    stop_words =  set(stopwords.words('english'))
    for i in range(0,len(posts)):
        
        newSentence =""
        sentence=posts.iloc[i]['Content']
        for k in sentence:
            if k.isalpha() or k.isdigit() or k==' ':
                newSentence=newSentence+k
                continue
            else:
                newSentence=newSentence+" " 
                continue
        
        word_tokens = word_tokenize(newSentence) 
        filtered_sentence = [] 
        stemmed_sentence=[]
        for w in word_tokens: 
          
            if w not in stop_words: 
                filtered_sentence.append(w) 
                stemmed_sentence.append(stemmer.stem(w))
            filtered=' '.join(map(str,filtered_sentence)) 
            filtered=filtered.translate(None, string.punctuation)
            stemmed=' '.join(map(str,stemmed_sentence)) 
            stemmed=stemmed.translate(None, string.punctuation)
            posts.at[i ,'Filtered'] = filtered
            posts.at[i,'Stemmed'] = stemmed
    posts.to_excel('askapatient.xlsx')
    return posts
def mentions():
    
    '''Stemmed'''
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    posts = pandas.read_excel('askapatient.xlsx')
    listOfPosts1=posts.iloc[:]['Stemmed']
    listOfPosts2=posts.iloc[:]['Filtered']
    for i in range(0,len(listOfPosts1)):
        word_tokens1 = word_tokenize(listOfPosts1[i])
        word_tokens2 = word_tokenize(listOfPosts2[i])
        ADRList=[]
        MentalList=[]
        DiseaseList=[]
        if (i==70):
            print "spot"
        for j in word_tokens1:
            
            if j in calcium_ADR_Dictionary:
                for k in calcium_ADR_Dictionary[j]:
                    if k not in ADRList:
                        
                            
                        ADRList.append(k)
                        
                        break
            if j in calcium_Mental_Dysfunction_Dictionary:
                for k in calcium_Mental_Dysfunction_Dictionary[j]:
                    if k not in MentalList:
                        MentalList.append(k)
                        break
            if j in calcium_Disease_Dictionary:
                for k in calcium_Disease_Dictionary[j]:
                    if k not in DiseaseList:
                        DiseaseList.append(k)
                        break
                
                '''Filtered'''
                ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        for j in word_tokens2:
            if j in calcium_ADR_Dictionary:
                for k in calcium_ADR_Dictionary[j]:
                    if k not in ADRList:
                        ADRList.append(k)
                        break
            if j in calcium_Mental_Dysfunction_Dictionary:
                for k in calcium_Mental_Dysfunction_Dictionary[j]:
                    if k not in MentalList:
                        MentalList.append(k)
                        break
            if j in calcium_Disease_Dictionary:
                for k in calcium_Disease_Dictionary[j]:
                    if k not in DiseaseList:
                        DiseaseList.append(k)  
                        break
        posts.at[i,'ADRCount']=len(ADRList)
        posts.at[i,'MentalCount']=len(MentalList)
        posts.at[i,'DieaseCount']=len(DiseaseList)
        
        jsond=json.dumps(ADRList)
        posts.at[i,'ADRs']=jsond
         
        jsond=json.dumps(MentalList)
        posts.at[i,'Mentals']=jsond
        
        jsond=json.dumps(DiseaseList)
        posts.at[i,'Dieases']=jsond
            
        #to read json again
        # js = json.loads(posts.at[i,'ADRs'])
        # str(js[j])

    posts.to_excel('askapatient.xlsx')
def features():
    posts = pandas.read_excel('askapatient.xlsx')
    ADRs=pandas.DataFrame()
    DSs=pandas.DataFrame()
    Mental=pandas.DataFrame()
    for i in calcium_ADR_Dictionary:
        for j in calcium_ADR_Dictionary[i]:
            posts.at[0,j]=0
    for i in range(0,len(posts)):
        for j in calcium_ADR_Dictionary:
            for k in calcium_ADR_Dictionary[j]:
                if k in posts.at[i,'ADRs']:
                    posts.at[i,k]="1"
                    ADRs.at[i,k]="1"
                else:
                    posts.at[i,k]="0"
                    ADRs.at[i,k]="0"
    for i in calcium_Disease_Dictionary:
        for j in calcium_Disease_Dictionary[i]:
            posts.at[0,j]=0
    for i in range(0,len(posts)):
        for j in calcium_Disease_Dictionary:
            for k in calcium_Disease_Dictionary[j]:
                if k in posts.at[i,'Dieases']:
                    posts.at[i,k]="1"
                    DSs.at[i,k]="1"
                else:
                    posts.at[i,k]="0"    
                    DSs.at[i,k]="0"
    for i in calcium_Mental_Dysfunction_Dictionary:
        for j in calcium_Mental_Dysfunction_Dictionary[i]:
            posts.at[0,j]=0
        
    for i in range(0,len(posts)):
        for j in calcium_Mental_Dysfunction_Dictionary:
            for k in calcium_Mental_Dysfunction_Dictionary[j]:
                if k in posts.at[i,'Mentals']:
                    posts.at[i,k]="1"
                    Mental.at[i,k]="1"
                else:
                    posts.at[i,k]="0"
                    Mental.at[i,k]="0"
    posts.to_excel('askapatient.xlsx')
    ADRs.to_excel('ADRs.xlsx')
    DSs.to_excel('DS.xlsx')
    Mental.to_excel('Mental.xlsx')
#posts=TFIDF()
    