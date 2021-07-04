#with this program you can add pretty comments to your code, have fun :)
#you can use it in both command line (python3 prettify.py filename.py) or in any IDE
#Version=1.1.0
import sys                                                                                                                                   #*|Importing libraries
a = sys.argv                                                                                                                                 #*|
if len(a)<2:                                                                                                                                 #*|Check if any argument sent in command line
    filename = input('Enter your file name: \n')                                                                                             #*|
else:                                                                                                                                        #*|
    filename = a[1]                                                                                                                          #*|Assign argument to file name
n=6                                                                                                                                          #*|
with open(filename, 'r') as file:                                                                                                            #*|
    lines = file.readlines()                                                                                                                 #*|
#----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad-----------------------------------------#*|
symbol = chr(35) + chr(42)                                                                                                                   #*|
Credit = '--Great idea by @amiralirj_pv, coded by Github.com/HamidValad--'                                                                   #*|You can replace it with any arbitrary string
l = len(Credit)                                                                                                                              #*|
res = []                                                                                                                                     #*|
maximum = max(max([len(chr(35).join(i.split(symbol)[:-1]).rstrip().strip('-')) if symbol in i else len(i) for i in lines]) , l+4) + n        #*|Check Maximun length of lines
#----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad-----------------------------------------#*|
print(maximum)                                                                                                                               #*|
for line in lines:                                                                                                                           #*|
    if symbol in line and line[0] != chr(35):                                                                                                #*|Handle reusing of this program
        line = chr(35).join(line.split(symbol)[:-1]).rstrip() + '\n'                                                                         #*|
    if line == '\n' or Credit in line:                                                                                                       #*|Handle empty lines and filled line with prettifying
        res.append(chr(35) + ((maximum-l)//2)*'-' + Credit + (maximum-(maximum-l)//2-l)*'-' + f'{symbol}|\n')                                #*|
    elif line.endswith('\\\n') or line.startswith(chr(35)):                                                                                  #*|Handle comments and skipped new lines
        res.append(line)                                                                                                                     #*|
    elif line.startswith('def') or line.lstrip().startswith('def'):                                                                          #*|Special comment for functions
        res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + 'Definition of function\n')                                        #*|
    elif line.startswith('class'):                                                                                                           #*|Special comment for functions within calsses
        res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + 'Definition of function\n')                                        #*|
    elif line.startswith('import'):                                                                                                          #*|Special comment for importing libraries
        res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + 'Importing libraries\n')                                           #*|
    elif line[-1:] != '\n':                                                                                                                  #*|Handle last line of file
        res.append(line + (maximum-len(line)+1)*' ' + symbol + '|' )                                                                         #*|
    else:                                                                                                                                    #*|
        res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|\n')                                                                   #*|
#----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad-----------------------------------------#*|
result_name = 'Prety-{}'.format(filename)                                                                                                    #*|Generate result file name
with open(result_name, 'w') as fout:                                                                                                         #*|
    for line in res:                                                                                                                         #*|
        fout.write(line)                                                                                                                     #*|
#----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad-----------------------------------------#*|
print(f'Your pretty version is ready: {result_name}')                                                                                        #*|