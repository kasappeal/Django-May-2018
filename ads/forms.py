from django.forms import ModelForm

from ads.models import Ad


class AdForm(ModelForm):

    class Meta:
        model = Ad
        fields = '__all__'
        exclude = ['owner', 'status']
