#!/bin/env python3
# Evan Widloski - 2019-12-05

tape = list(map(int, open('input', 'r').read().split(',')))

# tape = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

# tape = [2,3,0,3,99]

# tape = [1,9,10,3,2,3,11,0,99,30,40,50]

# tape = [1001, 0, 3, 0, 3, 1, 4, 0, 99]

# tape = [1101, 1, 1, 0, 1105, 1, 11, 1101, 2, 2, 0, 99]

# tape = [1108, 4, 2, 0, 99]

# tape = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# tape = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

def ADD(tape, params):
    print('  @ADD {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = params[0] + params[1]
def MUL(tape, params):
    print('  @MUL {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = params[0] * params[1]
def INP(tape, params):
    print('  @INP *{}'.format(params[0]))
    x = int(input('input:'))
    tape[params[0]] = x
def OUT(tape, params):
    print('  @OUT *{}'.format(params[0]))
    print('*' * 10 + ' output: {} '.format(tape[params[0]]) + '*' * 10)
def JPT(tape, params):
    if params[0] != 0:
        print('  @GOT *{}'.format(params[1]))
        return params[1]
    print('  @NOP')
def JPF(tape, params):
    if params[0] == 0:
        print('  @GOT *{}'.format(params[1]))
        return params[1]
    print('  @NOP')
def LTH(tape, params):
    print('  @LTH {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = 1 if params[0] < params[1] else 0
def EQS(tape, params):
    print('  @EQS {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = 1 if params[0] == params[1] else 0



operations = {
    # (NUM_PARAMS, (POS_PARAMS), LAMBDA_FUNC)

    1: (3, (3,), ADD),
    2: (3, (3,), MUL),
    3: (1, (1,), INP),
    4: (1, (1,), OUT),
    5: (2, (  ), JPT),
    6: (2, (  ), JPF),
    7: (3, (3,), LTH),
    8: (3, (3,), EQS)
}

index = 0
while True:

    param_modes, opcode = tape[index] // 100, tape[index] % 100

    if opcode == 99:
        break

    num_params, pos_params, operation = operations[opcode]

    params = []
    for param_index in range(1, num_params + 1):
        param_mode = (param_modes % 10**param_index) // 10**(param_index - 1)
        if param_mode == 1 or param_index in pos_params:
            params.append(tape[index + param_index])
        elif param_mode == 0:
            params.append(tape[tape[index + param_index]])
        else:
            raise Exception('Invalid param mode')

    print(tape)

    # print('  INSTR:', tape[index:index + 1 + num_params])
    # print('  PARAM:', params)

    jump_to = operation(tape, params)

    if jump_to is None:
        index += num_params + 1
    else:
        index = jump_to

print(tape)
