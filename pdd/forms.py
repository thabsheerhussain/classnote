from django import forms
from .models import pdd_upload_module_1
from .models import pdd_upload_module_2
from .models import pdd_upload_module_3
from .models import pdd_upload_module_4
from .models import pdd_upload_module_5
from .models import pdd_upload_module_6

class FileFormPddModule1(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormPddModule2(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormPddModule3(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormPddModule4(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormPddModule5(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormPddModule6(forms.ModelForm):
	class Meta:
		model = pdd_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
