from scapy.all import * from time import ctime,sleep from threading import Thread,Lock  # import IPy



flag = 0
dhcp_address = '0.0.0.0' current_subnet = '0.0.0.0'



def getdhcpip():
    global flag
    print "[+] Geting The DHCP server IP Address!" 

    while flag == 0: 
        tap_interface = 'eth0'                           src_mac_address = RandMAC() 
        ethernet = Ether(dst = 'ff:ff:ff:ff:ff:ff',src = src_mac_address,type=0x800)
        ip = IP(src ='0.0.0.0',dst='255.255.255.255')              udp =UDP (sport=68,dport=67)         fam,hw = get_if_raw_hwaddr(tap_interface) bootp = BOOTP(chaddr = hw, ciaddr = '0.0.0.0',xid = 0x01020304,flags= 1) 

        dhcp = DHCP(options = [("message-type","discover"),"end"]) 

        packet = ethernet / ip / udp / bootp / dhcp             
   
        sendp( packet, count=1, verbose=0)
        sleep(0.1)
