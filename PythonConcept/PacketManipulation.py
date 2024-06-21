from scapy.layers.inet import IP , TCP
from scapy.sendrecv import sr1


ip = IP(dst = 'www.google.com')
syn = TCP(dport = 443 , flags = 'S')
pkt = syn/ip
response = sr1(pkt , timeout = 1)

if response:
    response.show()

else:
    print("no response")