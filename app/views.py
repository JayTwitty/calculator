from django.shortcuts import render

# Create your views here.

def index_view(request, first_number_input, operator, second_number_input):
    first_number_input = request.POST.get('first_number_input')
    second_number_input = request.POST.get('second_number_input')
    operator = request.POST.get("operator")
    if operator == "+ (add)":
        answer = sum(first_number_input, second_number_input)
    elif operator == "- (subtract)":
        answer = sum(first_number_input, second_number_input)
    elif operator == "* (multiply)":
        answer = sum(first_number_input, second_number_input)
    elif operator == "/ (divide)":
        answer = sum(first_number_input, second_number_input)
    return render(request, 'index.html', {'answer': answer})
