import sys
import getopt

# script is based on the one found here https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB/

mappings = { 0x04:"A",  0x05:"B",  0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G",  0x0B:"H", 0x0C:"I",  0x0D:"J", 0x0E:"K", 0x0F:"L", 0x10:"M", 0x11:"N",0x12:"O",  0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U",0x19:"V", 0x1A:"W", 0x1B:"X", 0x1C:"Y", 0x1D:"Z", 0x1E:"1", 0x1F:"2", 0x20:"3", 0x21:"4", 0x22:"5",  0x23:"6", 0x24:"7", 0x25:"8", 0x26:"9", 0x27:"0", 0x28:"[ENTER]", 0x29:"[ESCAPE]", 0x2a:"[DEL]",  0X2B:"    ", 0x2C:" ",  0x2D:"-", 0x2E:"=", 0x2F:"[",  0x30:"]",  0x31:"\\", 0x32:"~", 0x33:";",  0x34:"'", 0x36:",",  0x37:"." }

nums = []



"""
This section extracts the 3rd byte as long as the 4th byte is empty.
I noticed that occasionally when capturing key presses of naturally typing  a duplicate events with two key presses would be genereated. This is unneccessary and thus filtered.
"""

def extract_key_presses(key_strokes_file):
	keys = open(key_strokes_file)
	
	for line in keys:
		if line[6:8] == "00":
			#print (line[4:6])
			nums.append(int(line[4:6],16))
			#print(nums)
	keys.close()

def print_key_presses_to_terminal():
	output = ""

	for n in nums:
		if n == 0 :
			continue
		if n in mappings:
			output += mappings[n]
		else:
			output += '[unknown]'
	print('Output :' + output)

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'decode.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
				inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	#print 'Input file is "', inputfile
	#print 'Output file is "', outputfile
	extract_key_presses(inputfile)
	print_key_presses_to_terminal()

if __name__ == "__main__":
   main(sys.argv[1:])
