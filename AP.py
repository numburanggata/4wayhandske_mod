import sys
import pygame
import socket
import threading
import hashlib
import binascii
import MySQLdb
import random

def sim():
    pygame.init()
    win_size = 900, 350
    black = 0, 0, 0
    black = 255, 255, 255

    screen = pygame.display.set_mode(win_size)

    pc = pygame.image.load("prot.jpg")
    pcrect = pc.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pc, (10, 10))
        pygame.display.flip()

server = '127.0.0.1'
port = 9001
bssid = "44:1C:A8:50:62:29"

print "Access Point Configuration"
essid = raw_input("ESSID\t: ")
print "BSSID\t: " + bssid
psk = raw_input("PSK\t: ")
pmk = hashlib.pbkdf2_hmac('sha256', psk, 'kmzway87aa', 100000)
print "PMK\t: " + binascii.hexlify(pmk)
print "Access Point Started (AP)\n"

colokan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
colokan.bind((server, port))

mainkan = threading.Thread(target=sim)
mainkan.start()

colokan.listen(1)
con, addr = colokan.accept()
con.sendall(essid)
con.sendall(bssid)
print "Status\t: Waiting for Authentication Requests...\n"

s_bssid = con.recv(32)
SQ = con.recv(152)

print "Authentication Request Received: Station BSSID = " + s_bssid + " || h(SQ) = " + str(SQ)

datb = MySQLdb.connect('localhost', 'root', "", 'protkrip')
datb.autocommit(True)
cursor = datb.cursor()

query = ("SELECT bssid FROM sequence_table WHERE bssid LIKE %s")
cursor.execute(query, s_bssid)
ubssid = ''
for bss in cursor:
    ubssid = bss
ubssid = ''.join(ubssid)

if ubssid:
    print (ubssid) + " already exists"
    query = ("SELECT sequence FROM sequence_table WHERE bssid LIKE %s")
    cursor.execute(query, s_bssid)
    for sq in cursor:
        sequ = sq[0]
    print "Current sequence is " + str(sequ)
    print "Correct sequence is " + str(sequ + 1)
    hsequ = hashlib.sha224(str(sequ + 1)).hexdigest()
    if hsequ == SQ:
        print "Hash sequence in AP\t: " + hsequ
        print "Hash sequence from S\t: " + SQ
        print "Continue to 4-way handshake."
        con.sendall('suc')
    else:
        print "Not the right sequence."
        print "Rejecting request."
        con.sendall('fin')
else:
    print "Continue to 4-way handshake."
    ra = random.randint(1, 2**32)
    print "Generated sequence: " + str(ra)
    ra = int(ra)
    adduser = ("INSERT INTO sequence_table (bssid, sequence) VALUES (%(bssi)s, %(seq)s)")
    entry = {'bssi': s_bssid, 'seq': ra}
    cursor.execute(adduser, entry)
    cursor.close()
    print ("Sending generated sequence using encrypted frame: EAPOL(" + str(ra) + ")\tkey: PMK")
    con.sendall(str(ra))
    con.sendall(str(pmk))

raw_input("Modified 4-Way Handshake Protocol Simulation Completed.")
raw_input("Press enter to quit.")
quit()
