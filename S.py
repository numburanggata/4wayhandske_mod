import socket
import hashlib
import binascii
server = '127.0.0.1'
port = 9001
#s_bssid = "11:29:EA:A2:11:34"
#s_bssid = "AA:AA:AA:AA:AA:AA"


print "Station A Started (S)"
s_bssid = raw_input("Station BSSID\t: ")
SQ = raw_input("Press enter current SQ\t: ")
SQ = int(SQ)
raw_input("Press enter to scan available AP\n")

colokan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
colokan.connect((server, port))

print "AP Found!"
ap_essid = colokan.recv(32)
print "ESSID\t: " + ap_essid
ap_bssid = colokan.recv(32)
print "BSSID\t: " + ap_bssid
raw_input("Press enter to send Authentication Requests\n")

psk = raw_input("PSK\t: ")
pmk = hashlib.pbkdf2_hmac('sha256', psk, 'kmzway87aa', 100000)
print "PMK\t: " + binascii.hexlify(pmk)

hsq = hashlib.sha224(str(SQ + 1)).hexdigest()
print "\nAuthentication Request: Station BSSID = " + s_bssid + " || h(SQ) = " + str(hsq)
colokan.sendall(s_bssid)
colokan.sendall(str(hsq))
#print hsq
print "Waiting for AP reply..."

def end():
    raw_input("Modified 4-Way Handshake Protocol Simulation Completed.")
    raw_input("Press enter to quit.")
    quit()

ra = colokan.recv(32)
if ra == "fin":
    print "Authentication rejected"
    end()
if ra == "suc":
    print "Authentication success"
    end()
else:
    print "Received decrypted EAPOL frame: EAPOL(" + (ra) +")\tkey = PMK\n"
    appmk = colokan.recv(64)
    print "PMK in S\t: " + str(pmk)
    print "PMK from AP\t: " + str(appmk)
    if appmk == pmk:
        print "Key matched, decrypted sequence is " + str(ra)
    else:
        print "Key incorrect, rejecting frame."
