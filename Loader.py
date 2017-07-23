def load(assembled, load_origin = 0):
    lines = assembled.split('\n')
    start_orig = 0
    for line in lines:
        if line.startswith('START'):
            start_orig = int(line.split()[1])
    if load_origin != 0:
        relocated_origin = start_orig + load_origin
    else:
        relocated_origin = start_orig
    assembled = assembled.replace("START " + str(start_orig), "START " + str(relocated_origin))
    return assembled
    