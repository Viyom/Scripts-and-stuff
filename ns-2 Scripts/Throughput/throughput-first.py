#print("Enter file name (like delay-pie-first-ftp.plotme)")
#name=raw_input()
fil = open("first-ftp-throughput.plotme", "r+")
s=fil.readlines()
l=[]
fil.close()
for c in s:
  l.append(c.replace('\n','').split(' '))
j=0
for c in l:
  l[j][1]=str(float(c[1])*8/(1024.0*1024.0))
  j=j+1
#print("Enter output file name (like delay-pie-first-ftp.plotme)")
#name=raw_input()
fil = open("throughput-first.plotme","w+")
for c in l:
  fil.write(c[0]+' '+c[1]+'\n')
fil.close()
