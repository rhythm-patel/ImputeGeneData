import sys

filename = sys.argv[1]
path = '../media/'+filename

# f = open("../media/testdata.txt")
f = open(path)

data = f.read()
newdata = data.upper()
f.close()

path2 = '../media/OUTPUT_'+filename

# nf = open("../media/OUTPUT.txt", "w")
nf = open(path2, "w")
nf.write(newdata)
nf.close()