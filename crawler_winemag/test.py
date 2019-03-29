import math

def getResult(testData, vocabDict, positivePrior, negativePrior, positiveCount, negativeCount, featureSize):
	testOutput = {}
	print "Test data"
	print testData
	i=0			
	for row in testData:
		actualPos = 0
		actualNeg = 0
		#through the dictionary		
		for key in vocabDict:			
			label = None
			if key in row[0]:
				positiveProb= vocabDict[key]["positiveProb"]
				actualPos += math.log10(positiveProb)
				negativeProb = vocabDict[key]["negativeProb"]
				actualNeg += math.log10(negativeProb)
			else:
				nPositiveProb = vocabDict[key]["nPositiveProb"]
				actualPos += math.log10(nPositiveProb)
				nNegativeProb = vocabDict[key]["nNegativeProb"]		
				actualNeg += math.log10(nNegativeProb)	
		# handling new words
		for word in row[0]:
			if word not in vocabDict:
				positiveProb = float(1)/(positiveCount+featureSize)
				actualPos+=math.log10(positiveProb)	
				negativeProb = float(1)/(negativeCount+featureSize)		
				actualNeg+=math.log10(negativeProb)
		actualPos+=math.log10(positivePrior)
		actualNeg+=math.log10(negativePrior)					
		if(actualPos>actualNeg):
			label = "Positive"
		else:
			label = "Negative"
		testOutput[i] = {
		"positive": actualPos,
		"negative": actualNeg,
		"label":label
		}		
		i+=1	
	return testOutput

def formConfusionMatrix(testData, predictedValues):
	confusionDict = initializeConfusionDict()
	for key in predictedValues:
		tempList = testData[int(key)]
		if tempList[2]==predictedValues[key]["label"]: 
			if tempList[2]=="Positive":
				confusionDict["true"]["positive"]+=1	
			else:
				confusionDict["true"]["negative"]+=1
		else:
			if predictedValues[key]["label"]=="Positive":
				confusionDict["false"]["positive"]+=1
			else:
				confusionDict["false"]["negative"]+=1
	print "Accuracy"
	print float(confusionDict["true"]["positive"]+confusionDict["true"]["negative"])/(confusionDict["true"]["positive"]+confusionDict["true"]["negative"]+confusionDict["false"]["positive"]+confusionDict["false"]["negative"])
	print "confusion matrix"
	print
	print confusionDict
	return confusionDict

def initializeConfusionDict():
	confusionDict = {"true": {"positive":0, "negative":0}, "false": {"positive":0, "negative":0}}
	return confusionDict







