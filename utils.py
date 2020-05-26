import re

#pytypes = {"None": None, "bool": bool, "int": int, "float": float, "str": str}
pytypes = ["None", "bool", "int", "float", "str"]

def np_pl_type_map(type_name):
    m = re.match('(u?int)([0-9]*)', type_name)
    if m:
        if m.group(2) in {'', '32'}:
            # should we reduce double-precision to single-precision?
            if m.group(1) == 'uint':
                return 'unsigned int'
            else:
                return 'int'
        else:
            return f'ap_{m.group(1)}<{m.group(2)}>'

    if type_name.startswith(('int', 'uint')):
        return type_name
    for pltype in pytypes:
        if type_name.startswith(pltype):
            return pltype
    return type_name
