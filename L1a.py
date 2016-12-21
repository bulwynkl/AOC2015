
import os



def getstring():
    if os.path.isfile('d:\bulwynkl\training\AoC2015\l1.txt')==True:
        print "Found data file"
        f = open('d:\bulwynkl\training\AoC2015\l1.txt','r')
        data = f.read().splitlines()
        f.close()
    return data[0]




def main():
    elevatorlist=""
    elevtorlist = getstring()
    print elevatorlist




if __name__ == '__main__':
    main()
