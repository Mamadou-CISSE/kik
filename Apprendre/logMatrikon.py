# -*- coding: utf-8 -*-
__author__ = "Mamadou CISSE"
__email__ = "cissemamadou2006@yahoo.fr"
__license__ = "None"

import re
import pandas as pd


#Fonction pour ouvrir un fichier avec python
def ouvrir(monfichier):
    return open(monfichier,'r', encoding = "ISO-8859-1")


############################ Fonction pour trouver  une ligne particulière du fichier########################################################
def trouveLine(line):
    matchThis = ""
    matched = re.match(r'\[\d\d/\d\d \d\d:\d\d:\d\d.\d+\]\(\d+,\d+\).+::', line)
    if matched:
        matchThis = matched.group()
    else:
        matchThis = "NONE"
    return matchThis

def trouveLine1(line):
    matchThis = ""
    matched = re.match(r'\[\d\d/\d\d \d\d:\d\d:\d\d.\d+\]\(\d+,\d+\) .+', line)
    if matched:
        matchThis = matched.group()
    else:
        matchThis = "NONE"
    return matchThis

########################Fonction  pour generer des dictionnaire avec comme clé le noms de nos colonnes###############################################

def generateDicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if line.startswith(trouveLine(line)):
            if currentDict:
                yield currentDict
            currentDict = {"TimeStamp":" ".join(['2016/'+line.split(']')[0].split('.')[0].split('[')[1].split(' ')[0],line.split(']')[0].split('.')[0].split('[')[1].split(' ')[1]]),"Data1Int":line.split(']')[0].split('.')[1],"Data2Int":line.split(',')[0].split('(')[1],
                           "Data3Int":line.split(')')[0].split(',')[1], "Message":line.split('::',1)[1],"DataStr":line.split('::')[0].split(') ')[1]}
        elif line.startswith(trouveLine1(line)):
            if currentDict:
                yield currentDict
            currentDict = {"TimeStamp":" ".join(['2016/'+line.split(']')[0].split('.')[0].split('[')[1].split(' ')[0],line.split(']')[0].split('.')[0].split('[')[1].split(' ')[1]]),"Data1Int":line.split(']')[0].split('.')[1],"Data2Int":line.split(',')[0].split('(')[1],
                           "Data3Int":line.split(')')[0].split(',')[1], "Message":line.split(')')[1]}
    yield currentDict


################################################################### Main ###################################################################################
Log = '/Volumes/TOSHIBA EXT/Fada/PSTCFGMatrikon.OPC.Tunneller.1.t'
f=ouvrir(Log)
#with open( "/Volumes/TOSHIBA EXT/Fada/PSTCFGMatrikon.OPC.Tunneller.1.txt", encoding = "ISO-8859-1") as f:
    #listNew = list(generateDicts(f))
pd.set_option('expand_frame_repr', False)
df = pd.DataFrame(list(generateDicts(f)), columns=["TimeStamp","Data1Int","Data2Int","Data3Int","DataStr","Message"])
df['TimeStamp']=pd.to_datetime(df['TimeStamp'])
df['Data1Int'] = df['Data1Int'].astype(int)
df['Data3Int'] = pd.to_numeric(df['Data3Int'], errors='coerce')
df['Data2Int'] = pd.to_numeric(df['Data2Int'], errors='coerce')
df.to_csv("/Users/Mamadou/Desktop/PSTCFGMatrikon.OPC.Tunneller.1.LOG.csv")
print(df.dtypes)
