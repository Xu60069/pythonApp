import binascii
#binary file dump
def bin_dump(f):
    with open("bin_dump.out", 'w') as fw:
        with open(f,'rb') as fr:
            line = fr.readline()
            fw.write(line.hex())
            fw.write("\n")
        with open(f,'r') as fr:
            line = fr.readline()
            for ch in line:
                fw.write(ch)
                fw.write(" ")
            fw.write("\n")

bin_dump("config-proj.xcl")
