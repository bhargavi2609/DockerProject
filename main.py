import string
import socket
import os


def main():
    # creating result.txt and reading files in home/data directory
    res = open("/home/output/result.txt", "w+")
    arr = os.listdir("/home/data")
    res.write("Files in the path /home/data are as follows:- ")
    res.write(" \n")
    for x in arr:
        res.write(" \n")
        res.write(x)

    # reading Limerick.txt and counting no.of words
    file2 = open('/home/data/Limerick.txt', 'r')
    data = file2.read()
    lines2 = data.split()
    res.write(" \n")
    res.write("Total no of words in Limerick.txt is : " + str(len(lines2)))

    # reading IF.txt and counting no.of words
    file1 = open('/home/data/IF.txt', 'r')
    data = file1.read()
    lines1 = data.split()
    words1 = []
    for i in lines1:
        temp = i.translate(str.maketrans('', '', string.punctuation))
        temp = temp.capitalize()
        words1.append(temp)
    res.write(" \n")
    res.write("Total no of words in IF.txt is: "+str(len(words1)))
    res.write(" \n")

    # total no of words in both files
    res.write("Total number of words in IF.txt and Limerick.txt are: " +
              str(len(words1) + len(lines2)))
    res.write("\n")

    # counting frequency of all words and finding out three top frequencies
    frequency = []
    counts = set(words1)
    for i in counts:
        frequency.append(words1.count(i))
    words1 = list(set(words1))
    sortedwords1 = sorted(frequency, reverse=True)
    res.write("The top 3 words with maximum frequency in IF.txt are:- ")
    j = 0
    for j in range(0, 3):
        for i in range(0, len(frequency)):
            if (frequency[i] == sortedwords1[j]):
                res.write("\n")
                res.write(""+words1[i]+" - " + str(frequency[i]))

    # finding IP address of machine
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    res.write("\n")
    res.write("Current machine IP Address is:" + IPAddr)
    res.close()

    # printing final output to console
    outputfile = open('/home/output/result.txt', 'r')
    desiredoutput = outputfile.read()
    print(desiredoutput)


if __name__ == "__main__":
    main()
