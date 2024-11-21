from scapy.all import *

sniff( count=0, lfilter="", store=0, prn = lambda pkt: print(pkt.summary()) 


lfilter=lambda pkt: return ( pkt.haslayer(DHCP) && (pkt[ IP] .dst == '255.255.255.255') && ((pkg[   .port == 68) || ( pkt.[   ].port == 67)) )



 