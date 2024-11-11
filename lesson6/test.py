import portie.reader

records = portie.reader.read_csv("../data/portfolio.csv", [str,str,int,float])
print(records)