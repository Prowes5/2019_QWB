import pyDes

cipher = '507ca9e68709cefa20d50dcf90bb976c9090f6b07ba6a4e8'.decode('hex')

key = 'AFSAFCEDYCXCXACNDFKDCQXC'

k = pyDes.triple_des(key,pyDes.ECB,None,pad=None,padmode=pyDes.PAD_PKCS5)
d = k.decrypt(cipher)

print d