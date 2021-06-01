from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = request.POST  # here you get data from form
        form = form.dict()
        print(form)
        print(type(form))
        return render(request, 'result.html', form)  # pass data to other html
    else:
        form = request.POST
    return render(request, 'index.html')            # Else statment is required


def result(request):                            # for ever url you need a view
    return render(request, 'result.html')
