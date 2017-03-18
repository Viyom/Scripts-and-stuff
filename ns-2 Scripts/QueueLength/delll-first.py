f=open("tmp-pi-first-ftp.tr","r+")
s=f.readlines()
j=0
for c in s:
  s[j]=c.replace('\n','').split(' ')
  j+=1
fil=open("tmp-pi-first-ftp.plotme","w+")
for c in s:
  if c[0]=='Q':
    fil.write(c[1]+' '+c[2]+'\n')
fil.close()
f.close()

