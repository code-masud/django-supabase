from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title',  'file']

    def clean_file(self):
        file = self.cleaned_data['file']


        ext = file.name.split(".")[-1].lower()
        allowed_extension = ['pdf', 'doc', 'docx', 'txt']

        if ext not in allowed_extension:
            raise forms.ValidationError(
                f'Only {", ".join(allowed_extension)} files are allowed'
            )
        
        if file.size > (2 * 1024 * 1024):
            raise forms.ValidationError(
                f'File size must be under 2MB'
            )
        
        return file