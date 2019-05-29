def encrypt(rounds,v,key):
	v0 = v[0]
	v1 = v[1]
	sum = 0
	delta = 0x9e3779b9
	for i in range(rounds):
		v0 += (((v1<<4) ^ (v1>>5)) + v1) ^ (sum + key[sum & 3])
		v0 = v0 & 0xffffffff
		sum += delta
		sum = sum & 0xffffffff
		v1 += (((v0<<4) ^ (v0>>5)) +  v0) ^ (sum + key[(sum>>11)&3])
		v1 = v1 & 0xffffffff
		#print hex(v0),hex(v1)
	v[0] = v0
	v[1] = v1
	#print sum

def decrypt(rounds,v,key):
	v0 = v[0]
	v1 = v[1]
	delta = 0x9e3779b9
	sum = delta*rounds
	sum = sum & 0xffffffff
	for i in range(rounds):
		v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3])
		v1 = v1 & 0xffffffff
		sum -= delta
		sum = sum & 0xffffffff
		v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3])
		v0 = v0 & 0xffffffff
	v[0] = v0
	v[1] = v1