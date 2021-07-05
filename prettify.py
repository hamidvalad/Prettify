#With this program you can add or remove pretty comments to your code, have fun :)
#You can use it in both command line (python3 prettify.py filename.py) or in any IDE
#Even after editing your code you can re-run this program to re-organize your comments
#Version=1.3.0
import sys                                                                                                                                     #*|Importing libraries
a = sys.argv                                                                                                                                   #*|
if len(a)<2:                                                                                                                                   #*|Check if any argument sent in command line
    filename = input('Enter your file name: \n')                                                                                               #*|
else:                                                                                                                                          #*|
    filename = a[1]                                                                                                                            #*|Assign argument to file name
n=7                                                                                                                                            #*|
Add_comment = True if len(sys.argv)>2 and sys.argv[2].isdigit() or int(input('1 for add and 0 for remove:\n')) else False                      #*|Asking for option
with open(filename, 'r', encoding='utf-8') as file:                                                                                            #*|
    lines = file.readlines()                                                                                                                   #*|
Credit = '--Great idea by @amiralirj_pv, coded by Github.com/HamidValad--'                                                                     #*|You can replace it with any arbitrary string
symbol = chr(35) + chr(42)                                                                                                                     #*|
#-----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad------------------------------------------#*|
l = len(Credit)                                                                                                                                #*|
res = []                                                                                                                                       #*|
maximum = max(max([len(chr(35).join(i.split(symbol)[:-1]).rstrip().strip('-')) if symbol in i else len(i) for i in lines]) , l+4) + n          #*|Check Maximun length of lines
#-----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad------------------------------------------#*|
if Add_comment:                                                                                                                                #*|
    for line in lines:                                                                                                                         #*|
        if symbol in line and line[0] != chr(35):                                                                                              #*|
            comment = line.split(symbol+'|')[1]                                                                                                #*|Handle reusing of comments
            line = chr(35).join(line.split(symbol+'|')[:-1]).rstrip() + '\n'                                                                   #*|Handle reusing of this program
        if line == '\n' or Credit in line:                                                                                                     #*|Handle empty lines and filled line with prettifying
            res.append(chr(35) + ((maximum-l)//2)*'-' + Credit + (maximum-(maximum-l)//2-l)*'-' + f'{symbol}|\n')                              #*|
        elif line.endswith('\\\n') or line.startswith(chr(35)):                                                                                #*|Handle comments and skipped new lines
            res.append(line)                                                                                                                   #*|
        elif line.startswith('def') or line.lstrip().startswith('def'):                                                                        #*|Special comment for functions even within classes
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Definition of function\n' if not comment else comment))        #*|
        elif line.startswith('class'):                                                                                                         #*|Special comment for classes
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Description of class\n' if not comment else comment))          #*|
        elif line.startswith('import'):                                                                                                        #*|Special comment for importing libraries
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Importing libraries\n' if not comment else comment))           #*|
        elif line[-1:] != '\n':                                                                                                                #*|Handle last line of file
            res.append(line + (maximum-len(line)+1)*' ' + symbol + '|' + comment)                                                              #*|
        else:                                                                                                                                  #*|
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('\n' if not comment else comment))                              #*|
        comment = ''                                                                                                                           #*|
else:                                                                                                                                          #*|
    for line in lines:                                                                                                                         #*|
        if symbol in line and line[0] != chr(35):                                                                                              #*|
            line = chr(35).join(line.split(symbol+'|')[:-1]).rstrip() + '\n'                                                                   #*|
            res.append(line)                                                                                                                   #*|
        elif line == '\n' or Credit in line:                                                                                                   #*|
            res.append('\n')                                                                                                                   #*|
        else:                                                                                                                                  #*|
            res.append(line)                                                                                                                   #*|
#-----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad------------------------------------------#*|
result_name = 'Prety-{}'.format(filename)                                                                                                      #*|Generate result file name
with open(result_name, 'w') as fout:                                                                                                           #*|
    for line in res:                                                                                                                           #*|
        fout.write(line)                                                                                                                       #*|
#-----------------------------------------Great idea by @amiralirj_pv, coded by Github.com/HamidValad------------------------------------------#*|
print(f'Your pretty version is ready: {result_name}')                                                                                          #*|
