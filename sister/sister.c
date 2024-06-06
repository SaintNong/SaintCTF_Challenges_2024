#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    uint32_t program_counter;
    uint32_t registers[16];
    uint16_t memory[256];
    uint16_t cmp_flag;

    uint16_t call_stack[100];
    int call_stack_idx;

} program_data;


uint16_t pop_from_call_stack(program_data* pd) {
    // Decrement call stack index
    pd->call_stack_idx--;
    
    // Get the current item at the top of stack
    uint16_t top = pd->call_stack[pd->call_stack_idx];
    
    return top;
}

void push_to_call_stack(program_data* pd) {
    // Push the program counter to call stack
    pd->call_stack[pd->call_stack_idx] = pd->program_counter;
    
    // Increment call stack index
    pd->call_stack_idx++;
}





enum {
    FLAG_EQUAL,
    FLAG_REGISTER_IS_HIGHER,
    FLAG_REGISTER_IS_LOWER
};

#define OPCODE(instruction) ((instruction & 0xF000) >> 12) // first 4 bits
#define DATA(instruction) ((instruction & 0x0FF0) >> 4) // bits 5-12
#define REGISTER(instruction) (instruction & 0x000F) // last 4 bits

uint16_t fetch(program_data* program) {
    // Get instruction from program counter
    uint16_t instruction = program->memory[program->program_counter++];
    return instruction;
}

void execute(program_data* data, uint16_t instruction) {
    int opcode = OPCODE(instruction);
    int data_value = DATA(instruction);
    int reg = REGISTER(instruction);
    

    //printf("%d\n", data->program_counter);

    switch (opcode) {
        case 0: // NOP (do nothing)
            //puts("NOP");
            break;

        case 1: // LOAD data into register
            data->registers[reg] = data_value;
            //printf("LOAD number %d -> r%d\n", data_value, reg);
            break;

        case 2: // STORE register to memory
            data->memory[data_value] = data->registers[reg];
            //printf("STORE m%d <- r%d (%d)\n", data_value, reg, data->registers[reg]);
            break;

        case 3: // ADD memory location to register
            data->registers[reg] += data->memory[data_value];
            //printf("ADD m%d to r%d\n", data_value, reg);
            break;

        case 4: // SUBTRACT memory location from register
            data->registers[reg] -= data->memory[data_value];
            //printf("SUBTRACT m%d from r%d\n", data_value, reg);
            break;

        case 5: // MULT register by memory location
            data->registers[reg] *= data->memory[data_value];
            //printf("MULT r%d with m%d\n", reg, data_value);
            break;

        case 6: // JUMP to memory address
            data->program_counter = data_value;
            //printf("JUMP to %d\n", data_value);
            break;

        case 7: // J_IF_EQU (Jump if equal)
            if (data->cmp_flag == FLAG_EQUAL) {
                //printf("JUMP (eq) to %d\n", data_value);
                data->program_counter = data_value;
            }
            //printf("JUMP (not eq) to %d\n", data_value);
            break;

        case 8: // J_IF_ABV (Jump if above)
            if (data->cmp_flag == FLAG_REGISTER_IS_HIGHER) {
                data->program_counter = data_value;
                //printf("JUMP (abv) to %d\n", data_value);
            }
            //printf("JUMP (not abv) to %d\n", data_value);
            break;

        case 9: // J_IF_BLW (Jump if below)
            if (data->cmp_flag == FLAG_REGISTER_IS_LOWER) {
                data->program_counter = data_value;
                //printf("JUMP (blw) to %d\n", data_value);
            }
            //printf("JUMP (not blw) to %d\n", data_value);
            break;

        case 10: // COMPARE register with memory
            if (data->registers[reg] == data->memory[data_value]) {
                data->cmp_flag = FLAG_EQUAL;
                //puts("EQUAL!");
            } else if (data->registers[reg] > data->memory[data_value]) {
                data->cmp_flag = FLAG_REGISTER_IS_HIGHER;
                //puts("REG HIGHER!");
            } else {
                data->cmp_flag = FLAG_REGISTER_IS_LOWER;
                //puts("REG LOWER!");
            }
            break;

        case 11: // OUTPUT character to terminal
            // prints character as charcode
            printf("%c", data->memory[data_value]);
            break;

        case 12: // INPUT number into memory and register
            uint16_t value;
            int _ = scanf("%hu", &value);

            // Memory
            data->memory[data_value] = value;

            // Register
            data->registers[reg] = value;
            break;

        case 13: // TERM program
            exit(0);
            break;

        case 14: // RET from function call
            // Pop old program_counter from call stack
            data->program_counter = pop_from_call_stack(data);
            break;

        case 15: // CALL function (go to address)
            //printf("CALL to %d\n", data_value);

            // Push program_counter to call stack
            push_to_call_stack(data);

            // Act like a JUMP instruction
            data->program_counter = data_value;
            break;


        default: // Unknown instruction
            exit(-1);
            break;
    }
}


void initialize_program(program_data *pd, uint16_t *memory_reel, int size_memory)
{
    for (int i = 0; i < size_memory; i++) {
        pd->memory[i] = memory_reel[i];
    }

}

int main() {
    program_data pd = {}; // Initialize program data to all zeroes

    
    uint16_t memory_reel[] = {
61840, 49402, 5215, 8527, 41290, 28800, 62240, 53248, 63040, 53248, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5823, 10447, 47296, 5727, 10447, 47296, 6047, 10447, 47296, 5039, 10447, 47296, 4623, 10447, 47296, 57344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6015, 10447, 47296, 5935, 10447, 47296, 5887, 10447, 47296, 5871, 10447, 47296, 5759, 10447, 47296, 4271, 10447, 47296, 57344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5839, 10447, 47296, 5887, 10447, 47296, 5887, 10447, 47296, 5823, 10447, 47296, 4623, 10447, 47296, 5695, 10447, 47296, 5839, 10447, 47296, 5887, 10447, 47296, 5951, 10447, 47296, 5727, 10447, 47296, 5935, 10447, 47296, 4271, 10447, 47296, 57344, 0, 0, 0, 0, 0, 0, 0, 0, 5951, 10607, 47456, 5663, 10607, 47456, 5791, 10607, 47456, 5871, 10607, 47456, 5967, 10607, 47456, 6079, 10607, 47456, 5695, 10607, 47456, 5983, 10607, 47456, 5951, 10607, 47456, 5967, 10607, 47456, 4879, 10607, 47456, 5855, 10607, 47456, 5631, 10607, 47456, 5663, 10607, 47456, 5951, 10607, 47456, 5951, 10607, 47456, 4927, 10607, 47456, 5855, 10607, 47456, 5679, 10607, 47456, 5839, 10607, 47456, 6047, 10607, 47456, 5631, 10607, 47456, 5695, 10607, 47456, 4879, 10607, 47456, 4879, 10607, 47456, 5839, 10607, 47456, 5631, 10607, 47456, 5935, 10607, 47456, 4895, 10607, 47456, 5759, 10607, 47456, 5775, 10607, 47456, 5967, 10607, 47456, 5119, 10607, 47456, 6111, 10607, 47456, 4271, 10607, 47456, 57344, 0, 0, 0, 0, 0,
    };
    int size_memory = 256;

    initialize_program(&pd, memory_reel, size_memory);

 

    while (1) {
        uint16_t instruction = fetch(&pd);
        execute(&pd, instruction);

    }

    return 0;
}

