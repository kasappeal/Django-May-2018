from django.shortcuts import render

from ads.models import Ad


def home(request):
    """
    Muestra el listado de los últimos anuncios
    :param request: objeto HttpRequest
    :return: HttpResponse con respuesta
    """
    # recuperar los anuncios de la base de datos
    ads = Ad.objects.all()

    # creamos contexto
    context = {'items': ads}

    # devolver la respuesta utilizando una plantilla
    return render(request, 'ads/list.html', context)
