from django import forms
from .models import eco_upload_module_1
from .models import eco_upload_module_2
from .models import eco_upload_module_3
from .models import eco_upload_module_4
from .models import eco_upload_module_5
from .models import eco_upload_module_6

class FileFormEcoModule1(forms.ModelForm):
	class Meta:
		model = eco_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormEcoModule2(forms.ModelForm):
	class Meta:
		model = eco_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormEcoModule3(forms.ModelForm):
	class Meta:
		model = eco_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormEcoModule4(forms.ModelForm):
	class Meta:
		model = eco_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormEcoModule5(forms.ModelForm):
	class Meta:
		model = eco_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormEcoModule6(forms.ModelForm):
	class Meta:
		model = eco_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
