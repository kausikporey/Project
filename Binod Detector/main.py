import os

dir_contents = os.listdir()
nBinod = 0

def isBinod(filename):
    f =  open(filename,'r')
    file_contents = f.read()
    if 'binod' in file_contents.lower():
        return True
    else:
        return False    

if __name__ == "__main__":
    for item in dir_contents:
        if item.endswith('txt'):
            flag = isBinod(item)
            if(flag == True):
                print(f"Binod found in {item}.")
                nBinod += 1

print("*******Summary of Binod Detector*******")
print(f"There are {nBinod} files Contents Binod")            
