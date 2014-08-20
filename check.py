def checkLanguage(language):
	import csv

	sampleStats={};
	inputStats={};

	with open('input2.csv', 'rb') as inputFile:
		reader = csv.reader(inputFile)
		for inputValue in reader:
			inputStats[inputValue[0]]=inputValue[1];

	with open("languages/"+language + '.csv', 'rb') as sampleFile:
		reader = csv.reader(sampleFile)
		for sampleValue in reader:
			sampleStats[sampleValue[0]]=sampleValue[1];
				

	languageScore=0;
	numberOfMathces= 0;
	for key in inputStats:
		if(key in sampleStats.keys()):
			languageScore+=(float(inputStats[key])/float(sampleStats[key]));
			numberOfMathces+=1;
	#		print "Match: {0}".format(key);
	#print "Matches: {0}".format(numberOfMathces);	
	if (numberOfMathces==0):
		return 0;
	lanaugeProbability=languageScore/numberOfMathces
	
	return lanaugeProbability;

print "English: {0}".format(checkLanguage("english")); 
print "French: {0}".format(checkLanguage("french"));

