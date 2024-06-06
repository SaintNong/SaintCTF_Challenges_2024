class Function:
    def __init__(self, start_addr, instructions):

        self.instructions = instructions
        
        self.instructions.append("RET 0 0")

        self.length = len(instructions)
        self.address = start_addr

    def create_call(self):
        return f"CALL {self.address} 0"
    


def create_print_function(start_address, string, mem_addr, register, include_newline=True) -> Function:
    """
    Creates a print function from a string in Saint Assembly
    The memory address and register given will be used
    """
    
    # add newline if not present
    if not string.endswith("\n") and include_newline:
        string += "\n"



    instructions = []

    for char in string:
        charcode = ord(char)
        
        # Load the charcode into the register
        instructions.append(f"LOAD {charcode} {register}")

        # Save the register to memory
        instructions.append(f"STORE {mem_addr} {register}")
    
        # Print from memory
        instructions.append(f"OUTPUT {mem_addr} 0")
    
    print_func = Function(start_address, instructions)
    return print_func

def get_input(addr, reg):
    return f"INPUT {addr} {reg}"

def set_mem(value, memory):
    return [
            f"LOAD {value} 15",
            f"STORE {memory} 15",
    ]


def write_functions(functions):
    instructions = ["NOP"] * 256


    for function in functions:
        start = function.address
        current_addr = start

        for line in function.instructions:
            instructions[current_addr] = line

            current_addr += 1
    return instructions
        


input_func = create_print_function(25, "key: ", 140, 15, include_newline=False)
wrong_func = create_print_function(50, "wrong", 140, 15)
right_func = create_print_function(100, "look closer", 140, 15)

flag_func = create_print_function(145, "saint{cust0m_ass3mbly_c00l_r1ght?}", 150, 15)

functions = [input_func, wrong_func, right_func, flag_func]
instructions = write_functions(functions)

# MAIN FUNCTION START HERE
# Print "Key: "
instructions[0] = input_func.create_call()
# Get input
instructions[1] = get_input(15, 10)

# Input == 69
instructions[2] = "LOAD 69 15"
instructions[3] = "STORE 20 15"
instructions[4] = "CMP 20 10"

# If input != 69
instructions[5] = "J_IF_EQU 8 0"



instructions[6] = wrong_func.create_call()
instructions[7] = "TERM"


# Else
instructions[8] = right_func.create_call()
instructions[9] = "TERM"
# End if



data = "\n".join(instructions)



with open("program.saint", "w") as file:
    file.write(data)

