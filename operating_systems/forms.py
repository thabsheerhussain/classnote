from django import forms
from .models import os_upload_module_1
from .models import os_upload_module_2
from .models import os_upload_module_3
from .models import os_upload_module_4
from .models import os_upload_module_5
from .models import os_upload_module_6

class FileFormOsModule1(forms.ModelForm):
	class Meta:
		model = os_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOsModule2(forms.ModelForm):
	class Meta:
		model = os_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOsModule3(forms.ModelForm):
	class Meta:
		model = os_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOsModule4(forms.ModelForm):
	class Meta:
		model = os_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOsModule5(forms.ModelForm):
	class Meta:
		model = os_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOsModule6(forms.ModelForm):
	class Meta:
		model = os_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
