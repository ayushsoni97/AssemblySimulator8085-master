def convertToMachine(assembled, symbolTable):
    lines = assembled.split("\n")
    code = ""
    for line in lines:
        if line.startswith('ADDI'):                                     #IS  00
            code+=('11000110\n')   
            val=int(line.split()[1])
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('ANI'):                                      #IS 01
            code+=('11100110\n')   
            val=int(line.split()[1])
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('JMP'):                                      #IS 02
            code+=('11000011\n')
            tag = line.split()[1].strip(":")
            val = 0
            if tag in symbolTable.keys():
                val = symbolTable[tag]
            val1=str('{0:016b}'.format(val))
            code+=(val1[0:8] + '\n')
            code+=(val1[8:16] + '\n')

        if line.startswith('JNZ'):                                  #IS 03
            code+=('11000010\n')
            tag = line.split()[1].strip(":")
            val = 0
            if tag in symbolTable.keys():
                val = symbolTable[tag]
            val1=str('{0:016b}'.format(val))
            code+=(val1[0:8] + '\n')
            code+=(val1[8:16] + '\n')

        if line.startswith('JZ'):                                   #IS 04
            code+=('11001010\n')
            tag = line.split()[1].strip(":")
            val = 0
            if tag in symbolTable.keys():
                val = symbolTable[tag]
            val1=str('{0:016b}'.format(val))
            code+=(val1[0:8] + '\n')
            code+=(val1[8:16] + '\n')

        if line.startswith('JP'):                           #IS 05
            code+=('11111010\n')
            tag = line.split()[1].strip(":")
            val = 0
            if tag in symbolTable.keys():
                val = symbolTable[tag]
            val1=str('{0:016b}'.format(val))
            code+=(val1[0:8] + '\n')
            code+=(val1[8:16] + '\n')

        if line.startswith('HLT'):                              #IS 06
            code+=('01110110\n')

        if line.startswith('SUI'):                                      #IS 07
            code+=('11010110\n')
            val=int(line.split()[1])
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('ADD A'):                        #IS 08
            code+=('11010110\n')
        if line.startswith('ADD B'):
            code+=('11010110\n')
        if line.startswith('ADD C'):
            code+=('11010110\n')
        if line.startswith('ADD D'):
            code+=('11010110\n')
        if line.startswith('ADD E'):
            code+=('11010110\n')
        if line.startswith('ADD H'):
            code+=('11010110\n')
        if line.startswith('ADD L'):
            code+=('11010110\n')

        if line.startswith('ANA A'):                #IS 09
            code+=('10100111\n')
        if line.startswith('ANA B'):
            code+=('10100000\n')
        if line.startswith('ANA C'):
            code+=('10100001\n')
        if line.startswith('ANA D'):
            code+=('10100010\n')
        if line.startswith('ANA E'):
            code+=('10100011\n')
        if line.startswith('ANA H'):
            code+=('10100100\n')
        if line.startswith('ANA L'):
            code+=('10100101\n')

        if line.startswith('SUB A'):                                #IS 10
            code+=('10010111\n')
        if line.startswith('SUB B'):
            code+=('10010000\n')
        if line.startswith('SUB C'):
            code+=('10010001\n')
        if line.startswith('SUB D'):
            code+=('10010010\n')
        if line.startswith('SUB E'):
            code+=('10010011\n')
        if line.startswith('SUB H'):
            code+=('10010100\n')
        if line.startswith('SUB L'):
            code+=('10010101\n')

        if 'WORD' in line:                                              #DL 01
            val=line.split()[2]
            for i in val:
                code+=(str('{0:08b}'.format(ord(i)))+'\n')    
        elif 'DB' in line:                                                          #DL 02
            val = int(line.split()[2])
            binary = str('{0:016b}'.format(val))
            code+=(binary[8:16] + "\n")
            code+=(binary[:8] + "\n")
        elif 'DQ' in line:                                                          #DL 03
            val = int(line.split()[2])
            binary = str('{0:032b}'.format(val))
            code+=(binary[24:32] + "\n")
            code+=(binary[16:24] + "\n")
            code+=(binary[8:16] + "\n")
            code+=(binary[:8] + "\n")
        elif 'DC ' in line:                                                              #DL 04
            val = line.split()[2]
            binary = str('{0:08b}'.format(ord(val)))
            code+=(binary[8:16] + "\n")
            code+=(binary[:8] + "\n")

        if line.startswith('POP'):                                              #IS 11
            code+=('11000001\n')

        if line.startswith('PUSH'):                                             #IS 12
            code+=('11000101\n')
            val = int(line.split()[1].strip(), 16)
            code+=(str('{0:08b}'.format(val)) + '\n')

        if line.startswith('MVI A'):                                #IS 13
            code+=('00111110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI B'):
            code+=('00000110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI C'):
            code+=('00001110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI D'):
            code+=('00010110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI E'):
            code+=('00011110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI H'):
            code+=('00100110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MVI L'):
            code+=('00101110\n')
            val=int((line.split(',')[1]).strip())
            code+=(str('{0:08b}'.format(val))+'\n')

        if line.startswith('MOV A'):                                         #IS 14
            code+=('01111110\n')
        elif line.startswith('MOV B'):
            code+=('01000110\n')
        elif line.startswith('MOV C'):
            code+=('01001110\n')
        elif line.startswith('MOV D'):
            code+=('01010110\n')
        elif line.startswith('MOV E'):
            code+=('01011110\n')
        elif line.startswith('MOV H'):
            code+=('01100110\n')
        elif line.startswith('MOV L'):
            code+=('01101110\n')
        elif line.startswith("MOV"):
            code+=('01110')
            reg = (line.split(',')[1]).strip()
            if reg == 'A':
                code+=('111\n')
            elif reg == 'B':
                code+=('000\n')
            elif reg == 'C':
                code+=('001\n')
            elif reg == 'D':
                code+=('010\n')
            elif reg == 'E':
                code+=('011\n')
            elif reg == 'H':
                code+=('100\n')
            elif reg == 'L':
                code+=('101\n')

        if line.startswith('ORA A'):        #IS 15
            code+=('10110111\n')

        if line.startswith('ORA B'):
            code+=('10110000\n')

        if line.startswith('ORA C'):
            code+=('10110001\n')

        if line.startswith('ORA D'):
            code+=('10110010\n')

        if line.startswith('ORA E'):
            code+=('10110011\n')

        if line.startswith('ORA H'):
            code+=('10110100\n')

        if line.startswith('ORA L'):
            code+=('10110101\n')

        if line.startswith('LDA'):                      #IS 16
            code+=('00111010\n')
            val=int(line.split()[1])
            val1=str('{0:08b}'.format(val))
            code+=(val1 + '\n')

        if line.startswith('LI A'):    
            if (line.split(',')[1].strip()).startswith("0x"):
                a = 16
            else:
                a = 10                 #IS 17
            code+=('10111110\n')
            val = int((line.split(',')[1]).strip(),a)
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI B'):
            if (line.split(',')[1].strip()).startswith("0x"):
                a = 16
            else:
                a = 10
            code+=('10000110\n')
            val = int((line.split(',')[1]).strip(), a)
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI C'):
            if (line.split(',')[1].strip()).startswith("0x"):
                a = 16
            else:
                a = 10
            code+=('10001110\n')
            val = int((line.split(',')[1]).strip(),a)
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI D'):
            if (line.split(',')[1].strip()).startswith("0x"):
                a = 16
            else:
                a = 10
            code+=('10010110\n')
            val = int((line.split(',')[1]).strip(),a)
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI E'):
            if (line.split(',')[1].strip()).startswith("0x"):
                a = 16
            else:
                a = 10
            code+=('10011110\n')
            val = int((line.split(',')[1]).strip(),a)
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI H'):
            code+=('10100110\n')
            val = int((line.split(',')[1]).strip())
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('LI L'):
            code+=('10101110\n')
            val = int((line.split(',')[1]).strip())
            val1 = str('{0:08b}'.format(val))
            code+=(val1+"\n")

        if line.startswith('SYSCALL'):                  #AD 06
            code+=('11001101\n')

        if line.startswith('LCL'):
            pass
        if "SET" in line:
            val = int(line.split()[2])
            binary = str('{0:016b}'.format(val))
            code+=(binary[8:16] + "\n")
            code+=(binary[:8] + "\n")

    return code

