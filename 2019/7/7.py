#!/bin/env python3
# Evan Widloski - 2019-12-08
import itertools
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

tape = list(map(int, open('input', 'r').read().split(',')))
# tape = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# tape = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
#         101,5,23,23,1,24,23,23,4,23,99,0,0]
# tape = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#         1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]


def ADD(tape, params, inp, out):
    log.debug('  @ADD {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = params[0] + params[1]
def MUL(tape, params, inp, out):
    log.debug('  @MUL {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = params[0] * params[1]
def INP(tape, params, inp, out):
    x = int(inp.pop(0))
    log.debug('  @INP {} -> *{}'.format(x, params[0]))
    tape[params[0]] = x
def OUT(tape, params, inp, out):
    log.debug('  @OUT *{}'.format(params[0]))
    # print('*' * 10 + ' output: {} '.format(tape[params[0]]) + '*' * 10)
    out.append(tape[params[0]])
def JPT(tape, params, inp, out):
    if params[0] != 0:
        log.debug('  @GOT *{}'.format(params[1]))
        return params[1]
    log.debug('  @NOP')
def JPF(tape, params, inp, out):
    if params[0] == 0:
        log.debug('  @GOT *{}'.format(params[1]))
        return params[1]
    log.debug('  @NOP')
def LTH(tape, params, inp, out):
    log.debug('  @LTH {}, {} -> *{}'.format(params[0], params[1], params[2]))
    tape[params[2]] = 1 if params[0] < params[1] else 0
def EQS(tape, params, inp, out):
    log.debug('  @EQS {}, {} -> *{}'.format(params[0], params[1], params[2]))
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

def compute(tape, inp):
    # program output
    out = []

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

        log.debug(tape)

        # print('  INSTR:', tape[index:index + 1 + num_params])
        # print('  PARAM:', params)

        jump_to = operation(tape, params, inp, out)

        if jump_to is None:
            index += num_params + 1
        else:
            index = jump_to

    return tape, out

trials = itertools.permutations([0, 1, 2, 3, 4])
max_output = 0
for phase_settings in trials:
    output = [0]
    print('---------- phase {} -----------'.format(phase_settings))
    for phase_setting in phase_settings:
        print('input:', output)
        tape, output = compute(tape, [phase_setting, output[0]])

    print('output:', output)
    if output[0] > max_output:
        max_phase_settings = phase_settings
        max_output = output[0]

print('maximum output:', max_output)
