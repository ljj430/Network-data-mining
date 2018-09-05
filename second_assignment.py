import os
def transform(word):
    word=list(word)
    word2=''
    word=list(filter(lambda ch:ch.isalpha(),word))
    for i in word:
        word2+=i
    return word2

def eachfile(filepath):
    pathDir=os.listdir(filepath)
    child=[]
    for allDir in pathDir:
        child.append(os.path.join('%s\\%s'%(filepath,allDir)))
    return child
child=eachfile(filepath='E:\python学习\Inverted_File\.idea\documents')
for i in range(len(child)):
    print(i,'\t',child[i])
Dic={}
for i in range(len(child)):
    file=open(str(child[i]),'r')
    Str=file.read()
    data=Str.split(' ')
    for j in range(len(data)):
        if(data[j].isalpha()==False):
            data[j]=transform(data[j])
    for j in data:
        if j not in Dic:
            Dic[j]=[i]
        elif i not in Dic[j]:
            Dic[j].append(i)
f=open("Inverted_File.txt",'w')
for k,v in Dic.items():
    l=str(k)+'\t'+str(v)+'\n'
    f.write(l)
f.close()


