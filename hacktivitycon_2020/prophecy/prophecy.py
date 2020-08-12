import socket
from pwn import *
import re

while True:
    answers = open("/home/kali/Downloads/answers.txt", 'a+')
    answers.seek(0,0)
    conn = remote('jh2i.com', 50012)
    answer_list = answers.readlines()

    data = conn.recvuntilS(b'> ')
    print(data)

    for answer in answer_list:    
        print(answer)
        conn.send(answer)    
        data = conn.recvuntilS(b'> ')
    conn.send("123\n")
    data = conn.recvuntilS(b'\n \n')
    print(data)
    if data.find('F A I L U R E') != -1:
        new_answer = re.findall(r'\d+', data)
        print("FOund new answer:")
        print(new_answer[0])
        answers.seek(0, 2)
        answers.write(new_answer[0] + '\n')
    answers.close()
    if data.find('flag') != -1:
        break




