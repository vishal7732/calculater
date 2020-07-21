from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def pos(request):
    return render(request, 'pos.html')
    
def calc(request):
    value1 = request.GET["value1"]
    value2 = request.GET["value2"]
    operation=request.GET["operation"]
    
    
    def ca():
        add = int(value1)+int(value2)
        minus = int(value1)-int(value2)
        multi = int(value1)*int(value2)
        if operation == "+":
            return add
        if operation == "-":
            return minus
        if operation == "*":
            return multi
    go = {'go':ca()}
    
    return render(request, 'index.html', go)

def calc1(request):

    value1 = int(request.POST["value_1"])
    value2 = int(request.POST["value_2"])
    operation=request.POST["operation_1"]
    
    def dal():
        add1 = value1+value2   
        minus1 = value1-value2
        multi1 = value1*value2
        if operation == "+":
            return add1
        if operation == "-":
            return minus1
        if operation == "*":
            return multi1
        
    do = {'do':dal()}
        
    return render(request, 'pos.html', do)