def parse_instruction(instruction):
    parts = instruction.strip().split()

    opcode = parts[0].upper()
    operands = parts[1:]

    return opcode, operands

def encode_instruction(opcode, operands):

    opcodes = {
        'NOP':       0,
        'LOAD':      1,
        'STORE':     2,
        'ADD':       3,
        'SUB':       4,
        'MULT':      5,
        'JUMP':      6,
        'J_IF_EQU':  7,
        'J_IF_ABV':  8,
        'J_IF_BLW':  9,
        'CMP':      10,
        'OUTPUT':   11,
        'INPUT':    12,
        'TERM':     13,
        'RET':      14,
        'CALL':     15
    }

    if opcode not in opcodes:
        raise ValueError(f"Unknown opcode: {opcode}")

    opcode_val = opcodes[opcode] << 12

    if opcode in ['NOP', 'TERM']:
        return opcode_val


    value = int(operands[0])
    register = int(operands[1])


    return opcode_val | (value << 4) | register


def assemble(assembly_code):
    """ Convert assembly instructions to machine code. """
    machine_code = []
    for line in assembly_code.split('\n'):
        if line.strip() == "" or line.strip().startswith('#'):  # Ignore empty lines and comments
            continue
        opcode, operands = parse_instruction(line)
        machine_instruction = encode_instruction(opcode, operands)
        machine_code.append(machine_instruction)
    return machine_code

with open("program.saint", "r") as file:
    assembly_code = file.read()




machine_code = assemble(assembly_code)

print(assembly_code)
for idx, code in enumerate(machine_code):
    print(f"{code}", end=", ")

print("")

