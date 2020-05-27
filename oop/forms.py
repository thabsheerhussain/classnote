from django import forms
from .models import oop_upload_module_1
from .models import oop_upload_module_2
from .models import oop_upload_module_3
from .models import oop_upload_module_4
from .models import oop_upload_module_5
from .models import oop_upload_module_6

class FileFormOopModule1(forms.ModelForm):
	class Meta:
		model = oop_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOopModule2(forms.ModelForm):
	class Meta:
		model = oop_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOopModule3(forms.ModelForm):
	class Meta:
		model = oop_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOopModule4(forms.ModelForm):
	class Meta:
		model = oop_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOopModule5(forms.ModelForm):
	class Meta:
		model = oop_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormOopModule6(forms.ModelForm):
	class Meta:
		model = oop_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
