from django.forms import ModelForm
from .models import raw_data_caltalog


class SearchForm(ModelForm):
	class Meta:
		model = raw_data_caltalog
		fields = {'id', 'source'}