# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:44:37 2019

@author: Ahmed
"""


import pandas
from nltk.tokenize import word_tokenize
import string
import ast
import re
import json
calcium_Disease_Dictionary ={
    'AD':['Alzheimer disease , familial , type 3 '],
    'CH':['Cyclic neutropenia '],
    'DH':['DERMATITIS HERPETIFORMIS , FAMILIAL '],
    'ET':['Thrombocythemia , Essential '],
    'HH':['Hereditary hemochromatosis '],
    'HI':['Harlequin Fetus '],
    'HT':['Hashimoto Disease '],
    'ID':['Communicable Diseases '],
    'KD':['Mucocutaneous Lymph Node Syndrome ', 'Bulbo-Spinal Atrophy , X-Linked '],
    'NS':['Nuclear non-senile cataract '],
    'OD':['Familial Osteochondritis Dissecans '],
    'OS':['Early infantile epileptic encephalopathy with suppression bursts '],
    'VF':['Ventricular Fibrillation ', 'Ventricular Fibrillation , Paroxysmal Familial , 1 '],
    'WG':['Granulomatosis with polyangiitis '],
    'WW':['EAR WAX , WET/DRY '],
    'abscess':['Abscess '],
    'ac':['Acute Chest Syndrome '],
    'acn':['Acne Vulgaris ', 'Acne '],
    'adynamia':['adynamia '],
    'afib':['Atrial Fibrillation '],
    'ai':['Aortic Valve Insufficiency '],
    'aid':['Acquired Immunodeficiency Syndrome '],
    'aivr':['Accelerated Idioventricular Rhythm '],
    'am':['ABLEPHARON-MACROSTOMIA SYNDROME '],
    'amyloidosi':['Amyloidosis '],
    'anaphylaxi':['anaphylaxis '],
    'anemia':['Anemia '],
    'anorexia':['Anorexia '],
    'append':['Appendicitis '],
    'arb':['BESTROPHINOPATHY , AUTOSOMAL RECESSIVE '],
    'arrest':['Cardiac Arrest '],
    'arteriosclerosi':['Arteriosclerosis '],
    'arthriti':['Arthritis '],
    'asd':['ATRIAL SEPTAL DEFECT 1 '],
    'asthma':['Asthma '],
    'asthmat':['Asthma '],
    'atherosclerosi':['Arteriosclerosis ', 'Atherosclerosis '],
    'bad':['Brachial Amyotrophic Diplegia '],
    'bald':['Alopecia '],
    'behcet':['Behcet'],
    'bend':['Decompression Sickness '],
    'bo':['Dermatofibrosis lenticularis disseminata '],
    'bon':['Bisphosphonate-associated osteonecrosis '],
    'bph':['Benign Prostatic Hyperplasia '],
    'bppv':['Benign Paroxysmal Positional Vertigo '],
    'bronchiectasi':['Bronchiectasis '],
    'bronchiol':['Bronchiolitis '],
    'bronchiti':['Bronchitis '],
    'bursiti':['Bursitis '],
    'cardiomyopathi':['Cardiomyopathies '],
    'carsick':['Carsickness'],
    'cataract':['Bilateral cataracts'],
    'caviti':['Dental caries '],
    'ccf':['Congestive heart failure '],
    'cdl':['Cornelia De Lange Syndrome '],
    'cf':['Chronic Fatigue Syndrome '],
    'chc':['Pseudohyperkalemia Cardiff '],
    'chf':['Congestive heart failure '],
    'cholecyst':['Cholecystitis '],
    'cholestasi':['Cholestasis'],
    'chondriti':['Chondritis'],
    'cidp':['Polyradiculoneuropathy , Chronic Inflammatory Demyelinating '],
    'cirrhosi':['Liver Cirrhosis ', 'Cirrhosis'],
    'ckd':['Chronic Kidney Diseases '],
    'cold':['Common Cold ', 'Upper Respiratory Infections '],
    'coliti':['Colitis '],
    'condit':['Disease '],
    'copd':['Copd', 'Chronic obstructive pulmonary disease of horses '],
    'costochondr':["Tietze 's Syndrome "],
    'crohn':['Crohns'],
    'croup':['Croup '],
    'cryoglobulinaemia':['Cryoglobulinaemia'],
    'css':['Coffin-Siris syndrome '],
    'ct':['Carpal Tunnel Syndrome '],
    'curb':['Curb', 'Curb '],
    'cva':['Cva'],
    'cvd':['Cvd'],
    'cyst':['Cyst '],
    'cystocel':['Cystocele'],
    'dandruff':['Seborrheic dermatitis of scalp ', 'Scurfiness of scalp '],
    'ddd':['dowling-degos disease '],
    'defici':['Malnutrition '],
    'deficit':['Deficit'],
    'dehydr':['Dehydration '],
    'dengu':['Dengue Fever '],
    'dermatomyos':['Dermatomyositis ', 'Dermatomyositis'],
    'di':['Deafness , Sensorineural , And Male Infertility '],
    'diabet':['Diabetes', 'Diabetes Mellitus '],
    'diseas':['Disease', 'Disease '],
    'dish':['Hyperostosis , Diffuse Idiopathic Skeletal '],
    'disord':['Disease '],
    'diverticul':['Diverticulitis '],
    'diverticulosi':['Diverticulosis '],
    'dlb':['Lewy Body Disease '],
    'dress':['Drug Hypersensitivity Syndrome '],
    'duoden':['Duodenitis '],
    'dvt':['Dvt', 'Deep thrombophlebitis '],
    'dysautonomia':['Dysautonomia '],
    'dyscinesia':['Dyskinetic syndrome '],
    'dysfunct':['DYSFUNCTION - SKIN DISORDERS '],
    'dysmenorrhoea':['Dysmenorrhea '],
    'dystonia':['Dystonia Disorders '],
    'eclampsia':['Eclampsia '],
    'ect':['Benign Rolandic Epilepsy '],
    'eiph':['Bleeder syndrome '],
    'emphysema':['Pulmonary Emphysema '],
    'encephalopathi':['Encephalopathies '],
    'endo':['Endometriosis '],
    'endometriosi':['Endometriosis '],
    'enuresi':['Enuresis ', 'Urinary incontinence of non-organic origin '],
    'epilepsi':['Epilepsy '],
    'epstein':['Epstein'],
    'erythema':['Erythema '],
    'fad':['Pena-Shokeir syndrome type I '],
    'fed':['Fish-Eye Disease '],
    'fibril':['Fibrillation '],
    'fibromyalgia':['Fibromyalgia '],
    'flash':['Photopsia '],
    'flicker':['Photopsia '],
    'flu':['Influenza '],
    'fmd':['Fibromuscular Dysplasia ', 'Muscular Dystrophy , Facioscapulohumeral '],
    'gallston':['Gallstone', 'Cholecystolithiasis ', 'Cholelithiasis '],
    'gastriti':['Gastritis '],
    'gastroenter':['Gastroenteritis '],
    'gastroparesi':['Gastroparesis '],
    'gastropathi':['Stomach Diseases '],
    'gerd':['Gastroesophageal reflux disease '],
    'gist':['PARAGANGLIOMA AND GASTRIC STROMAL SARCOMA '],
    'glass':['Chromosome 2q32-Q33 Deletion Syndrome '],
    'glaucoma':['Glaucoma '],
    'glomerular':['Renal glomerular disease '],
    'glomerulonephr':['Glomerulonephritis '],
    'gout':['Gout '],
    'grip':['Influenza '],
    'gripp':['Influenza '],
    'haemochromatosi':['Hemochromatosis '],
    'haemorrhoid':['Hemorrhoids '],
    'hashitoxicosi':['Hyperthyroidism with Hashimoto disease '],
    'hav':['Hepatitis A '],
    'hdl3':['HUNTINGTON DISEASE-LIKE 3'],
    'hdlc':['Hypoalphalipoproteinemia , Familial '],
    'heav':['Chronic obstructive pulmonary disease of horses '],
    'helix':['HELIX SYNDROME '],
    'hematuria':['Hematuria '],
    'hemochromatosi':['HEMOCHROMATOSIS , TYPE 1 '],
    'hemorrhoid':['Hemorrhoids '],
    'hemotympanum':['Hematotympanum '],
    'hepat':['Hepatitis ', 'Hepatitis A '],
    'herp':['herpes '],
    'hit':['Heparin-induced thrombocytopenia '],
    'hive':['Urticaria '],
    'htn':['Hypertensive disease '],
    'hyperaldosteron':['Hyperaldosteronism '],
    'hyperlipidaemia':['Hyperlipidaemia'],
    'hyperparathyroid':['Hyperparathyroidism '],
    'hypertens':['Hypertensive disease '],
    'hyperthyroid':['Hyperthyroidism '],
    'hypoglycemia':['Hypoglycemia '],
    'hyponatremia':['Hyponatremia '],
    'hypothyroid':['Hypothyroidism '],
    'ib':['Irritable Bowel Syndrome '],
    'ic':['Kartagener Syndrome '],
    'iddm':['Diabetes Mellitus , Insulin-Dependent '],
    'ie':['Subacute Bacterial Endocarditis '],
    'incl':['Infantile neuronal ceroid lipofuscinosis '],
    'incontin':['Incontinence '],
    'infect':['Infection'],
    'influenza':['Influenza '],
    'lah':['HYPOTRICHOSIS 6 '],
    'lbbb':['Left Bundle-Branch Block '],
    'lca':['Amaurosis congenita of Leber , type 1 '],
    'lordosi':['Lordosis '],
    'lupu':['Lupus Vulgaris ', 'Lupus Erythematosus , Discoid ', 'Lupus Erythematosus '],
    'lvf':['Left-Sided Heart Failure '],
    'lvh':['Left Ventricular Hypertrophy '],
    'lymphaden':['Lymphadenitis '],
    'lymphadenopathi':['Lymphadenopathy '],
    'lymphoedema':['Lymphedema '],
    'ma':['Macrophage Activation Syndrome '],
    'malaria':['Malaria '],
    'measl':['Measles '],
    'med':['MICROCEPHALY , EPILEPSY , AND DIABETES SYNDROME '],
    'mf':['Marfan Syndrome '],
    'mg':['MUNGAN SYNDROME '],
    'mh':['Malignant hyperpyrexia due to anesthesia '],
    'microangiopathi':['Disease of capillaries '],
    'migrain':['Migraine Disorders '],
    'mona':['TORG-WINCHESTER SYNDROME '],
    'morphea':['Localized scleroderma '],
    'morphoea':['Morphea '],
    'mpgn':['Glomerulonephritis , Membranoproliferative '],
    'msd':['Multiple Sulfatase Deficiency Disease '],
    'multi':['Multiple Chronic Conditions '],
    'mump':['Mumps '],
    'myocard':['Myocarditis '],
    'myopathi':['Myopathy '],
    'myositi':['Myositis '],
    'nash':['Fatty Liver Disease '],
    'nasopharyng':['Nasopharyngitis '],
    'nearsight':['Myopia '],
    'nephropathi':['Kidney Diseases '],
    'neuropathi':['Neuropathy '],
    'nod':['Dentatorubral-Pallidoluysian Atrophy '],
    'nph':['Hydrocephalus , Normal Pressure '],
    'nstemi':['Non-ST Elevated Myocardial Infarction '],
    'nystagmu':['Nystagmus '],
    'obes':['Obesity '],
    'oesophag':['Esophagitis '],
    'osteoarthr':['Degenerative polyarthritis '],
    'osteopathi':['Osteopathy'],
    'osteophyt':['External exotoses ', 'Osteophyte '],
    'osteoporosi':['Osteoporosis '],
    'otiti':['Ear Inflammation ', 'Infection of ear '],
    'pac':['Atrial Premature Complexes '],
    'pan':['POLYARTERITIS NODOSA , CHILDHOOD-ONSET '],
    'pancreat':['Pancreatitis '],
    'park':['PARKINSON DISEASE , LATE-ONSET '],
    'pco':['Polycystic Ovary Syndrome '],
    'pcp':['Pneumocystis jiroveci pneumonia '],
    'pdr':['Proliferative diabetic retinopathy ', 'PIGMENTARY DISORDER , RETICULATE , WITH SYSTEMIC MANIFESTATIONS '],
    'pericard':['Pericarditis '],
    'pit':['Van der Woude syndrome '],
    'pituitari':['Pituitary Diseases '],
    'pl':['Papillon-Lefevre Disease '],
    'plagu':['Plague'],
    'plan':['Infantile Neuroaxonal Dystrophy '],
    'plaqu':['Dental Plaque '],
    'pleurisi':['Pleurisy '],
    'pmd':['Pelizaeus-Merzbacher Disease ', 'ANOPHTHALMIA AND PULMONARY HYPOPLASIA '],
    'pnd':['Paroxysmal nocturnal dyspnea '],
    'pneumocephalu':['Pneumocephalus'],
    'pneumonia':['Pneumonia '],
    'polyarthralgia':['Polyarthralgia '],
    'porphyria':['Disorders of Porphyrin Metabolism '],
    'pre-diabet':['Prediabetes syndrome '],
    'prediabet':['Prediabetes syndrome '],
    'prehypertens':['Prehypertension'],
    'proctiti':['Proctitis '],
    'prolaps':['Ptosis '],
    'prostat':['prostatitis '],
    'psoriasi':['Psoriasis '],
    'psvt':['Paroxysmal supraventricular tachycardia '],
    'purg':['Purging'],
    'pvc':['Pvc', 'Premature ventricular contractions '],
    'pvr':['Proliferative vitreoretinopathy '],
    'quinsi':['Peritonsillar Abscess '],
    'radiculopathi':['Radiculopathy '],
    'raynaud':['Raynaud Disease '],
    'rbbb':['Right bundle branch block '],
    'red':['Erythema '],
    'regress':['Developmental regression '],
    'relaps':['Recurrent disease '],
    'renovascular':['Renal vascular disorder '],
    'rhc':['SKIN/HAIR/EYE PIGMENTATION , VARIATION IN , 2'],
    'rhiniti':['Rhinitis '],
    'rl':['Restless Legs Syndrome '],
    'rosacea':['Rosacea '],
    'rubella':['Rubella '],
    'rubeola':['Measles '],
    'sarcoidosi':['Sarcoidosis '],
    'sbe':['Subacute Bacterial Endocarditis '],
    'scleroderma':['Scleroderma ', 'Systemic Scleroderma '],
    'sepsi':['Septicemia ', 'Sepsis '],
    'septicaemia':['Septicaemia'],
    'septicemia':['Sepsis '],
    'sid':['Sudden infant death syndrome '],
    'sinus':['Sinusitis '],
    'soft':['SHORT STATURE , ONYCHODYSPLASIA , FACIAL DYSMORPHISM , AND HYPOTRICHOSIS SYNDROME '],
    'spondyl':['Spondylitis'],
    'spondylodisk':['Discitis '],
    'stagger':['Cerebellar decompression injury '],
    'stare':['Staring '],
    'steatohepat':['Steatohepatitis'],
    'steatosi':['Steatohepatitis '],
    'strep':['Streptococcal Infections '],
    'stroke':['Cerebrovascular accident '],
    'struck':['Struck'],
    'svt':['Supraventricular tachycardia '],
    'tendon':['Tendinitis '],
    'tetani':['Tetany '],
    'thyroid':['Thyroiditis '],
    'thyrotoxicosi':['Thyrotoxicosis '],
    'tia':['Transient Ischemic Attack ', 'Transient Cerebral Ischemia '],
    'tingl':['Paresthesia '],
    'tk':['TAKENOUCHI-KOSAKI SYNDROME '],
    'toxaemia':['Septic Toxemia '],
    'toxemia':['Septicemia ', 'Bacterial Toxemia '],
    'toxoplasmosi':['Toxoplasmosis '],
    'ulcer':['Ulcer '],
    'urticaria':['Urticaria '],
    'uti':['Urinary tract infection '],
    'v':['V'],
    'varic':['Varicosity '],
    'varix':['Varicosity '],
    'vascul':['Vasculitis '],
    'vcjd':['New Variant Creutzfeldt-Jakob Disease '],
    'vfib':['Ventricular Fibrillation '],
    'wast':['Wasting '],
    'wpw':['Wolff-Parkinson-White Syndrome '],
    'wss':['Weaver syndrome ', 'Wrinkly skin syndrome '],
    'yaw':['Yaws '],
    'zona':['Herpes zoster disease '],
}

calcium_Mental_Dysfunction_Dictionary ={
    'abus':['Drug abuse '],
    'addict':['Addictive Behavior '],
    'adhd':['Attention deficit hyperactivity disorder '],
    'agoraphobia':['Agoraphobia '],
    'alcohol':['Alcoholic Intoxication , Chronic '],
    'analgesia':['Agnosia for Pain '],
    'anxieti':['Anxiety ', 'Anxiety Disorders '],
    'anxiou':['Anxiety '],
    'anxious':['Anxiety '],
    'apathi':['Apathy '],
    'aphasia':['Aphasia '],
    'asd':['Autism Spectrum Disorders '],
    'autism':['Autistic Disorder '],
    'bing':['Binge eating disorder '],
    'blackout':['Alcoholic blackout '],
    'block':['Mental blocking '],
    'caffein':['Caffeine related disorders '],
    'confus':['Confusion '],
    'daze':['Confusion '],
    'depress':['Mental Depression ', 'Depressive disorder '],
    'dereal':['Derealization'],
    'despond':['despondency '],
    'disori':['Disorientation '],
    'disorient':['Confusion ', 'Disorientation '],
    'drowsi':['Somnolence '],
    'drunk':['Alcoholic Intoxication ', 'Acute alcoholic intoxication '],
    'dysthymia':['Dysthymic Disorder '],
    'enuresi':['Bedwetting '],
    'flash':['Flashing'],
    'flashback':['Hallucinogen Persisting Perception Disorder '],
    'forget':['forgetting ', 'Forgetting'],
    'frenzi':['Frenzy'],
    'gad':['Generalized Anxiety Disorder '],
    'hallucin':['Hallucinations '],
    'hyper':['Hyperactive behavior '],
    'hypervigil':['Hypervigilance'],
    'hypochondria':['Hypochondriasis '],
    'icd':['Disruptive , Impulse Control , and Conduct Disorders '],
    'impati':['Impatience'],
    'manic':['Manic'],
    'mci':['Mild cognitive disorder '],
    'mdi':['MAJOR AFFECTIVE DISORDER 2 '],
    'moodi':['Mood swings '],
    'neurosi':['Neurotic Disorders '],
    'nightmar':['Nightmare', 'Nightmares'],
    'obsess':['Obsessions '],
    'ocd':['Obsessive-Compulsive Personality ', 'Obsessive-Compulsive Disorder '],
    'person':['As If Personality '],
    'phobia':['Phobic anxiety disorder '],
    'pot':['Marijuana Abuse '],
    'psych':['Psychiatric problem '],
    'psycholog':['Psychiatric problem '],
    'psychot':['Psychotic'],
    'ptsd':['Post-Traumatic Stress Disorder '],
    'pund':['Punding'],
    'schizophrenia':['Schizophrenia '],
    'sleepi':['Somnolence '],
    'somat':['Somatization '],
    'somnol':['Somnolence '],
    'spray':['Spraying behavior '],
    'ssd':['Speech Sound Disorders'],
    'stubborn':['Stubbornness'],
    'suffer':['Mental Suffering'],
    'tens':['Tension'],
    'tension':['Tension'],
    'violent':['violent'],
    'weed':['Marijuana Abuse'],
    'withdraw':['Withdrawal dysfunction'],
}
calcium_ADR_Dictionary ={
    'ach':['Pain', 'Ache'],
    'agit':['Agitation'],
    'ailment':['Illness'],
    'angina':['Angina Pectoris'],
    'Apnea':['Apnea'],
    'apnoea':['Apnea'],
    'arthralgia':['Arthralgia'],
    'ataxia':['Ataxia', 'Cerebellar Ataxia'],
    'belch':['Eructation'],
    'blackout':['Syncope', 'Blackout - symptom'],
    'bloat':['Abdominal bloating'],
    'blotchi':['Blotchy'],
    'blush':['Blushing'],
    'breathless':['Dyspnea'],
    'burn':['Burning sensation'],
    'burp':['Eructation'],
    'chill':['Chills'],
    'clumsi':['Clumsiness'],
    'confus':['Clouded consciousness'],
    'constip':['Constipation'],
    'convuls':['Seizures', 'Convulsions'],
    'cough':['Coughing'],
    'cramp':['Muscle Cramp', 'Cramping sensation quality'],
    'daze':['Clouded consciousness'],
    'diarrhoea':['Diarrhea'],
    'discomfort':['Malaise', 'Actual Discomfort'],
    'dizzi':['Vertigo', 'Dizziness'],
    'dizzy':['Dizziness'],
    'doe':['Dyspnea on exertion'],
    'dull':['Dull pain'],
    'dyspnoea':['Dyspnea'],
    'dystonia':['Dystonia'],
    'ear ache':['Earache'],
    'exert':['exercise induced'],
    'exhaust':['Exhaustion'],
    'faint':['Syncope'],
    'fascicul':['Muscular fasciculation'],
    'fatigu':['Fatigue'],
    'fever':['Fever'],
    'fit':['Seizures'],
    'flare':['Flare'],
    'floppi':['Floppy'],
    'fluctuat':['Fluctuation'],
    'flush':['Flushing', 'Blushing'],
    'gas':['gastrointestinal gas'],
    'gasp':['Gasping for breath'],
    'giddi':['giddy mood ', 'Dizziness and giddiness symptoms ', 'giddiness' , 'Vertigo'],
    'gurgl':['Gurgling'],
    'halo':['Visual halos'],
    'hangov':['Hangover from any Alcohol or Other Drugs substance ', 'Hangover from alcohol'],
    'headach':['Headache'],
    'heartburn':['Heartburn'],
    'hemiplegia':['Hemiplegia'],
    'hive':['Welts'],
    'hoars':['Hoarseness'],
    'hunger':['Hunger'],
    'hungri':['Hunger'],
    'ill':['Malaise', 'Illness'],
    'imbal':['Imbalance'],
    'indigest':['Dyspepsia'],
    'insomnia':['Sleeplessness'],
    'jaundic':['Icterus'],
    'jerk':['Spasmodic movement'],
    'lazi':['Laziness'],
    'letharg':['Lethargy'],
    'lethargi':['Lethargy'],
    'lighthead':['Lightheadedness'],
    'lightheaded':['Dizziness', 'Lightheadedness'],
    'malais':['Malaise'],
    'mass':['Mass of body region'],
    'miser':['Depressed - symptom'],
    'nausea':['Nausea'],
    'nauseat':['Nausea'],
    'nauseou':['Nausea'],
    'nervou':['Nervousness'],
    'nervous':['Nervousness', 'Feeling nervous'],
    'nightmar':['Nightmares'],
    'numb':['Numbness'],
    'oedema':['Edema'],
    'oedemat':['Edema'],
    'pain':['Pain'],
    'photophobia':['Photophobia'],
    'polyuria':['Polyuria'],
    'pre-syncop':['Presyncope'],
    'prickl':['Prickling sensation'],
    'qol':['Perceived quality of life'],
    'quiver':['Tremor', 'Involuntary Quiver'],
    'rash':['Exanthema'],
    'regurgit':['Regurgitation'],
    'restless':['Agitation', 'Restlessness'],
    'rigor':['Muscle Rigidity', 'Rigor - Temperature-associated observation'],
    'rundown':['Rundown'],
    'seizur':['Seizures', 'Seizures'],
    'shake':['Tremor'],
    'sick':['Illness'],
    'sigh':['Sighing respiration'],
    'sleepless':['Sleeplessness'],
    'sluggish':['Sluggishness'],
    'sneez':['Sneezing'],
    'snore':['Snoring'],
    'sob':['Dyspnea'],
    'sore':['Sore to touch', 'Sore skin'],
    'spasm':['Muscle Cramp', 'Spasm', 'Spasm'],
    'spastic':['Muscle Spasticity'],
    'spell':['spells'],
    'spot':['Exanthema ', 'Spots on skin ', 'Menstrual spotting'],
    'stagger':['Staggering gait'],
    'stiff':['Muscular stiffness'],
    'suffoc':['Suffocated'],
    'swell':['Edema'],
    'syncop':['Syncope'],
    'tender':['Sore to touch'],
    'tens':['Feeling tense'],
    'tingl':['Has tingling sensation'],
    'tinnitu':['Tinnitus'],
    'tire':['Fatigue', 'Tired'],
    'tired':['Fatigue'],
    'trembl':['Trembling', 'Tremor'],
    'tremor':['Tremor'],
    'trigemini':['Pulsus trigeminus'],
    'vertigo':['Vertigo'],
    'vomit':['Vomiting'],
    'wast':['Cachexia'],
    'weak':['Weakness'],
    'wheez':['Wheezing'],
    'wheezi':['Wheezing'],
    'woozi':['Dizziness'],

}
age_related_list=[
      'age',
      'years',
      'year',
      'yrs',
      'yr',
      'old',
      'yo',
      'am',
      "m",
      "a",
      "of",
      "now",
      'y/o',
      "im",
      "Im",
      "is",
      "at"
]

drugList={
        "Nadolol":["Nadolol","Beta"],
        "Amlodipine":["Amlodipine","Calcium"],
        "Diltiazem":["Diltiazem","Calcium"],
        "Hydrochlorothiazide":["Hydrochlorothiazide","Diuretics"],
        "Atenolol":["Atenolol","Beta"],
        "Lisinopril":["Lisinopril","Angiotensin"],
}

posts= pandas.read_csv('CurrentPosts.csv')

listOfPosts1=posts.iloc[:]['Stemmed']
listOfPosts2=posts.iloc[:]['Filtered']
for i in posts.columns:
    if "Unnamed" in i:
        posts=posts.drop(columns=[i])
def drugs():
    for i in range(0,len(posts)):
        drug= posts.iloc[i]['Drug']
        if drug in drugList:
            drug= posts.iloc[i]['Drug']
            drugfamily=drugList[drug][1]
            posts.at[i,'DrugFamily']=drugfamily
            posts.at[i,'Drug']=drugList[drug][0]
        
        
    posts.to_csv('CurrentPosts.csv')
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
                    k=w.split('/')
                    if(k[0]!='' and int(k[0])>12):
                        presure.append(w)
            filtered=' '.join(map(str,presure)) 
            filtered=filtered.translate(None, string.punctuation)
            #posts.at[i ,'Filtered'] = filtered
        
        posts.at[i,'pressures']= str(presure)
    posts.to_csv('CurrentPosts.csv')

def age():
    
    file_object2  = open("age.txt", "w")
    j=0
    
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
        
        
        x=any(char.isdigit() for char in word_tokens[0])
        y=('/' not in word_tokens[0])
        z=(word_tokens[1] in age_related_list)
        b=(any(w in word_tokens[0] for w in age_related_list))
            
        age=[]
        if (x and y and (z or b)):
            age.append(word_tokens[0])
        for k in range(1,len(word_tokens)-1): 
            x=any(char.isdigit() for char in word_tokens[k])
            y=('/' not in word_tokens[k])
            z=(word_tokens[k-1] in age_related_list)
            a=(word_tokens[k+1] in age_related_list)
            b=(any(w in word_tokens[k] for w in age_related_list))
            c=('mg' not in word_tokens[k+1])
            d=('mg' not in word_tokens[k-1])
            e=('mg' not in word_tokens[k])
            if (x and y and (z or a or b) and c and d and e):
                file_object2.write(str(j)+": "+word_tokens[k]+" "+str(x)+" "+str(y)+" "+str(z)+" "+str(a)+" "+str(b)+'\n')
                age.append(word_tokens[k-1]+word_tokens[k]+word_tokens[k+1])
            filtered=' '.join(map(str,age)) 
            filtered=filtered.translate(None, string.punctuation)
            
            #posts.at[i ,'Filtered'] = filtered
        posts.at[j,'years1']= str(age)
        j+=1
       
        #print ""
    posts.to_csv('CurrentPosts.csv')
    file_object2.close()       
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

    posts.to_csv('CurrentPosts.csv')
def height():
    for i in range(0,len(posts)):
        
        newSentence =""
        sentence=posts.iloc[i]['Content']
        height=[[],[]]
        ch=""
        isHeight=False
        for k in range(0,len(sentence)):
            if sentence[k].isdigit():
                isHeight=True
            if isHeight==True and (sentence[k].isdigit() or sentence[k]=="'" or sentence[k]=="\"" or sentence[k]=="-"):
                ch+=sentence[k]
            elif isHeight==True and not (sentence[k].isdigit() or sentence[k]=="'" or sentence[k]=="\"" or sentence[k]=="-"):
                isHeight=False
                
                if "\"" in ch or "'"in ch:
                    height[0].append(ch)
                
                ch=""
            if (sentence[k].isalpha()) or sentence[k].isdigit() or sentence[k]==' ' or sentence[k]=="/":
                newSentence=newSentence+sentence[k]
                continue
            else:
                newSentence=newSentence+" " 
                continue
        word_tokens = word_tokenize(newSentence)
        posts.at[i,'heights']=str(height)
        
       
        #print ""
    posts.to_csv('CurrentPosts.csv')
def features():
    for i in calcium_ADR_Dictionary:
        for j in calcium_ADR_Dictionary[i]:
            posts.at[0,j]=""
    for i in range(0,len(posts)):
        for j in calcium_ADR_Dictionary:
            for k in calcium_ADR_Dictionary[j]:
                if k in posts.at[i,'ADRs']:
                    posts.at[i,k]="1"
                else:
                    posts.at[i,k]="0"
    posts.to_csv('CurrentPosts.csv')
def feetToCM():
    for i in range(0,len(posts)):
        feet=posts.iloc[i]['Inches']
        feet=ast.literal_eval(feet)[0]
        if len(feet)!=0:
            feet=feet[0].split('-')
            cm=30.48*int(feet[0])+ 2.54*int(feet[1])
            posts.at[i,"Height"]=int(cm)
    posts.to_csv('CurrentPosts.csv')
#feetToCM()
#features()
#mentions()
#age()
#pressure()