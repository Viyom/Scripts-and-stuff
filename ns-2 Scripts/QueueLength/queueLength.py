import sys

for file_name in sys.argv[1:]:
    f=open(file_name,"r+")
    s=f.readlines()
    j=0
    for c in s:
        s[j]=c.replace('\n','').split(' ')
        j+=1
    fil=open(file_name[:file_name.rindex(".")] + ".plotme","w+")
    for c in s:
        if c[0]=='Q':
            fil.write(c[1]+' '+c[2]+'\n')
    fil.close()
    f.close()

