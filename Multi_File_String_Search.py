#Multi File String Search

filepaths=[]
search_string=input("What do you want to search for: ")
results_name=input("Name your file and add a file extension: ")
results=open(results_name,"w")
results.write("Searching for "+search_string+"\n")
results.close()
cnt=0


with open ('Include_of_Includes_Sample.dat','r') as file:
    for line in file:
        if line.startswith('INCLUDE'):
            beg_index=line.find("'")
            a=line[beg_index+1:]
            a1=a.strip()
            b=file.readline()
            c=b[0:-2]
            c1=c.strip()
            filepath=a1+c1
            filepaths.append(filepath)
        else:
            pass
print(filepaths)

for filepath in filepaths:
    try:
        open_filepath=open(filepath)
        #print(open_filepath)
        for line in open_filepath:
            if search_string in line:
                results=open(results_name,'a')
                if cnt==0:
                    result=print('That string exists in this file: '+filepath)
                    results.write('That string exists in this file: '+filepath+'\n')
                    results.write(line+'\n')
                    results.close()
                    cnt=1
                else:
                    results.write(line+'\n')
                    results.close()
    except:
        continue
    cnt=0
print('Done!')
