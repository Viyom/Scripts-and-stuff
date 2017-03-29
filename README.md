# Scripts-and-stuff

To run CheckStyle:  ./utils/check-style.py --level=3 --in-place -f src/path/filename.cc

## ns-2 
### QueueLength: python queueLength.py file1.tr file2.tr file3.tr 
(tmp-pi-first.tr)

### Throughput: perl throughput.pl filename.tr 6 0.1 > output.plotme
- 6: end node
- 0.1: granularity

## ns-3
### Throughput: python calculateTP.py file1.pcap file2.pcap file3.pcap 
- Prerequisites: install tshark using `sudo apt-get install tshark`
