from ..models import Variable

def get_variables():
    queryset = Variable.objects.all()
    return (queryset)

def create_variable(form):
    measurement = form.save()
    measurement.save()
    return ()

def get_variable_by_id(variable_id):
    try:
        return Variable.objects.get(id=variable_id)
    except Variable.DoesNotExist:
        return None