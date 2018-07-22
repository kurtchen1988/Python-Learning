def to_dict(model, columns=None, append_columns=None):
    '''model to dict'''
    from sqlalchemy.orm import class_mapper
    def to_str(o):
        if (isinstance(o, int) or isinstance(o, float) or o == None):
            return o

        return str(o)

    if columns == None:
        columns = [c.key for c in class_mapper(model.__class__).columns]

    if append_columns is not None:
        columns += append_columns

    return dict((c, to_str(getattr(model, c))) for c in columns)

def models_to_dict(models):
    return [to_dict(o) for o in models]