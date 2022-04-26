# -*- coding: utf-8 -*-


#input parameters
from predictiveAnalysis.predictiveAnalysis import textAndCharacteristics
from predictiveAnalysis.predictiveAnalysis import removeRedundantCharacterists
from predictiveAnalysis.predictiveAnalysis import newPdfGetTextLabelsAndTextIndex
from predictiveAnalysis.predictiveAnalysis import classGrouping
from predictiveAnalysis.predictiveAnalysis import clusterFormation
from predictiveAnalysis.predictiveAnalysis import removeOtherClassCharacteristics
from predictiveAnalysis.predictiveAnalysis import uniqueTitleCharacteristics
from docxAndPdfGenerator.docxAndPdfGenerator import previewPdf
from docxAndPdfGenerator.docxAndPdfGenerator import createDocxWithDeliminator
from docxAndPdfGenerator.docxAndPdfGenerator import individualAbstractDocxCreation
from docxAndPdfGenerator.docxAndPdfGenerator import convertDocxToPdfEachAbstract




#input parameters
modelLocation = 'C:/Users/darshanRaghunath/tfModel.h5'
TokenizerLocation = 'C:/Users/darshanRaghunath/tokenizer.json'
filename = "C:/Users/darshanRaghunath/Downloads/Doc14.pdf"
filenameDocx = "Doc14"
fileLocation = 'C:/Users/darshanRaghunath/'



#paragraph along with their characterisitics is extracted 
text , characteristics, docObject = textAndCharacteristics(filename, filenameDocx)

#remove the redundant Characteristics if present
characteristics = removeRedundantCharacterists(characteristics)

#get the Labels for each paragraph
textLabels , textIndex= newPdfGetTextLabelsAndTextIndex(text,characteristics,modelLocation,TokenizerLocation)

#group all of them to differenct class
title, author, affliation , abstract , noise , ids = classGrouping(textIndex, textLabels, text, characteristics)

#form clusters for each classes
titleCluster = clusterFormation(title , "Title")
authorCluster = clusterFormation(author , "Author")
affliationCluster = clusterFormation(affliation, "Affliation")
abstractCluster = clusterFormation(abstract, "Abstract")
noiseCluster = clusterFormation(noise, "Noise")
idCluster = clusterFormation(ids, "Ids")


#remove overlapping characteristics 
otherCharacteristics = []
otherCharacteristics = removeOtherClassCharacteristics(authorCluster,otherCharacteristics)
otherCharacteristics = removeOtherClassCharacteristics(affliationCluster,otherCharacteristics)
otherCharacteristics = removeOtherClassCharacteristics(abstractCluster,otherCharacteristics)

#Extract title characteristics
fontSize, fontFamily, colour, titleCharacteristicsList = uniqueTitleCharacteristics(titleCluster,otherCharacteristics)





#print a preview of the pdf with deliminator
previewPdf(text , characteristics,titleCharacteristicsList)

#creates docx file with deliminator
createDocxWithDeliminator(text , characteristics,titleCharacteristicsList,filenameDocx,fileLocation)

#creates docx file for each abstract
countOfDocx = individualAbstractDocxCreation(text ,characteristics,titleCharacteristicsList,filenameDocx,fileLocation,docObject)

#each docx files are converted to pdf 
convertDocxToPdfEachAbstract(countOfDocx,filenameDocx,fileLocation)    


