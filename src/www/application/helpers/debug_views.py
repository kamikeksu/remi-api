from django.http import HttpResponse

def debug(request):
    response = HttpResponse()
    response['Content-Type'] = 'text/plain'

    content = ''
    try:
        f = open("/opt/www/.build", "r")
        content = f.read()
    except:
        content = ''
    response.write(content)

    return response
