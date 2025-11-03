def parse_fms_file(fms_file_path):
    #We want to parse the text file and extract the fms values
    with open(fms_file_path, 'r') as f:
        lines = f.readlines()
    

    #save the fms values in a list
    fms_values = []
    temp = []
    for line in lines:
        #We do not need the spaces, only the values
        if line.strip():
            temp.append(line)
    #The first 7 line is irrelevant
    temp = temp[7:]
    
    #Now let's keep only the first values as the fms values

    for readings in temp:
        fms_values.append(int(readings[0]))
    
    #return the integer fms values 
    return fms_values