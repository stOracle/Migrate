import csv
glob_count = 125

def pull():
    
    with open("movies.csv", "r") as csvfile:

        readCSV = csv.reader(csvfile, delimiter = ",")

        genre_1930 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1940 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1950 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1960 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1970 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1980 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_1990 = [0, 0, 0, 0, 0, 0, 0, 0]
        genre_2000 = [0, 0, 0, 0, 0, 0, 0, 0]

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
                    decades[idx][-1] += 1
                    
        ratios = []
        for decade in decades:
            total = decade[-1]
            deg_list = []
            sum = 0
            for el in decade:
                deg = map(el, 0, total, 0, 360)
                deg_list.append(int(deg))
                sum += int(deg)
            if (sum < 360):
                res = 360 - sum
                deg_list[0] += res
            ratios.append(deg_list)

    return ratios

master_data = pull()
image_idx = 0

def setup():
    
    size(600, 700)
    frameRate(30)
    courier = createFont("Courier-New", 32)
    textFont(courier)
        
def draw():
    
    global master_data
    global image_idx
    
    background(50, 200, 50)    
    
    data = master_data[image_idx]
    data1 = master_data[-1]
    begin = 0
    
    colors = ["#E53535", "#F041D3", "#8BEDFF", "#6AFFB8", "#FDFF8B", "#EAAE2B", "#FFFFFF"]
    genre_list = ["Action", "Animation", "Comedy", 
                          "Drama", "Documentary", "Romance", "Short"]
    
    title1 = "Genre by Decade:"
    title2 = "{}s".format(1930 + 10 * image_idx)
    
    strokeWeight(4)
    stroke(0)
    fill(0)
    line(115, 88, 475, 88)
    
    textSize(45)
    textAlign(CENTER)
    text(title1, width/2, 75)
    
    textSize(75)
    textAlign(CENTER)
    text(title2, width/2, 170)
    
    strokeWeight(2)
    stroke(255)
    fill(0)  
    
    for i in range (7):
        # first fill out the table below the chart
        #fill(colors[i])
        textSize(20)
        textAlign(LEFT)
        entry = ("   =   {}".format(genre_list[i]))
        if (i > 3):
            fill(0)
            text(entry, 350, 565 + 30 * (i - 4))
            fill(colors[i])
            rect(325, 550 + 30 * (i - 4), 20, 20, 7)
        else:
            fill(0)
            text(entry, 100, 550 + 30 * i)
            fill(colors[i])
            rect(75, 535 + 30 * i, 20, 20, 7)
            
        # now draw the graph
        move = radians(int(data[i]) + 1)
        arc(300, 350, 300, 300, begin, begin + move, PIE)
        begin += move        
    
def keyPressed():
    
    global image_idx
    if (key == CODED):
        if ((keyCode == RIGHT) and (image_idx < 7)):
            image_idx += 1
        elif ((keyCode == LEFT) and (image_idx > 0)):
            image_idx -= 1