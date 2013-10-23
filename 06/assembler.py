import sys

class Parser(object):
    def __init__(self):
        #opens input stream and gets ready to parse it
        self.filename = sys.argv[1]
        f = open(self.filename)
        self.input = f.readlines()
        f.close()
        self.command = ''

    def hasMoreCommands(self):
        return len(self.input) > 0

    def advance(self):
        self.command = self.input.pop(0)

    def commandType(self):
        if self.command[0] == '@':
            if self.command[1:].isdigit(): #OR issymbol(), implement this
                return 'A_COMMAND'
        elif ';' in self.command:
            return 'C_COMMAND' #dest=comp;jump
        elif self.command[0] == '(' and self.command[-1] == ')':
            return 'L_COMMAND' #Loop

    def symbol(self):
        # call if commandType is A or L
        if self.commandType() == 'A_COMMAND':
            return command[1:] #Xxx from @Xxx
        elif self.commandType() == 'L_COMMAND':
            return command[1:-1] #Xxx from (Xxx)

    def dest(self):
        if self.commandType() == 'C_COMMAND':
            return self.command.split('=')[0]

    def comp(self):
        if self.commandType == 'C_COMMAND':
            return self.command.split('=')[1].split(';')[0]

    def jump(self):
        if self.commandType == 'C_COMMAND':
            return self.command.split('=')[1].split(';')[1]

class Code(object):
    def dest(mnemonic):
        translate = {'null': '000',
                     'M':    '001',
                     'D':    '010',
                     'MD':   '011',
                     'A':    '100',
                     'AM':   '101',
                     'AD':   '100',
                     'AMD':  '111'}
        return translate[mnemonic]

    def comp(mnemonic):
        translate = {#a=0
                     '0':  '0101010',
                     '1':  '0111111',
                     '-1': '0111010',
                     'D':  '0001100',
                     'A':  '0110000', 
                     '!D': '0001101',
                     '!A': '0110001',
                     '-D': '0001111',
                     '-A': '0110011',
                     'D+1':'0011111',
                     'A+1':'0110111',
                     'D-1':'0001110',
                     'A-1':'0110010',
                     'D+A':'0000010',
                     'D-A':'0010011',
                     'A-D':'0000111',
                     'D&A':'0000000',
                     'D|A':'0010101',
                     #a=1
                     'M'  :'1110000',
                     '!M' :'1110001',
                     '-M' :'1110011',
                     'M+1':'1110111',
                     'M-1':'1110010',
                     'D+M':'1000010',
                     'M-D':'1000111',
                     'D&M':'1000000',
                     'D|M':'1010101'}
        return translate[mnemonic]

    def jump(mnemonic):
        translate = {'null': '000',
                     'JGT' : '001',
                     'JEQ' : '010',
                     'JGE' : '011',
                     'JLT' : '100',
                     'JNE' : '101',
                     'JLE' : '110',
                     'JMP' : '111'}
        return translate[mnemonic]

def main():
    parser = Parser()
    f = open(parser.filename.split('.')[0] + '.hack', 'w')
    f.write('wefjiowefoijefw IS WORKING')
    code = Code()
    while parser.hasMoreCommands():
        print "parsing"
        parser.advance()
        if parser.commandType == 'A_COMMAND' or parser.commandType == 'L_COMMAND':
            print "found a command type " + parser.commandType
            f.write(str(bin(parser.symbol()))[2:])
        elif parser.commandType == 'C_COMMAND':
            f.write(code.dest(parser.dest()) + code.comp(parser.comp()) + code.jump(parser.jump()))
    f.close()

if __name__ == "__main__":
    main()





# class SymbolTable(object):
#     def __init__(self):
#         self.table = {}

#     def addEntry(symbol, address):
#         self.table[symbol] = address

#     def contains(symbol):
#         return symbol in self.table

#     def GetAddress(symbol):
#         return table[address]

