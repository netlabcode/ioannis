import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8807
 
conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")


cursor = conn.cursor()

#Value id 51-66
cursor.execute('''SELECT value from objects WHERE id=51''')
result = cursor.fetchone()
record1 = result[0]
cursor.execute('''SELECT value from objects WHERE id=52''')
result = cursor.fetchone()
record2 = result[0]
cursor.execute('''SELECT valueb from objects WHERE id=53''')
result = cursor.fetchone()
record3 = result[0]
cursor.execute('''SELECT value from objects WHERE id=54''')
result = cursor.fetchone()
record4 = result[0]
cursor.execute('''SELECT value from objects WHERE id=55''')
result = cursor.fetchone()
record5 = result[0]
cursor.execute('''SELECT value from objects WHERE id=56''')
result = cursor.fetchone()
record6 = result[0]
cursor.execute('''SELECT value from objects WHERE id=57''')
result = cursor.fetchone()
record7 = result[0]
cursor.execute('''SELECT value from objects WHERE id=58''')
result = cursor.fetchone()
record8 = result[0]
cursor.execute('''SELECT value from objects WHERE id=59''')
result = cursor.fetchone()
record9 = result[0]
cursor.execute('''SELECT value from objects WHERE id=60''')
result = cursor.fetchone()
record10 = result[0]
cursor.execute('''SELECT value from objects WHERE id=61''')
result = cursor.fetchone()
record11 = result[0]
cursor.execute('''SELECT value from objects WHERE id=62''')
result = cursor.fetchone()
record12 = result[0]
cursor.execute('''SELECT value from objects WHERE id=63''')
result = cursor.fetchone()
record13 = result[0]
cursor.execute('''SELECT value from objects WHERE id=64''')
result = cursor.fetchone()
record14 = result[0]
cursor.execute('''SELECT value from objects WHERE id=65''')
result = cursor.fetchone()
record15 = result[0]
cursor.execute('''SELECT value from objects WHERE id=66''')
result = cursor.fetchone()
record16 = result[0]


#Value code
cursor.execute('''SELECT code from objects WHERE id=51''')
result = cursor.fetchone()
r1 = result[0]
cursor.execute('''SELECT code from objects WHERE id=52''')
result = cursor.fetchone()
r2 = result[0]
cursor.execute('''SELECT code from objects WHERE id=53''')
result = cursor.fetchone()
r3 = result[0]
cursor.execute('''SELECT code from objects WHERE id=54''')
result = cursor.fetchone()
r4 = result[0]
cursor.execute('''SELECT code from objects WHERE id=55''')
result = cursor.fetchone()
r5 = result[0]
cursor.execute('''SELECT code from objects WHERE id=56''')
result = cursor.fetchone()
r6 = result[0]
cursor.execute('''SELECT code from objects WHERE id=57''')
result = cursor.fetchone()
r7 = result[0]
cursor.execute('''SELECT code from objects WHERE id=58''')
result = cursor.fetchone()
r8 = result[0]
cursor.execute('''SELECT code from objects WHERE id=59''')
result = cursor.fetchone()
r9 = result[0]
cursor.execute('''SELECT code from objects WHERE id=60''')
result = cursor.fetchone()
r10 = result[0]
cursor.execute('''SELECT code from objects WHERE id=61''')
result = cursor.fetchone()
r11 = result[0]
cursor.execute('''SELECT code from objects WHERE id=62''')
result = cursor.fetchone()
r12 = result[0]
cursor.execute('''SELECT code from objects WHERE id=63''')
result = cursor.fetchone()
r13 = result[0]
cursor.execute('''SELECT code from objects WHERE id=64''')
result = cursor.fetchone()
r14 = result[0]
cursor.execute('''SELECT code from objects WHERE id=65''')
result = cursor.fetchone()
r15 = result[0]
cursor.execute('''SELECT code from objects WHERE id=66''')
result = cursor.fetchone()
r16 = result[0]


try:                   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.bind(('',PORT1))
        s1.listen()
        conn1, addr = s1.accept()
        with conn1:
            print('Server 1 from:',addr)
            while True:
                a = 1
                while a < 6:
                    #Format: mu01_id+value
                    cursor.execute('''SELECT value from objects WHERE id=51''')
                    result = cursor.fetchone()
                    if record1 != result[0]:
                        print(result[0])
                        string = "mu01_"+str(r1)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record1 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=52''')
                    result = cursor.fetchone()
                    if record2 != result[0]:
                        print(result[0])
                        string = "mu10_"+str(r2)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record2 = result[0]

                    cursor.execute('''SELECT valueb from objects WHERE id=53''')
                    result = cursor.fetchone()
                    if record3 != result[0]:
                        print(result[0])
                        string = "mu10_"+str(r3)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record3 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=54''')
                    result = cursor.fetchone()
                    if record4 != result[0]:
                        print(result[0])
                        string = "mu10_"+str(r4)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record4 = result[0]
                        
                    cursor.execute('''SELECT value from objects WHERE id=55''')
                    result = cursor.fetchone()
                    if record5 != result[0]:
                        print(result[0])
                        string = "mu02_"+str(r5)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record5 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=56''')
                    result = cursor.fetchone()
                    if record6 != result[0]:
                        print(result[0])
                        string = "mu02_"+str(r6)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record6 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=57''')
                    result = cursor.fetchone()
                    if record7 != result[0]:
                        print(result[0])
                        string = "mu03_"+str(r7)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record7 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=58''')
                    result = cursor.fetchone()
                    if record8 != result[0]:
                        print(result[0])
                        string = "mu03_"+str(r8)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record8 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=59''')
                    result = cursor.fetchone()
                    if record9 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r9)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record9 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=60''')
                    result = cursor.fetchone()
                    if record10 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r10)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record10 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=61''')
                    result = cursor.fetchone()
                    if record11 != result[0]:
                        print(result[0])
                        string = "mu05_"+str(r11)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record11 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=62''')
                    result = cursor.fetchone()
                    if record12 != result[0]:
                        print(result[0])
                        string = "mu06_"+str(r12)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record12 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=63''')
                    result = cursor.fetchone()
                    if record13 != result[0]:
                        print(result[0])
                        string = "mu07_"+str(r13)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record13 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=64''')
                    result = cursor.fetchone()
                    if record14 != result[0]:
                        print(result[0])
                        string = "mu08_"+str(r14)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record14 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=65''')
                    result = cursor.fetchone()
                    if record15 != result[0]:
                        print(result[0])
                        string = "mu08_"+str(r15)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record15 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=66''')
                    result = cursor.fetchone()
                    if record16 != result[0]:
                        print(result[0])
                        string = "mu08_"+str(r16)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record16 = result[0]

except:
   print ("Error: unable to start thread")

while 1:
   pass

