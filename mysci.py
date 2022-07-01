# Initialize my data variable
data = {'date':[], 'time':[], 'tempout':[]}

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    datum = line.split()
    data['date'].append(datum[0])
    data['time'].append(datum[1])
    data['tempout'].append(float(datum[2]))







