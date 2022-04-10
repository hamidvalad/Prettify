#With this program you can add or remove pretty comments to your code, have fun :)
#You can use it in both command line (python3 prettify.py filename.py) or in any IDE
#Even after editing your code you can re-run this program to re-organize your comments
#Version=1.4.2
import sys, argparse                                                                                                                                                         #*|Importing libraries
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
parser = argparse.ArgumentParser(description="With this program you can add or remove pretty comments to your code")                                                         #*|
parser.add_argument('file', help='Add pretty comment to your code', type=str, default= '')                                                                                   #*|
parser.add_argument('--type', '-t', help='Add pretty comment to your code pass 0 for removing comments', type= int, default= 1)                                              #*|Defining arguments and default values
parser.add_argument('--number', '-n', help='Number of space after maximum length', type=int, default= 7)                                                                     #*|
parser.add_argument('--symbol', '-s',  help='Pattern at end of line', type=str, default= chr(42))                                                                            #*|
parser.add_argument('--credit', '-c', help='Add optional credit in empty lines', type=str, default='--"Pretty Commands", coded with love by Github.com/HamidValad--')        #*|
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
if len(sys.argv) < 2:                                                                                                                                                        #*|Check if any argument sent in command line
    filename = input('Enter your file name: \n')                                                                                                                             #*|Ask user to input file name if not sent as argument
    n = 7                                                                                                                                                                    #*|
    Credit = '--"Pretty Commands", coded with love by Github.com/HamidValad--'                                                                                               #*|
    symbol = chr(35) + chr(42)                                                                                                                                               #*|
    Type = 1                                                                                                                                                                 #*|
else:                                                                                                                                                                        #*|
    args=parser.parse_args()                                                                                                                                                 #*|Parsing arguments
    filename = args.file                                                                                                                                                     #*|Assign argument to values
    n = args.number                                                                                                                                                          #*|
    Credit = args.credit                                                                                                                                                     #*|
    symbol = chr(35) + args.symbol                                                                                                                                           #*|
    Type = args.type                                                                                                                                                         #*|
try:                                                                                                                                                                         #*|Check the file name is correct
    with open(filename, 'r', encoding='utf-8') as file:                                                                                                                      #*|
        lines = file.readlines()                                                                                                                                             #*|
        if lines == []:                                                                                                                                                      #*|
            sys.exit()                                                                                                                                                       #*|
except:                                                                                                                                                                      #*|
    print('Wrong file name!')                                                                                                                                                #*|
    sys.exit()                                                                                                                                                               #*|In case of wrong file name exit the program
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
l = len(Credit)                                                                                                                                                              #*|
res = []                                                                                                                                                                     #*|
maximum = max(max([len(chr(35).join(i.split(symbol)[:-1]).rstrip().strip('-')) if symbol in i else len(i) for i in lines]) , l+4) + n                                        #*|Check Maximun length of lines
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
if Type:                                                                                                                                                                     #*|
    for line in lines:                                                                                                                                                       #*|
        comment = ''                                                                                                                                                         #*|
        if symbol in line and line[0] != chr(35):                                                                                                                            #*|
            comment = line.split(symbol+'|')[1]                                                                                                                              #*|Handle reusing of comments
            line = chr(35).join(line.split(symbol+'|')[:-1]).rstrip() + '\n'                                                                                                 #*|Handle reusing of this program
        if line == '\n' or (line.startswith('#') and Credit in line):                                                                                                        #*|Handle empty lines and filled line with prettifying
            res.append(chr(35) + ((maximum-l)//2)*'-' + Credit + (maximum-(maximum-l)//2-l)*'-' + f'{symbol}|\n')                                                            #*|
        elif line.endswith('\\\n') or line.startswith(chr(35)):                                                                                                              #*|Handle comments and skipped new lines
            res.append(line)                                                                                                                                                 #*|
        elif line.startswith('def') or line.lstrip().startswith('def'):                                                                                                      #*|Special comment for functions even within classes
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Definition of function\n' if not comment else comment))                                      #*|
        elif line.startswith('class'):                                                                                                                                       #*|Special comment for classes
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Description of class\n' if not comment else comment))                                        #*|
        elif line.startswith('import'):                                                                                                                                      #*|Special comment for importing libraries
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('Importing libraries\n' if not comment else comment))                                         #*|
        elif line[-1:] != '\n':                                                                                                                                              #*|Handle last line of file
            res.append(line + (maximum-len(line)+1)*' ' + symbol + '|' + comment)                                                                                            #*|
        else:                                                                                                                                                                #*|
            res.append(line[:-1] + (maximum-len(line)+2)*' ' + symbol + '|' + ('\n' if not comment else comment))                                                            #*|
else:                                                                                                                                                                        #*|In case of removing pretty comments from file
    for line in lines:                                                                                                                                                       #*|
        if symbol in line and line[0] != chr(35):                                                                                                                            #*|
            line = chr(35).join(line.split(symbol+'|')[:-1]).rstrip() + '\n'                                                                                                 #*|
            res.append(line)                                                                                                                                                 #*|
        elif line == '\n' or Credit in line:                                                                                                                                 #*|
            res.append('\n')                                                                                                                                                 #*|
        else:                                                                                                                                                                #*|
            res.append(line)                                                                                                                                                 #*|
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
result_name = 'Prety-{}'.format(filename)                                                                                                                                    #*|Generate result file name
with open(result_name, 'w') as fout:                                                                                                                                         #*|
    for line in res:                                                                                                                                                         #*|
        fout.write(line)                                                                                                                                                     #*|
#--------------------------------------------------------"Pretty Commands", coded with love by Github.com/HamidValad---------------------------------------------------------#*|
print(f'Your pretty version is ready: {result_name}')                                                                                                                        #*|
