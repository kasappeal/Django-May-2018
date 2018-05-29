from django.http import HttpResponse

from ads.models import Ad


def home(request):
    """
    Muestra el listado de los últimos anuncios
    :param request: objeto HttpRequest
    :return: HttpResponse con respuesta
    """
    # recuperar los anuncios de la base de datos
    ads = Ad.objects.all()

    # construir el documento HTML
    html = '<ul>'
    for ad in ads:
        html += '<li>{0}</li>'.format(ad)
    html += '</ul>'

    # devolver la respuesta
    return HttpResponse(html)
