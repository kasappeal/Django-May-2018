from django.http import HttpResponse
from django.shortcuts import render

from ads.models import Ad


def home(request):
    """
    Muestra el listado de los últimos anuncios
    :param request: objeto HttpRequest
    :return: HttpResponse con respuesta
    """
    # recuperar los anuncios de la base de datos
    ads = Ad.objects.filter(status=Ad.PENDING).order_by('-created_on')

    # creamos contexto
    context = {'items': ads[:5]}

    # devolver la respuesta utilizando una plantilla
    return render(request, 'ads/list.html', context)


def ad_detail(request, pk):
    """
    Muestra el detalle de un anuncio
    :param request: objeto HttpRequest
    :param pk: identificador del anuncio
    :return: HttpResponse con la respuesta
    """
    # recuperar de la base de datos el anuncio que me piden
    try:
        ad = Ad.objects.select_related().get(pk=pk)
    except Ad.DoesNotExist:
        # si no existe el anuncio, devolvemos un 404
        return HttpResponse('No existe el anuncio que buscas', status=404)

    # si existe el anuncio, creamos el contexto
    context = {'ad': ad}

    # devolver la respuesta utilizando una plantilla
    return render(request, 'ads/detail.html', context)
