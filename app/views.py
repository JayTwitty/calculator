from django.shortcuts import render
import operator
# Create your views here.

def index_view(request):
    print(request.POST)
    try:
        if request.POST:
            first_number_input = float(request.POST['first_number_input'])
            second_number_input = float(request.POST['second_number_input'])
            operation = request.POST["operator"]

            if operation == "+ (add)":
                answer = operator.add(first_number_input, second_number_input)
                operation = "+"
            elif operation == "- (subtract)":
                answer = operator.sub(first_number_input, second_number_input)
                operation = "-"
            elif operation == "x (multiply)":
                answer = operator.mul(first_number_input, second_number_input)
                operation = "x"
            else:
                try:
                    answer = operator.truediv(first_number_input, second_number_input)
                except ZeroDivisionError:
                    answer = "Answer is Undefined (You can't divide by zero)"
                operation = "/"
            return render(request, 'index.html', {'answer': answer,
                                                  'operation': operation,
                                                  'first_number': first_number_input,
                                                  'second_number': second_number_input})
        else:
            return render(request,'index.html',{})
    except (ValueError, TypeError):
        answer = "INVALID ENTRY"
        return render(request, "index.html",{'answer':answer})
