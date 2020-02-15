from sys import argv

for i in range(len(argv)):
    print("Argv of " + str(i) + " is " + argv[i])
argv.sort(key=len, reverse=True)
print "\n".join(argv)

