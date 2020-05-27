from django import forms
from .models import coa_upload_module_1
from .models import coa_upload_module_2
from .models import coa_upload_module_3
from .models import coa_upload_module_4
from .models import coa_upload_module_5
from .models import coa_upload_module_6

class FileFormCoaModule1(forms.ModelForm):
	class Meta:
		model = coa_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormCoaModule2(forms.ModelForm):
	class Meta:
		model = coa_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormCoaModule3(forms.ModelForm):
	class Meta:
		model = coa_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormCoaModule4(forms.ModelForm):
	class Meta:
		model = coa_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormCoaModule5(forms.ModelForm):
	class Meta:
		model = coa_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormCoaModule6(forms.ModelForm):
	class Meta:
		model = coa_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
