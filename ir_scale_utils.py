import irtoy
import serial
import matplotlib.pyplot as plt

def raw2int(text):
	packet3 = 0
	status = 0

	if len(text) == 40:
		k = 0
		for j in range(15, 33):
			if text[j] == '+':
				packet3 = packet3 | (1 << (17-k))
			k += 1

		k = 0
		for j in range(13, 15):
			if text[j] == '+':
				status = status | (1 << (1-k))
			k += 1

	return packet3, status


def get_data(file):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def get_data_serial(port):
	lines = []
	with serial.Serial(port) as serialDevice:
		print 'Prepare...'
		toy = irtoy.IrToy(serialDevice)
		print 'Reading IR signals...'
		raw_data = toy.receive()
		i = 0
		for tmp in range(0, len(raw_data) / 2):
			value = (raw_data[i]*0x100+raw_data[i+1])*21.3333
			i += 2
			lines.append(str(round(value, 4)))
		return lines


def preprocess(lines):
	data = []
	for line in lines:
		data.append(round(float(line),0))

	packet = ''
	packet2 = ''
	packets = []

	for i in range(0, len(data)):
		if data[i] > 1100:

			for j in range(0, len(packet)/2):
				packet2 += packet[j*2]
			packets.append(packet2)

			packet = ''
			packet2 = ''
		
		if data[i] < 800:
			packet += '+'

		if data[i] > 800:
			packet += '.'
	return packets

def get_real_weight(packets):
	weights = []
	for packet in packets:
		raw_weight, status = raw2int(packet)
		weight = float(raw_weight)/10.0
		if status == 3:
			weights.append(weight)

	weight_sum = 0
	for w in weights:
		weight_sum += w

	if len(weights) > 0:
		avg_weight = weight_sum / len(weights)
		return avg_weight
	else:
		return 0.0
