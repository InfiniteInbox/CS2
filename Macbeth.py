import string
import matplotlib.pyplot as plt
macBeth = input('Enter the name of the file: ')
try:
    fhand = open(macBeth)
except:
    print('File cannot be opened:', macBeth)
    exit()
def main():
    topyn = input('Would you like the top words? y/n:')
    counts = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans("", "", string.punctuation)) 
        line = line.lower()
        word = line.split(" ")
        for instance in word:
            if instance not in counts:
                counts[instance] = 1
            else:
                counts[instance] += 1                   
    finaldict = dict(reversed(sorted(counts.items(), key=lambda x:x[1])))                                 
    for key in list(finaldict.keys()):
        print(key, ":", finaldict[key])

    if topyn == "y":    
            topnumb = int(input("\nHow many top?: "))                             #If they want top results, how many top results?
            print(top_n(dict(finaldict), topnumb))                                #Calls function to print top instances
    elif topyn == "n":   
        for key in list(finaldict.keys()):                                    #For every key in the dictionary,
            if finaldict[key] == int(1):                                      #If there is only one instnace of a word, returns correct grammar (time vs. times)
                print("'" + str(key) + "' was used", finaldict[key], "time.")
            else:
                print("'" + str(key) + "' was used", finaldict[key], "times.")
    else:
        print("\nSorry, please input y or n.")
    grap = input('would you like a graph? y/n:')
    if grap == 'y':
        graphing(finaldict)
    elif grap == 'n':
        break
    else:
        print('sorry incorrect input')
            

def top_n(finaldict, topnumb):

    '''
    Finds the top used words in the text file

    :param name 1: finaldict the directory being used
    :param name 2: topnumb the amount of keys returned
    :param type 1: dictionary
    :param type 2: integer
    :returns: the formatted top keys in the given directory
    :return type: string
    :raises:
    '''

    loopbreak = topnumb
    topcount = 1
    output = ""
    for key in list(finaldict.keys()):
        output = str(output) + "\n" + str(topcount) + ". '" + str(key) + "' was used " + str(finaldict[key]) + " stimes."
        topcount = topcount + 1
        loopbreak = loopbreak - 1
        if loopbreak == 0:
            return str(output + "\n")
    print(top_n(dict(finaldict), topnumb))
                       
def graphing(finaldict):
    Finallist = finaldict.items()
    Finallist = sorted(Finallist)
    x, y = zip(*Finallist)

    plt.plot(x, y)
    plt.xlabel('Key')
    plt.ylabel('Frequency of words')
    plt.title('words and their frequency')
    plt.show()
    
if __name__ == '__main__':
    main()
