def pull():
    
    in_file = open("./wordfrequency.txt", "r")
    freq_dict = {}
    freq_list = []
    
    for line in in_file:
        line = line.strip()
        line = line.split(":")
        freq_dict[int(line[0])] = int(line[1])
        freq_list.append(int(line[0]))    
    
    return [freq_dict, freq_list]

def setup():
    
    size(900, 900)
    background(160, 255, 246)
    
def draw():
    
    info = pull()
    freq_dict = info[0]
    freq_list = info[1]
    num_freq = len(freq_list)    
    stroke(2)
    
    for i in range(num_freq):
        
        word_count = int((freq_dict[freq_list[i]] ** .5))
        word_metric = map(word_count, 0, 52, 0, width)
        width_sector = radians(50)
        
        if (i % 3 == 0):
            fill(227, 209, 140)
                                    
        elif (i % 3 == 1):
            fill(255, 247, 214)    
            
        else:
            fill(167, 127, 39)
                        
        arc(width/2, height/2, word_metric, word_metric, i * width_sector, (i + 1) * width_sector, PIE)
            