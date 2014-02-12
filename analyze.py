import matplotlib.pyplot as plt



def raw2int(text):
	packet3 = 0
	if len(text) == 40:
		k = 0
		for j in range(15, 33):
			#print packet2[j],
			if text[j] == '+':
				packet3 = packet3 | (1 << (17-k))
			#print k
			k += 1
	return packet3


#f = open('data/1-6,1kg.txt', 'r')
#f = open('data/2-13,6lb.txt', 'r')
#f = open('data/3_5,1kg.txt', 'r')
#f = open('data/4-94,7kg.txt', 'r')
#f = open('data/5-209,2_lb.txt', 'r')
#f = open('data/6_0kg.txt', 'r')
#f = open('data/7-0_64kg.txt', 'r')
f = open('data/8-0_64kg.txt', 'r')

lines = f.readlines()
f.close()

print 'Lines:',  len(lines)

data = []
for line in lines:
	data.append(round(float(line),0))


j = 0
'''
for i in range(0, len(data)):
	if data[i] > 1100:
		#print "%06d, %03d, %09.01f" % (i, (i-j), data[i])
		#print data[i:i+80]
		for v in data[i:i+80]:
			if v < 800:
				print 0, 
			else:
				print 1,

		print 
		j = i
'''

packet = ''
packet2 = ''
packet_index = 0
#nr = 0
bit_index = 0

for i in range(0, len(data)):
	if data[i] > 1100:
		packet2 = ''
		#bit_index = 0
		for j in range(0, len(packet)/2):
			packet2 += packet[j*2]
		veight = float(raw2int(packet2))/10.0
		print packet2, 
		print '%4.1f' % veight
		#print '%04X' % raw2int(packet2)
		#print '%04X' % raw2int('.+.+.+.++.......++++++++++++++++........')
		#print

		#print '%02X' % (nr & 0xFF)
		#nr = 0

		packet_index = 0
		packet = ''
		packet2 = ''
	
	if data[i] < 800:
		packet += '+'
		#packet_index += 1
		#nr = nr | (1 << (80-bit_index))
		#bit_index += 1
		#print bit_index 

	if data[i] > 800:
		packet += '.'
		#packet_index += 1
		#bit_index += 1
		#nr = nr << 1 | 0


#plt.plot(data)
#plt.hist(data, bins=len(lines), color='blue')
#plt.show()


'''
0   0000
1 	0001
2 	0010
3 	0011
4 	0100
5 	0101
6 	0110
7 	0111
8 	1000
9 	1001
'''

'''
+.+.+.+++...++............++++.+ .+++.+.		| 6.1     kg* 		13.448 	lb
+.+.+.+++...++............+++++. .+++.++		| 16.168  kg        13.6    lb*
+.+.+.++..+..................... ++..+.+   		| 5.1     kg* 		11.243 	lb
+.+.+.+++...++........+++.++..++ +++.+++     	| 94.7    kg* 		208.778 lb
+.+.+.+++...++........+++.++.+.+ ++++...     	| 94.891  kg        209.2   lb*
+.+.+.++........................ +.+.+.+     	| 0
'''

