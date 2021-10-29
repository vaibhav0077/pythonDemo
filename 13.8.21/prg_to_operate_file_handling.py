
# r -> read only

# rb -> read brinary format

# r+/w+ -> read and write both

# rb+/wb+ -> read & write both brinary format

# w -> write only

# wb ->  write only in binary format

# a -> append mode

# ab -> append in binary format

# a+ -> apppend & read both

# ab+ -> append and read both in binary format.
import os  
print(os.getcwd() ) 
try:
    fil = open("demo.txt","r+")

    if fil:
        print("file exist ")
        con = fil.read()
        lena = len(con)
        print("Content is :\n",con)
        print("\n\n\n\n")
        line = fil.readline()
        lines = fil.readlines()
        print("Line : ", line)
        print("Lines : ",lines)
        print("\n\n\n\n")
        print("Length of file is ", lena)
        print("\n\n\n\n")
        

    else:
        print("A")
    
    

finally:
    print(fil)
    for i in fil:
            print(i)
        # fil = open("demo.txt", "a")

    fil.close()
    print("File Closed")
