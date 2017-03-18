f = open( 'throughput.plotme', 'w')
old_time = 0
new_time =0
val = 0
p = 0.0
count = 0
with open('output.txt') as fq:
    fp = fq.readlines()
    for line in fp:
        new_time = float(line.split(' ')[0])
        val += float(line.split(' ')[1])
        count += 1
        if (new_time - old_time > 0.08):
            val = val/(new_time - old_time)
            f.write(str(p) + " " + str(val*8.0/(1024 * 1024)) + '\n')
            p += new_time - old_time
            old_time = new_time
            val = 0
            count = 0
