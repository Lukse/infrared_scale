import irtoy
import serial

with serial.Serial('COM43') as serialDevice:
	print 'Prepare'
	toy = irtoy.IrToy(serialDevice)
	print 'Read...'
	raw_data = toy.receive()
	#print 'print'
	#toy.transmit(irCode)
	#print irCode
	print 'Length:', len(raw_data), raw_data
	print

	f = open('log.txt', 'w')
	#print f

	#timing = []
	i = 0
	for tmp in range(0, len(raw_data) / 2):
		value = (raw_data[i]*0x100+raw_data[i+1])*21.3333
		i += 2
		f.write(str(round(value, 4)))
		f.write('\n')
	f.close()
