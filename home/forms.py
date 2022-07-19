from django.forms import ModelForm

from .models import Account


class CustomerForm(ModelForm):
	class Meta:
		model = Account
		fields = '__all__'
		exclude = ['user']