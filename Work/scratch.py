# f = open('Data/portfolio.csv', 'rt')
# data = f.read()
# print(data)
# f.close()



import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
