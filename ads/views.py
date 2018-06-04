from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from ads.forms import AdForm
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


@login_required
def ad_form(request):
    """
    Muestra el formulario para crear un anuncio y lo procesa
    :param request: objeto HttpRequest
    :return: HttpResponse con la respuesta
    """
    # si la peticion es post, entonces tenemos que crear el anuncio
    if request.method == 'POST':
        ad = Ad()
        ad.owner = request.user
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            # creamos el anuncio
            ad = form.save()
            # limpiar el formulario
            form = AdForm()
            # Devolvemos un mensaje de OK
            messages.success(request, 'Anuncio creado correctamente')
    else:
        # si no es post, tenemos que mostrar un formulario vacío
        form = AdForm()
    context = {'form': form}
    return render(request, 'ads/form.html', context)
