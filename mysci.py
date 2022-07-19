# Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill':12}

# data types for each column (if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Initialize my data variable
data = {}
for column in columns:
  data[column] = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    datum = line.split()
    for column in columns:
      i = columns[column]
      t = types.get(column, str)
      value = t(datum[i])
      data[column].append(value)

def estimate_windchill(t, v):
  wci = t - 0.7 * v
  return wci

windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
  windchill.append(estimate_windchill(temp, windspeed))

# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
   wc_diff = wc_orig - wc_comp
   print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')





