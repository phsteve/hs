line1 = "Mux16(a[%d]=a[%d], b[%d]=b[%d], sel=sel[0], out[%d]=w%d);"
line2 = "Mux16(a[%d]=c[%d], b[%d]=d[%d], sel=sel[0], out[%d]=w%d);"
line3 = "Mux16(a[%d]=w%d, b[%d]=w%d, sel=sel[1], out[%d]=out[%d]);"

def prnt(line):
    for i in range(16):
        print line %(i, i, i, i, i, i)
#lines = [line1, line2, line3]
#for line in lines:
#    prnt(line)

for i in range(16):
    print line1 %(i, i, i, i, i, i)

for i in range(16):
    print line2 %(i, i, i, i, i, i+16)

for i in range(16):
    print line3 %(i, i, i, i+16, i, i)