def copy_obj_attr(source, target):
    if isinstance(source, dict):
        soudict = source
    else:
        soudict = source.__dict__
    if isinstance(target, dict):
        tardict = target
    else:
        tardict = target.__dict__
    # #print(soudict)
    # #print(tardict)
    for tarkey in tardict.keys():
        if tarkey in soudict:
            setattr(target, tarkey, soudict.get(tarkey))
    return target


def list_dinstinct(lst: list):
    temp = []
    for item in lst:
        if not item in temp:
            temp.append(item)
    return temp
