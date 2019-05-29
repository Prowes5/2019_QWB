# -*- coding: utf-8 -*-
import xtea

tmp = [32,67,111,-67,115,-23,-90,-36,-85,40,-28,109,-105,-55,74,-128,-7,70,111,113,25,-115,19,-104,-57,22,37,60,-99,107,-14,-70,102,55,57,48,53,125]
for i in range(len(tmp)):
	tmp[i] = tmp[i] & 0xff
cipher = []

k = [0,0,0,0]
r = 32

for i in range(0,len(tmp)-9,4):
	tmp_cipher = tmp[i]<<0
	tmp_cipher = tmp_cipher | (tmp[i+1]<<8)
	tmp_cipher = tmp_cipher | (tmp[i+2]<<16)
	tmp_cipher = tmp_cipher | (tmp[i+3]<<24)
	cipher.append(tmp_cipher)

flag = ''

for i in range(0,len(cipher),2):
	v = []
	v.append(cipher[i])
	v.append(cipher[i+1])
	xtea.decrypt(r,v,k)
	#print v
	for j in range(0,len(v)):
		flag += hex(v[j])[2:-1].decode('hex')[::-1]

for i in range(len(tmp)-6,len(tmp)):
	flag += chr(tmp[i])

print flag