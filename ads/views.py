from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from ads.forms import AdForm
from ads.models import Ad


class HomeView(ListView):

    model = Ad
    template_name = 'ads/list.html'

    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(status=Ad.PENDING).order_by('-created_on')[:5]


class AdDetailView(View):

    def get(self, request, pk):
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


@method_decorator(login_required, name='dispatch')
class AdFormView(View):

    def get(self, request):
        """
        Muestra el formulario para crear un anuncio
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """
        form = AdForm()
        context = {'form': form}
        return render(request, 'ads/form.html', context)

    def post(self, request):
        """
        Procesa el formulario para crear un anuncio
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """
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
        context = {'form': form}
        return render(request, 'ads/form.html', context)
