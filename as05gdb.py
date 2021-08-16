import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.5.0.11'
HOST2 = '100.5.0.12'
HOST3 = '100.5.0.13'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.7", database="CRoF", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h,
        		i
    		)

			cursor.execute(" INSERT INTO s05m1(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res, tr_cb_ctrl, tr_cb_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("1")

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST2, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h,
        		i,
        		j,
        		k,
        		l,
        		m,
        		n,
        		o,
        		p
    		)

			cursor.execute(" INSERT INTO s05m2(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res, g_cb_ctrl, g_cb_res, f_res, ld_res, g_p_ctrl, g_p_res, g_q_res, g_v_ctrl, g_v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("2")


def serverThree():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST3, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j,k,l,m,n = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h,
        		i,
        		j,
        		k,
        		l,
        		m,
        		n
    		)

			cursor.execute(" INSERT INTO s05m3(dtime, cb_ctrl, cb_res, f_res, hv_p_res, hv_q_res, ld_res, lv_p_res, lv_q_res, tap, tap_ctrl, tap_mode, tap_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("3")


# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverThree, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass