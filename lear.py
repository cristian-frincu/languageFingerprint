def split_by_len(text,chunksize):
    return [text[i:(i+chunksize)] for i in range(len(text)-chunksize+1)] 

def textToStats(inputFileName,outputName):
	import operator
	f = open(inputFileName, 'r');

	words={};
	max_count=0; 
	for word in split_by_len(f.read(),4):
		if word in words:
			count = words[word];
		else:
			count=0;
		words[word] = count+1;
		if(count>=max_count):
			max_count=count;
	max_count+=1;

	sorted_words = reversed(sorted(words.iteritems(), key=operator.itemgetter(1))); 

	import csv 
	w = csv.writer(open("languages/"+outputName, "w"))

	count=0;
	for key, val in sorted_words:
		w.writerow([key,float( val)/max_count])
		count+=1;
		if(count>25):
			break;

print "Input the name of the file:";
inputName= raw_input();
textToStats(inputName,inputName+".csv");
print "Complete!";   
