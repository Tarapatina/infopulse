with open('less.py','r') as file:
    for line in file:
        print(line.rstrip() +'!')
file.close()
