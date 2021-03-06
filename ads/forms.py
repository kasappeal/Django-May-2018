from django.core.exceptions import ValidationError
from django.forms import ModelForm

from ads.models import Ad


class AdForm(ModelForm):

    class Meta:
        model = Ad
        fields = '__all__'
        exclude = ['owner', 'status']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is not None and 'image' not in image.content_type:
            raise ValidationError('El archivo no es una imagen válida')
        return image

    def clean(self):
        super().clean()  # al llamar al método clean de la superclase garantizamos la validacion de los campos del modelo
        send_choice = self.cleaned_data.get('send_choice', False)
        type = self.cleaned_data.get('type')
        if type == Ad.BUY and send_choice:
            raise ValidationError('Los anuncios de compra no pueden llevar envío.')
