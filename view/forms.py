from django import forms
from datetime import datetime
from django.conf import settings

class AdvancedEditor(forms.Textarea):
	class Media:
		js = (settings.MEDIA_URL+'/js/tinymce/tiny_mce.js',)

	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'class': 'advancededitor'}
		if attrs: self.attrs.update(attrs)
		super(AdvancedEditor, self).__init__(attrs)

class UploadForm(forms.Form):
   docid =forms.CharField(required=False, label="Document identifier")
   doc = forms.CharField(widget=AdvancedEditor(), label="Document")

class ImportForm(forms.Form):
   docid =forms.CharField(required=False, label="Document identifier")
   url = forms.CharField(label="Document URL")

