from django.shortcuts import render

# Crefrom django.shortcuts import render
def hello_world(request):
    return render(request, 'hello_world.html', {})
