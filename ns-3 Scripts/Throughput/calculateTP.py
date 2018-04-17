# This program is used to plot throughput calculation from pcap file 

import sys
import os

for file_name in sys.argv[1:]:
    os.system("tshark -r " + file_name +" -T fields -e frame.time_relative -e frame.len -e ip.dst  >" + file_name[0:file_name.rindex('.')] + ".csv")
    f = open('TP-' + file_name[0:file_name.rindex('.')] + '.plotme', 'w')
    fPackets = open('TP-Packets-' + file_name[0:file_name.rindex('.')] + '.plotme', 'w')
    old_time = 0
    new_time =0
    val = 0
    valPackets = 0
    totalval = 0
    totalvalPackets = 0
    p = 0.0
    print "\nThroughput for " + file_name[0:file_name.rindex('.')]
    with open(file_name[0:file_name.rindex('.')] + '.csv') as fq:
        fp = fq.readlines()
        for line in fp:
            if float(line.split('\t')[1]) >= 100:
                new_time = float(line.split('\t')[0])
                val += float(line.split('\t')[1])
                valPackets += 1
                totalval += float(line.split('\t')[1])
                totalvalPackets += 1
                if (new_time - old_time > 0.1):
                    val = val/(new_time - old_time)
                    valPackets = valPackets/(new_time - old_time)
                    f.write(str(p) + " " + str(val * 8.0 / (1000.0 * 1000.0)) + "\n")
                    fPackets.write(str(p) + " " + str(valPackets) + "\n")
                    p += (new_time - old_time)
                    old_time = new_time
                    val = 0
                    valPackets = 0
        print "Overall throughput (Mbps):" + str(totalval * 8.0 / (1000.0 * 1000.0) / new_time)
        print "Overall throughput (Packets/sec):" + str(totalvalPackets * 1.0 / new_time)

    f.close()
    fPackets.close()
    os.remove(file_name[0:file_name.rindex('.')] + '.csv')
