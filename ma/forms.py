from django import forms
from .models import maths_upload_module_1
from .models import maths_upload_module_2
from .models import maths_upload_module_3
from .models import maths_upload_module_4
from .models import maths_upload_module_5
from .models import maths_upload_module_6

class FileFormMathsModule1(forms.ModelForm):
	class Meta:
		model = maths_upload_module_1
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormMathsModule2(forms.ModelForm):
	class Meta:
		model = maths_upload_module_2
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormMathsModule3(forms.ModelForm):
	class Meta:
		model = maths_upload_module_3
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormMathsModule4(forms.ModelForm):
	class Meta:
		model = maths_upload_module_4
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormMathsModule5(forms.ModelForm):
	class Meta:
		model = maths_upload_module_5
		fields = ('Title', 'Module', 'File', 'Description', 'Email')

class FileFormMathsModule6(forms.ModelForm):
	class Meta:
		model = maths_upload_module_6
		fields = ('Title', 'Module', 'File', 'Description', 'Email')
