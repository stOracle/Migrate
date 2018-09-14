import csv

def main():

	with open("movies.csv") as csvfile:

		readCSV = csv.reader(csvfile, delimiter = ",")

		genre_1930 = [0, 0, 0, 0, 0, 0, 0]
		genre_1940 = [0, 0, 0, 0, 0, 0, 0]
		genre_1950 = [0, 0, 0, 0, 0, 0, 0]
		genre_1960 = [0, 0, 0, 0, 0, 0, 0]
		genre_1970 = [0, 0, 0, 0, 0, 0, 0]
		genre_1980 = [0, 0, 0, 0, 0, 0, 0]
		genre_1990 = [0, 0, 0, 0, 0, 0, 0]
		genre_2000 = [0, 0, 0, 0, 0, 0, 0]

		decades = [genre_1930, genre_1940, genre_1950, genre_1960,
			genre_1970, genre_1980, genre_1990, genre_2000]	

		for row in readCSV:

			if (row[1] == "title"):
				continue
 
			year = int(row[2])
			if (year < 1930):
				continue

			decade = (year // 10) % 10
			idx = decade - 3
			if idx < 0:
				idx = -1

			genre_list = ["Action", "Animation", "Comedy", 
			"Drama", "Documentary", "Romance", "Short"]

			for i in range (7):
				if row[i + 5] == "1":
					decades[idx][i] += 1

			#data = [year, genre]

		return decades

main()



