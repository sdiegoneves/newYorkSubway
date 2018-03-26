import pandas

def filter_by_regular(filename):
    dataFrame = pandas.read_csv(filename)
    turnstile_data = dataFrame.query("DESC == 'REGULAR'")

    return turnstile_data

df = filter_by_regular("data/file_0.txt")
df.sort_values(['UNIT'])

row = next(df.iterrows())[1]
print row

#for row in df.iterrows():
#	print row.index

#df['ENTRIESn_hourly']=0

#print df


