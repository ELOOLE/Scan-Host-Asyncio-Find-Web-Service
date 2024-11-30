from js import Response

def on_fetch(request):
    print("Hi there!")
    return Response.new("Hello World!")
