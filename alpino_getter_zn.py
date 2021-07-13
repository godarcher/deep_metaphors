##############
#dependencies#
##############
import csv
from lxml import etree
from io import StringIO, BytesIO
import os
import xml.etree.ElementTree as ET

###############
#DOCUMENTATION#
###############

################
#USER INTERFACE#
################

#globals
sensed1 = ""
sensed2 = ""
sensed3 = ""
sensed4 = ""
sensed5 = ""
sensed6 = ""
sensed7 = ""

rootd1 = ""
rootd2 = ""
rootd3 = ""
rootd4 = ""
rootd5 = ""
rootd6 = ""
rootd7 = ""

genusd1 = ""
genusd2 = ""
genusd3 = ""
genusd4 = ""
genusd5 = ""
genusd6 = ""
genusd7 = ""

getald1 = ""
getald2 = ""
getald3 = ""
getald4 = ""
getald5 = ""
getald6 = "" 
getald7 = ""

###########
#FUNCTIONS#
###########
import warnings
warnings.filterwarnings("ignore")

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
                                                       
##################
#GLOBAL VARIABLES#
##################

filenumber = 0
parser = etree.XMLParser(ns_clean=True,remove_comments=True)
directory = r'C:\Users\Josso\Documents\Radboud\corpus_alpino_parsed'

