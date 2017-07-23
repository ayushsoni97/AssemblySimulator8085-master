def link(assembled, link_origin = 0):
    externals = {}
    start_orig = 0
    fexts = open("exported.extrn", "r+")
    exportedVars = fexts.read().split("\n")
    if len(exportedVars)>0:
        try:
            for var in exportedVars:
                name,val = var.strip().split()
                externals[name] = int(val)
        except:
            pass
    lines = assembled.split('\n')
    for line in lines:
        if line.startswith('START'):
            start_orig = int(line.split()[1])
        if "?" in line:
            exter = line.split()[1]
            print externals.keys(), exter
            if exter in externals.keys():
                assembled = assembled.replace(line, "LDA " + exter + "\nMOV " + exter + ", A\n")
    if link_origin != 0:
        relocated_origin = start_orig + link_origin
    else:
        relocated_origin = start_orig
    assembled = assembled.replace("START " + str(start_orig), "START " + str(relocated_origin))
    return assembled
