#with this code you can add pretty comments to your code, have fun :)
#you can use it in both command line (python3 prettify.py filename.py) or any IDE
#Version=1.0.0
import sys                                                                                             #-|Importing libraries
a = sys.argv                                                                                           #-|
if len(a)<2:                                                                                           #-|Check if any argument sent in command line
    filename = input('Enter your file name: \n')                                                       #-|
else:                                                                                                  #-|
    filename = a[1]                                                                                    #-|Assign argument to file name
n=6                                                                                                    #-|
with open(filename, 'r') as file:                                                                      #-|
    lines = file.readlines()                                                                           #-|
#---------------------------Great idea by @amiralirj_pv, code by @HamidValadb----------------------------|
Credit = '-Great idea by @amiralirj_pv, code by @HamidValadb-'                                         #-|You can replace it with same length string of '-'
res = []                                                                                               #-|
maximum = max([len(i) for i in lines])                                                                 #-|Check Maximun length of lines
maximum = max(maximum, len(Credit)+4) + n                                                              #-|Add an arbitrary number of white space
#---------------------------Great idea by @amiralirj_pv, code by @HamidValadb----------------------------|
for line in lines:                                                                                     #-|
    if line == '\n':                                                                                   #-|Handle empty lines
        res.append('#' + ((maximum-53)//2)*'-' + Credit + (maximum-(maximum-53)//2-53)*'-' + '|\n')    #-|
    elif line.endswith('\\\n') or line.endswith('#'):                                                  #-|Handle comments and skiped new lines
        res.append(line)                                                                               #-|
    elif line.startswith('def'):                                                                       #-|Special comment for functions
        res.append(line[:-1] + (maximum-len(line)-2)*' ' + '#-' + '|' + 'Definition of function\n')    #-|
    elif line.startswith('import'):                                                                    #-|Special comment for importing libraries
        res.append(line[:-1] + (maximum-len(line)-2)*' ' + '#-' + '|' + 'Importing libraries\n')       #-|
    elif line[-1:] != '\n':                                                                            #-|Handle last line
        res.append(line + (maximum-len(line)-3)*' ' + '#-' + '|' )                                     #-|
    else:                                                                                              #-|
        res.append(line[:-1] + (maximum-len(line)-2)*' ' + '#-' + '|\n')                               #-|
#---------------------------Great idea by @amiralirj_pv, code by @HamidValadb----------------------------|
result_name = 'Prety-{}'.format(filename)                                                              #-|Generate result file name
with open(result_name, 'w') as fout:                                                                   #-|
    for line in res:                                                                                   #-|
        fout.write(line)                                                                               #-|
#---------------------------Great idea by @amiralirj_pv, code by @HamidValadb----------------------------|
print(f'Your pretty version is ready: {result_name}')                                                  #-|