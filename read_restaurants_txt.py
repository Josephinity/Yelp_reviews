import pandas as pd
def read_restaurants_txt(filename='restaurants_0_50.txt',seperator='#'):
    with open(filename) as f:
        lines=[line for line in f.readlines() if line]
        header=lines[0].split(seperator)[1:]
        header[-1]=header[-1][:-1]
        content=[]
        current=''
        for line in lines[1:]:
            if len(line)>3 and line[-3]=='#': 
                current+=line
                content.append(current)
                current=''
            elif line is not '':
                current+=line
        content=[line[:-1].replace('"','').split(seperator)[1:] for line in content]
    return pd.DataFrame(content,columns=header)