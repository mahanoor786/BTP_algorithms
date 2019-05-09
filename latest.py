import math

# Open the file with read only permit
inFile = open('20kMyOutFile.txt')
outFile = open("Latest.txt", "w")
# use readline() to read the first line 
line = inFile.readline()
# use the read line to read further.




while line:
	stringtime = []
	ind = line.split(':')
	edge_array = ind[2].split(',')
	i=0;
	j=0;
	
	while i<len(edge_array):
		if i==int(edge_array[j]):
			
			
			
			while(j+1<len(edge_array) and (edge_array[j]==edge_array[j+1])):
				
				j=j+1
			stringtime.append(j)
			j=j+1
			
			i=i+1
		elif i<int(edge_array[0]):
			stringtime.append(0)
			i=i+1
		else :

			first=int(edge_array[j-1])
			second=int(edge_array[j])
			if abs(first-i)>abs(second-i):
				stringtime.append(j)
			else :
				stringtime.append(j-1)
			i=i+1
			
	stringtime = [str(i) for i in stringtime]
	st  = ",".join(stringtime)
	
	outFile.write(ind[1] + ':' + ind[0] + ':'+st+'\n')
	
	line = inFile.readline()
inFile.close()
outFile.close()
