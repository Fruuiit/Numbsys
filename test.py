import csv

with open('testexample2.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		L = []
		for row in readCSV:
			#print(row)
			
			L.append(row[0]);


		print(L)
		#M = list(set(L))
		
		Dforward = {}
		Dbackward = {}
		for i in range(len(M)):
			Dforward[M[i]] = i
			Dbackward[i] = M[i];
		print(Dforward)
		print(Dbackward);