subdirectories = os.listdir(directory)
for directory_d2_first in subdirectories:
    print(directory_d2_first)
    directory_d2 = directory + "\\" + directory_d2_first
    for filename in os.listdir(directory_d2):
        if filename.endswith(".xml"):
            #print(filename)
            #definitions are placed here so they are reset for each file
            sensed1 = ""
            sensed2 = ""
            sensed3 = ""
            sensed4 = ""
            sensed5 = ""
            sensed6 = ""
            sensed7 = ""

            rootd1 = ""
            rootd2 = ""
            rootd3 = ""
            rootd4 = ""
            rootd5 = ""
            rootd6 = ""
            rootd7 = ""

            genusd1 = ""
            genusd2 = ""
            genusd3 = ""
            genusd4 = ""
            genusd5 = ""
            genusd6 = ""
            genusd7 = ""

            getald1 = ""
            getald2 = ""
            getald3 = ""
            getald4 = ""
            getald5 = ""
            getald6 = "" 
            getald7 = ""
            
            filenumber = filenumber + 1
            filedirectory = directory_d2 + "\\" + filename        
            tree = etree.parse(filedirectory,parser)
            root = tree.getroot()                                                             
        
            ############################################
            #PART 1: get obj subj verb and sent number #
            ############################################
            for alpino_ds in root.iter('alpino_ds'):
                for top in alpino_ds:
                    for smain in top:
                        nounfound = False

                        ############
                        #MAIN LEVEL#
                        ############
                        
                        for child in smain:
                            kind_child = child.get('frame')
                            if not str(kind_child) == "None": #empty
                                if kind_child.find('noun') != -1:
                                    nounfound = True

                        for child in smain:
                            if nounfound == True:
                                #Gather xml objects
                                sense_child = child.get('sense')
                                root_child = child.get('root')
                                genus_child = child.get('genus')
                                getal_child = child.get('getal')
                                
                                #check if not empty
                                if not str(sense_child) == "None":
                                    sensed1 = sense_child

                                #check if not empty
                                if not str(sense_child) == "None":
                                    rootd1 = root_child

                                #check if not empty
                                if not str(sense_child) == "None":
                                    genusd1 = genus_child

                                #check if not empty
                                if not str(sense_child) == "None":
                                    getald1 = getal_child
                     
                        #########
                        #LEVEL 2#
                        #########
                                                    
                            nounfound2 = False
                            for childx in child:
                                kind_child = childx.get('frame')
                                if not str(kind_child) == "None": #empty
                                    if kind_child.find('noun') != -1:
                                        nounfound2 = True

                            for childx in child:
                                if nounfound2 == True:
                                    #Gather xml objects
                                    sense_child = childx.get('sense')
                                    root_child = childx.get('root')
                                    genus_child = childx.get('genus')
                                    getal_child = childx.get('getal')
                                    
                                    #check if not empty
                                    if not str(sense_child) == "None":
                                        sensed2 = sense_child

                                    #check if not empty
                                    if not str(sense_child) == "None":
                                        rootd2 = root_child

                                    #check if not empty
                                    if not str(sense_child) == "None":
                                        genusd2 = genus_child

                                    #check if not empty
                                    if not str(sense_child) == "None":
                                        getald2 = getal_child
                                        
                        #########
                        #LEVEL 3#
                        #########

                                nounfound3 = False                                            
                                for childy in childx:
                                    kind_child = childy.get('frame')
                                    if not str(kind_child) == "None": #empty
                                        if kind_child.find('noun') != -1:
                                            nounfound3 = True

                                for childy in childx:
                                    if nounfound3 == True:
                                        #Gather xml objects
                                        sense_child = childy.get('sense')
                                        root_child = childy.get('root')
                                        genus_child = childy.get('genus')
                                        getal_child = childy.get('getal')
                                        
                                        #check if not empty
                                        if not str(sense_child) == "None":
                                            sensed3 = sense_child

                                        #check if not empty
                                        if not str(sense_child) == "None":
                                            rootd3 = root_child

                                        #check if not empty
                                        if not str(sense_child) == "None":
                                            genusd3 = genus_child

                                        #check if not empty
                                        if not str(sense_child) == "None":
                                            getald3 = getal_child                     

                        #########
                        #LEVEL 4#
                        #########

                                    nounfound4 = False                        
                                    for childz in childy:
                                        kind_child = childz.get('frame')
                                        if not str(kind_child) == "None": #empty
                                            if kind_child.find('noun') != -1:
                                                nounfound4 = True

                                    for childz in childy:
                                        if nounfound4 == True:                                                   
                                            #Gather xml objects
                                            sense_child = childz.get('sense')
                                            root_child = childz.get('root')
                                            genus_child = childz.get('genus')
                                            getal_child = childz.get('getal')
                                            
                                            #check if not empty
                                            if not str(sense_child) == "None":
                                                sensed4 = sense_child

                                            #check if not empty
                                            if not str(sense_child) == "None":
                                                rootd4 = root_child

                                            #check if not empty
                                            if not str(sense_child) == "None":
                                                genusd4 = genus_child

                                            #check if not empty
                                            if not str(sense_child) == "None":
                                                getald4 = getal_child    

                        #########
                        #LEVEL 5#
                        #########

                                        nounfound5 = False                        
                                        for childa in childz:
                                            kind_child = childa.get('frame')
                                            if not str(kind_child) == "None": #empty
                                                if kind_child.find('noun') != -1:
                                                    nounfound5 = True

                                        for childa in childz:
                                            if nounfound5 == True:
                                                #Gather xml objects
                                                sense_child = childa.get('sense')
                                                root_child = childa.get('root')
                                                genus_child = childa.get('genus')
                                                getal_child = childa.get('getal')
                                                
                                                #check if not empty
                                                if not str(sense_child) == "None":
                                                    sensed5 = sense_child

                                                #check if not empty
                                                if not str(sense_child) == "None":
                                                    rootd5 = root_child

                                                #check if not empty
                                                if not str(sense_child) == "None":
                                                    genusd5 = genus_child

                                                #check if not empty
                                                if not str(sense_child) == "None":
                                                    getald5 = getal_child  

                        #########
                        #LEVEL 6#
                        #########

                                            nounfound6 = False                        
                                            for childb in childa:
                                                kind_child = childb.get('frame')
                                                if not str(kind_child) == "None": #empty
                                                    if kind_child.find('noun') != -1:
                                                        nounfound6 = True

                                            for childb in childa:
                                                if nounfound6 == True:
                                                    #Gather xml objects
                                                    sense_child = childb.get('sense')
                                                    root_child = childb.get('root')
                                                    genus_child = childb.get('genus')
                                                    getal_child = childb.get('getal')
                                                    
                                                    #check if not empty
                                                    if not str(sense_child) == "None":
                                                        sensed6 = sense_child

                                                    #check if not empty
                                                    if not str(sense_child) == "None":
                                                        rootd6 = root_child

                                                    #check if not empty
                                                    if not str(sense_child) == "None":
                                                        genusd6 = genus_child

                                                    #check if not empty
                                                    if not str(sense_child) == "None":
                                                        getald6 = getal_child  

                        #########
                        #LEVEL 7#
                        #########

                                                nounfound7 = False                        
                                                for childc in childb:
                                                    kind_child = childc.get('frame')
                                                    if not str(kind_child) == "None": #empty
                                                        if kind_child.find('noun') != -1:
                                                            nounfound7 = True

                                                for childc in childb:
                                                    if nounfound7 == True:                                                               
                                                        #Gather xml objects
                                                        sense_child = childc.get('sense')
                                                        root_child = childc.get('root')
                                                        genus_child = childc.get('genus')
                                                        getal_child = childc.get('getal')
                                                        
                                                        #check if not empty
                                                        if not str(sense_child) == "None":
                                                            sensed7 = sense_child

                                                        #check if not empty
                                                        if not str(sense_child) == "None":
                                                            rootd7 = root_child

                                                        #check if not empty
                                                        if not str(sense_child) == "None":
                                                            genusd7 = genus_child

                                                        #check if not empty
                                                        if not str(sense_child) == "None":
                                                            getald7 = getal_child  

            ########
            #output#
            ########

            #opening an output file for the associated input file
            outputdirectory = directory_d2.replace(".xml","")
            outputindex = outputdirectory.rfind("\\")
            outputfolder = outputdirectory[outputindex+1:]
            outputfolder = outputfolder.replace("_sen.txt.alpinoxml","")
            
            outputdirectory = outputdirectory + "\\" + outputfolder + "_zn_" + filename + ".txt"
            f = open(outputdirectory, "w")
            #verb based printing filewriting approach
            #configured for line in file based reading
            if debug == True:
                #filename
                #print("")
                #print(filename)
                i = 1


            #TODO: build way to link verb with information that comes with it!
                    
            if verbd2 != "" and verbd2 != " " and verbd2 != "\n":
                if objd2 != "" and subd2 != "" and str(subd2) != "None" and str(objd2) != "None":
                    f.write("verb: " + verbd2 + " obj: " + objd2 + " subj: " + subd2 + " objlemma: " + olemd2 + " subjlemma: " + slemd2 + "\n")
                elif (objd2 != "" and str(objd2) != "None" and subd2 == "") or (objd2 != "" and str(objd2) != "None" and str(subd2) == "None"):
                    f.write("verb: " + verbd2 + " obj: " + objd2 + " objlemma: " + olemd2 + "\n")
                elif (objd2 == "" and subd2 != "" and str(subd2) != "None") or (str(objd2) == "None" and subd2 != "" and str(subd2) != "None"):
                    f.write("verb: " + verbd2 + " subj: " + subd2 + " subjlemma: " + slemd2 + "\n")
                elif verbd2 != "" and verbd2 != " " and verbd2 != "\n":
                    f.write("verb: " + verbd1)                    
            if verbd3 != "" and verbd3 != " " and verbd3 != "\n":
                if objd3 != "" and subd3 != "" and str(subd3) != "None" and str(objd3) != "None":
                    f.write("verb: " + verbd3 + " obj: " + objd3 + " subj: " + subd3 + " objlemma: " + olemd3 + " subjlemma: " + slemd3 + "\n")
                elif (objd3 != "" and str(objd3) != "None" and subd3 == "") or (objd3 != "" and str(objd3) != "None" and str(subd3) == "None"):
                    f.write("verb: " + verbd3 + " obj: " + objd3 + " objlemma: " + olemd3 + "\n")
                elif (objd3 == "" and subd3 != "" and str(subd3) != "None") or (str(objd3) == "None" and subd3 != "" and str(subd3) != "None"):
                    f.write("verb: " + verbd3 + " subj: " + subd3 + " subjlemma: " + slemd3 + "\n")
                elif verbd3 != "" and verbd3 != " " and verbd3 != "\n":
                    f.write("verb: " + verbd1)  
            if verbd4 != "" and verbd4 != " " and verbd4 != "\n":
                if objd4 != "" and subd4 != "" and str(subd4) != "None" and str(objd4) != "None":
                    f.write("verb: " + verbd4 + " obj: " + objd4 + " subj: " + subd4 + " objlemma: " + olemd4 + " subjlemma: " + slemd4 + "\n")
                elif (objd4 != "" and str(objd4) != "None" and subd4 == "") or (objd4 != "" and str(objd4) != "None" and str(subd4) == "None"):
                    f.write("verb: " + verbd4 + " obj: " + objd4 + " objlemma: " + olemd4 + "\n")
                elif (objd4 == "" and subd4 != "" and str(subd4) != "None") or (str(objd4) == "None" and subd4 != "" and str(subd4) != "None"):
                    f.write("verb: " + verbd4 + " subj: " + subd4 + " subjlemma: " + slemd4 + "\n")
                elif verbd4 != "" and verbd4 != " " and verbd4 != "\n":
                    f.write("verb: " + verbd4)
            if verbd5 != "" and verbd5 != " " and verbd5 != "\n":
                if objd5 != "" and subd5 != "" and str(subd5) != "None" and str(objd5) != "None":
                    f.write("verb: " + verbd5 + " obj: " + objd5 + " subj: " + subd5 + " objlemma: " + olemd5 + " subjlemma: " + slemd5 + "\n")
                elif (objd5 != "" and str(objd5) != "None" and subd5 == "") or (objd5 != "" and str(objd5) != "None" and str(subd5) == "None"):
                    f.write("verb: " + verbd5 + " obj: " + objd5 + " objlemma: " + olemd5 + "\n")
                elif (objd5 == "" and subd5 != "" and str(subd5) != "None") or (str(objd5) == "None" and subd5 != "" and str(subd5) != "None"):
                    f.write("verb: " + verbd5 + " subj: " + subd5 + " subjlemma: " + slemd5 + "\n")
                elif verbd5 != "" and verbd5 != " " and verbd5 != "\n":
                    f.write("verb: " + verbd5)
            if verbd6 != "" and verbd6 != " " and verbd6 != "\n":
                if objd6 != "" and subd6 != "" and str(subd6) != "None" and str(objd6) != "None":
                    f.write("verb: " + verbd6 + " obj: " + objd6 + " subj: " + subd6 + " objlemma: " + olemd6 + " subjlemma: " + slemd6 + "\n")
                elif (objd6 != "" and str(objd6) != "None" and subd6 == "") or (objd6 != "" and str(objd6) != "None" and str(subd6) == "None"):
                    f.write("verb: " + verbd6 + " obj: " + objd6 + " objlemma: " + olemd6 + "\n")
                elif (objd6 == "" and subd6 != "" and str(subd6) != "None") or (str(objd6) == "None" and subd6 != "" and str(subd6) != "None"):
                    f.write("verb: " + verbd6 + " subj: " + subd6 + " subjlemma: " + slemd6 + "\n")
                elif verbd6 != "" and verbd6 != " " and verbd6 != "\n":
                    f.write("verb: " + verbd6)
            if verbd7 != "" and verbd7 != " " and verbd7 != "\n":
                if objd7 != "" and subd7 != "" and str(subd7) != "None" and str(objd7) != "None":
                    f.write("verb: " + verbd7 + " obj: " + objd7 + " subj: " + subd7 + " objlemma: " + olemd7 + " subjlemma: " + slemd7 + "\n")
                elif (objd7 != "" and str(objd7) != "None" and subd7 == "") or (objd7 != "" and str(objd7) != "None" and str(subd7) == "None"):
                    f.write("verb: " + verbd7 + " obj: " + objd7 + " objlemma: " + olemd7 + "\n")
                elif (objd7 == "" and subd7 != "" and str(subd7) != "None") or (str(objd7) == "None" and subd7 != "" and str(subd7) != "None"):
                    f.write("verb: " + verbd7 + " subj: " + subd7 + " subjlemma: " + slemd7 + "\n")
                elif verbd7 != "" and verbd7 != " " and verbd7 != "\n":
                    f.write("verb: " + verbd7)

            f.close()         

