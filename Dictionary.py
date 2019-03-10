# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:44:37 2019

@author: Ahmed
"""


import pandas
from nltk.tokenize import word_tokenize
import string

calcium_Disease_Dictionary ={
        "abcess":["ABSCESS"],
        "abscess":["ABSCESS"],
        "ad":["Alzheimer disease"],
        "adynamic":["Adynamia"],
        "afib":["Atrial Fibrillation"],
        "appendicitis":["Appendicitis"],
        "arthritis":["Arthritis"],
        "asthma":["Asthma"],
        "atherosclerosis":["Arteriosclerosis"],
        "bph":["Benign Prostatic Hyperplasia"],
        "bronchitis":"Bronchitis",
        "cardiomyopathy":["Cardiomyopathies"],
        "cataracts":["Cataracts"],
        "ccf":["Congestive heart failure"],
        "chf":["Congestive heart failure"],
        "cholecystitis":["Cholecystitis"],
        "cholestasis":["Cholestasis"],
        "cidp":["CIDP"],
        "cirrhosis":["Liver Cirrhosis"],
        "cn":["CN"],
        "cold":["Common Cold","Upper Respiratory Infections"],
        "copd":["COPD NOS","Chronic obstructive pulmonary disease of horses"],
        "crohn":["Crohn Disease"],
        "cvd":["Cardiovascular Diseases"],
        "cyst":["Cyst"],
        "dandruff":["Seborrheic dermatitis of scalp","Scurfiness of scalp"],
        "deficiency":["Malnutrition"],
        "deydr":["Dehydration"],
        "diabet":["Diabetes"],
        "disorder":["Disorder"],
        "diverticulitis":["Diverticulitis"],
        "duodenitis":["Duodenitis"],
        "dysautonomia":["Dysautonomia"],
        "dysfunction":["Dysfunction"],
        "eco":["Endocrine-Cerebroosteodysplasia"],
        "eiph":["Bleeder syndrome"],
        "endo":["Endometriosis"],
        "esophagitis":["Esophagitis"],
        "fibrillation":["Fibrillation"],
        "flu":["Influenza"],
        "gallston":["Gallstone"],
        "gastritis":["Gastritis"],
        "gastroparesis":["Gastroparesis"],
        "gerd":["Gastroesophageal reflux disease"],
        "grip":["Influenza"],
        "haemotympanum":["Hemotympanum"],
        "hashitoxicosis":["Hyperthyroidism"],
        "hdlc":["Hypoalphalipoproteinemia, Familial"],
        "hemorrhoid":["Haemorrhoid"],
        "hepatitis":["Hepatitis"],
        "herpes":["Herpes"],
        "hh":["Hereditary hemochromatosis"],
        "hive":["Urticaria"],
        "htn":["Hypertensive disease"],
        "hypertension":["Hypertension"],
        "hyperthyroid":["Hyperthyroidism"],
        "hyponatremia":["Hyponatremia"],
        "hypothyroid":["Hypothyroidism"],
        "incl":["INCL"],
        "infect":["Communicable Diseases"],
        "influenza":["INFLUENZA"],
        "inhibit":["Cardiac Arrest"],
        "lordosis":["Lordosis"],
        "lupus":["Lupus"],
        "lvh":["Left Ventricular Hypertrophy"],
        "lymphadenitis":["Lymphadenitis"],
        "lymphedema":["Lymphedema"],
        "measles":["Measles"],
        "migrain":["Migraine"],
        "myopathies":["Myopathy"],
        "myositis":["Myositis"],
        "nasopharyngitis":["Nasopharyngitis"],
        "neuropathy":["Neuropathy"],
        "obes":["Obesity"],
        "osteoarthritis":["Degenerative polyarthritis"],
        "osteophytes":["External exotoses","Osteophyte"],
        "osteoporosis":["Osteoporosis"],
        "otitis":["Ear Inflammation"],
        "pacs":["Atrial Premature Complexes"],
        "pancreatitis":["Pancreatitis"],
        "pituitary":["Pituitary Diseases"],
        "pcp":["Pneumocystis jiroveci pneumonia"],
        "porphyria":["Disorders of Porphyrin Metabolism"],
        "prolapse":["Ptosis"],
        "pvc":["Premature ventricular contractions"],
        "pvr":["Proliferative vitreoretinopathy"],
        "quinsy":["Peritonsillar Abscess"],
        "radiculopathy":["Radiculopathy"],
        "red":["Erythema"],
        "renovascular":["Renal vascular disorder"],
        "rhc":["RHC"],
        "rubella":["Rubella"],
        "sepsis":["Septicemia","Sepsis"],
        "sinusitis":["Sinusitis"],
        "spondylitis":["Spondylitis"],
        "spondylodiscitis":["Discitis"],
        "strep":["Streptococcal Infections"],
        "stroke":["Cerebrovascular accident"],
        "svt":["Supraventricular tachycardia"],
        "thi":["Transient hypogammaglobulinemia of infancy"],
        "thyroiditis":["Thyroiditis"],
        "thyrotoxicosis":["Thyrotoxicosis"],
        "tia":["Transient Ischemic Attack","Transient Cerebral Ischemia"],
        "tingling":["Paresthesia"],
        "ulcer":["Ulcer"],
        "urticaria":["Urticaria"],
        "varices":["Varicosity"],
        "vasculitis":["Vasculitis"],
        "vfib":["Ventricular Fibrillation"],
        "vtach":["Tachycardia, Ventricular"],
        "wpw":["Wolff-Parkinson-White Syndrome"],
}

calcium_Mental_Dysfunction_Dictionary ={
        "abuse":["Drug Abuse"],
        "addict":["Addictive behavior"],
        "agoraphobia":["Agoraphobia"],
        "analgesia":["Agnosia for Pain"],
        "anxious":["Anxiety"],
        "bing":["Binge eating disorder"],
        "blocking":["Mental blocking"],
        "confus":["Confusion"],
        "caffein":["Caffeine related disorders"],
        "depress":["Depression"],
        "disoriented":["Disorientation"],
        "drowsiness":["Somnolence"],
        "flashback":["Hallucinogen Persisting Perception Disorder"],
        "forget":["forgetting"],
        "forgot":["forgetting"],
        "hyper":["Hyperactive behavior"],
        "icd":["Disruptive, Impulse Control, and Conduct Disorders"],
        "inhibit":["Mental blocking"],
        "Nightmares":["Nightmare Disorder"],
        "pot":["Marijuana Abuse"],
        "ptsd":["PTSD"],
        "sleepiness":["Somnolence"],
        "somnolence":["Somnolence"],
        "stubborn":["Stubbornness"],
        "stun":["Confusion"],
        "suffer":["Mental Suffering"],
        "violent":["VIOLENT"],
        "withdrawal":["Withdrawal"]
}
calcium_ADR_Dictionary ={
  "ache":["Pain","Ache"],
  "angina": ["Angina Pectoris"],
  "apnea": ["APNOEA"],
  "ailment":["Illness"],
  "belch": ["Eructation"],
  "bloat":["Abdominal bloating"],
  "blotchy":["Blotchy"],
  "breathless":["Dyspnea"],
  "burning":["Burning sensation"],
  "confus":["Clouded consciousness"],
  "constipation":["Constipation"],
  "convulsions":["Seizures"],
  "cough":["Coughing"],
  "cramp":["Muscle Cramp","Cramping sensation quality"],
  "diarrhea":["Diarrhea"],
  "discomfort":["Malaise","Actual Discomfort"],
  "dizzy":["Dizziness"],
  "doe":["Dyspnea","Dyspnea on exertion"],
  "dull":["Dull pain"],
  "exhaust":["Exhaustion"],
  "faint":["Syncope"],
  "fatigu":["Fatigue"],
  "fever":["Fever"],
  "fit":["Seizures"],
  "Flare":["flare"],
  "flush":["Flush"],
  "fluctuation":["Fluctuation"],
  "gasp":["Gasping for breath"],
  "gas":["gastrointestinal gas"],
  "headache":["Headache"],
  "hungry":["Hungry"],
  "heartburn":["Heartburn"],
  "hive":["Welts"],
  "ill":["Malaise"],
  "indigestion":["Dyspepsia"],
  "insomnia":["Sleeplessness"],
  "jerk":["Spasmodic movement"],
  "lazy":["Laziness"],
  "lethargic":["Lethargy"],
  "lightheaded":["Lightheadedness"],
  "malaise":["Malaise"],
  "miserable":["Depressed"],
  "misery":["Depressed"],
  "nausea":["Nausea"],
  "nervous":["Nervousness"],
  "nightmares":["Nightmares"],
  "numb":["Numbness"],
  "pain":["Pain"],
  "prickling":["Prickling sensation"],
  "rash":["Exanthema"],
  "regurgitation":["Regurgitation"],
  "restless":["Agitation","Restlessness"],
  "rigor":["Muscle Rigidity","Temperature-associated observation"],
  "seizure":["Seizures"],
  "shake":["Tremor"],
  "sick":["Illness"],
  "sleepless":["Sleepless"],
  "sneeze":["Sneezing"],
  "snore":["Snoring"],
  "sob":["Dyspnea"],
  "sore":["Sore to touch","Sore skin"],
  "spasm":["Muscle Cramp","Spasm"],
  "spell":["Spells"],
  "spot":["Exanthema","Spots on skin","Menstrual spotting"],
  "stiff":["Muscular stiffness"],
  "stun":["Clouded consciousness"],
  "swell":["Edema"],
  "syncop":["Syncope"],
  "tingling":["Tingling sensation"],
  "tired":["Fatigue"],
  "tremble":["Trembling"],
  "tremor":["Tremor"],
  "trigemini":["Pulsus trigeminus"],
  "vertigo":["Vertigo"],
  "vomit":["Vomiting"],
  "weak":["Weakness"],
  "wheeze":["Wheezing"]
}


posts= pandas.read_csv('Calcium.csv')

listOfPosts1=posts.iloc[:]['Stemmed']
listOfPosts2=posts.iloc[:]['Filtered']

def pressure():
    for i in range(0,len(posts)):
        newSentence =""
        sentence=posts.iloc[i]['Content']
        for k in sentence:
            if (k.isalpha()) or k.isdigit() or k==' ' or k=="/":
                newSentence=newSentence+k
                continue
            else:
                newSentence=newSentence+" " 
                continue
        word_tokens = word_tokenize(newSentence)
        presure=[]
        for w in word_tokens: 
            if ('/' in w ):
                if (any(c.isalpha() for c in w))==False:
                    presure.append(w)
            filtered=' '.join(map(str,presure)) 
            filtered=filtered.translate(None, string.punctuation)
            #posts.at[i ,'Filtered'] = filtered
        print presure
        print ""
            
def mentions():
    
    '''Stemmed'''
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    for i in range(0,len(listOfPosts1)):
        word_tokens1 = word_tokenize(listOfPosts1[i])
        word_tokens2 = word_tokenize(listOfPosts2[i])
        ADRList=[]
        MentalList=[]
        DiseaseList=[]
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
        posts.at[i,'DieaseCount']=len(MentalList)
        posts.at[i,'MentalCount']=len(DiseaseList)
        #if len(ADRList)==0:
            #posts.at[i,'ADRs']=ADRList
        #if len(MentalList)==0:     
            #posts.at[i,'Dieases']=MentalList
        #if len(DiseaseList)==0:    
            #posts.at[i,'Mentals']=DiseaseList

    posts.to_csv('Calcium.csv')