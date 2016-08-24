import sys
import csv
import os
from brfss_reader import BRFSSreader

class BRFSSreader:
	def __init__(self, fname):
		self.schema = self.populate_schema(fname)

	def populate_schema(self, fname):
		schema_list = []
		f = open(fname, 'rt')
		r = csv.reader(f)
		for line in r:
			schema_list.append(self.new_schema_entry(line))
		return schema_list

	def new_schema_entry(self, row):
		entry = {
			'start': int(row[0]),
			'name': row[1],
			'length': int(row[2])
		}
		return entry

	def show_schema(self):
		l = []
		for i in self.schema:
			l.append(i['name'])
		return ','.join(l)

	def read_line(self, line):
		l = []
		for s in self.schema:
			ss = self.trim(line, s['start'], s['length'])
			l.append(ss)
		return ','.join(l)

	def trim(self, string, beg, length):
		beg = beg - 1
		end = beg + length
		return string[beg:end].rstrip()

def trim(self, beg, end):
		beg = beg - 1
		return self.rawline[beg:end].rstrip()

def writeline(output_fname, s):
	with open(output_fname, 'a') as f:
		f.write(s + '\n')

def main(argv):
	if len(argv) != 4:
		print "need three arguments, sowwy"
		sys.exit(0)
	input_fname = argv[1]
	codes_fname = argv[2]
	output_fname = argv[3]

	if os.path.isfile(output_fname):
		os.remove(output_fname)
	s = BRFSSreader(codes_fname)
	writeline(output_fname, s.show_schema())

	for line in open(input_fname):
		writeline(output_fname, s.read_line(line))

if __name__ == "__main__":
	main(sys.argv)