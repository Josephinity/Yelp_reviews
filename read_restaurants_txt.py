import pandas as pd
def read_restaurants_txt(filename='restaurants_0_50.txt',seperator='\\'):
    with open(filename) as f:
        lines=[[line] for line in f.readlines()]
        header=lines[0][0].split(seperator)[1:]
        header[-1]=header[-1][:-1]
        content=[line[0].split(seperator)[1:] for line in lines[1:]]
    return pd.DataFrame(content,columns=header)