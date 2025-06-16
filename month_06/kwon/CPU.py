def to_bin(num_str, bits):
    return format(int(num_str), f'0{bits}b')

N = int(input())

opcode_table = {
    'ADD': '0000', 'ADDC': '0000',
    'SUB': '0001', 'SUBC': '0001',
    'MOV': '0010', 'MOVC': '0010',
    'AND': '0011', 'ANDC': '0011',
    'OR':  '0100', 'ORC':  '0100',
    'NOT': '0101', 'NOTC': '0101',
    'MULT':'0110', 'MULTC':'0110',
    'LSFTL': '0111', 'LSFTLC': '0111',
    'LSFTR': '1000', 'LSFTRC': '1000',
    'ASFTR': '1001', 'ASFTRC': '1001',
    'RL': '1010', 'RLC': '1010',
    'RR': '1011', 'RRC': '1011',
}

for _ in range(N):
    parts = input().split()
    inst = parts[0]
    dst, src1, src2 = parts[1:]

    opcode = opcode_table[inst]
    is_immediate = '1' if inst[-1] == 'C' else '0'

    rD = to_bin(dst, 3)

    # special case: MOV, NOT 류는 rA는 항상 '000'
    if inst in ['MOV', 'MOVC', 'NOT', 'NOTC']:
        rA = '000'
    else:
        rA = to_bin(src1, 3)

    rB_or_C = to_bin(src2, 3)

    result = opcode + is_immediate + rD + rA + rB_or_C + '00'
    print(result)
