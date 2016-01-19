import pandas as pd
#read reviews
def read_reviews_txt(filename):
    with open(filename) as f:
        lines=[[line] for line in f.readlines()]
        header=lines[0][0].split('\t')[1:]
        header[-1]=header[-1][:-1]
        content=[line[0].split('\t')[1:] for line in lines[1:]]
        for row in content:
            row[4]=row[4][:-1]
            row[3]=row[3].decode('utf-8')
            row[3]=row[3].replace('"','')
            row[3]=stripHerf(row[3])
    return pd.DataFrame(content,columns=header)
    
#remove links for pictures in reviews
def stripHerf(review):
    e=0
    alist=[]
    while(review[e:].find('<a')>0):
        s=review[e:].find('<a')+e
        e=review[s:].find('a>')+s
        if(e>s):
            alist.append([s,e+2])
    if(len(alist)>0):
        newstr=''
        for pair in alist:
            newstr+=review[0:pair[0]]+review[pair[1]:]
        return newstr
    else:
        return review