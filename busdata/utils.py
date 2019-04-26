from busdata.models import *

def getDictFromQueryset(queryset):
    Model = queryset.model
    valuesDict = queryset.values()
    foreignKeys = {}
    for f in Model._meta.fields:
        if isinstance(f, models.ForeignKey):
            foreignKeys[f.column] = f.name
    if foreignKeys:
        for d in valuesDict:
            obj = Model.objects.get(id=d['id'])
            for k in d.keys():
                if k in foreignKeys.keys():
                    foreignKeyObj = (getattr(obj,foreignKeys[k]))
                    if foreignKeyObj:
                        d[k] = foreignKeyObj.__str__()
    return valuesDict

