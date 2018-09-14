def pull():
    
    in_file = open("./wordfrequency.txt", "r")
    freq_dict = {}
    freq_list = []
    breaks = []
    
    for line in in_file:
        line = line.strip()
        line = line.split(":")
        freq_dict[int(line[0])] = int(line[1])
        freq_list.append(int(line[0]))
    
    for i in range (len(freq_list) - 1):
        if (freq_list[i + 1] != freq_list[i] + 1):
            breaks.append(freq_list[i])    
    
    return [freq_dict, freq_list, breaks]

def setup():
    
    size(900, 900)
    #background(0)
    background(160, 255, 246)
    #angle = 355
    
def draw():
    
    info = pull()
    freq_dict = info[0]
    freq_list = info[1]
    breaks = info[2]
    num_freq = len(freq_list)    
    stroke(2)
    
    for i in range(num_freq):
        
        # metric maps i's range from [0, num_freq] to [0, 255]
        # will help with color coating
        metric = map(i, 0, num_freq, 0, 255)
        
        word_count = int((freq_dict[freq_list[i]] ** .5))
        word_metric = map(word_count, 0, 52, 0, width)
        max_words = freq_dict[freq_list[0]]
        width_sector = radians(50)
        
        if (i % 3 == 0):
            fill(227, 209, 140)
                                    
        elif (i % 3 == 1):
            fill(255, 247, 214)    
            
        else:
            fill(167, 127, 39)
                        
        arc(width/2, height/2, word_metric, word_metric, i * width_sector,(i + 1) * width_sector, PIE)
            