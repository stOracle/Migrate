import csv

def main():

	with open("movies.csv") as csvfile:

		readCSV = csv.reader(csvfile, delimiter = ",")

		years = []
		ratings = []
		mpaa_values = ["R", "PG-13", "PG", "G", "NC-17"]
		mpaa = []
		mpaa_dict = {}
		is_act = []
		is_ani = []
		is_com = []
		is_dra = []
		is_doc = []
		is_rom = []
		is_short = []	
		genres = [is_act, is_ani, is_com, is_dra, is_doc, is_rom, is_short]
		genre_list = ["Action", "Animation", "Comedy", 
			"Drama", "Documentary", "Romance", "Short"]
		genre_dict = {}
		min_year = 1893
		max_year = 2005

		for row in readCSV:
			if (row[1] == "title"):
				continue

			years.append(row[2])
			if (int(row[2]) > max_year):
				max_year = int(row[2])
			ratings.append(row[3])
			mpaa.append(row[4])
			for i in range (7):
				genres[i].append(int(row[i + 5]))

		print(max_year)



		for el in mpaa:
			if (el == ""):
				continue
			elif not el in mpaa_dict:
				mpaa_dict[el] = 1
			else:
				mpaa_dict[el] += 1

		

		# for i in range (genres):
		# 	for el in genres[i]:
		# 		if (el == "1"):
		# 			if genre_dict[genre_list]
				

		print (mpaa_dict)
		#print (genre_dict)
			
		print (ratings[3])
		print (mpaa[:5])
		print (len(ratings))
		print (len(genres))
	print (max_year)

main()