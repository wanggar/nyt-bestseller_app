from django import forms
from .models import BookCollections


class ShareBookForm(forms.Form):
    description = forms.CharField(max_length=1000)

    def cleaned_description(self):
        data = self.cleaned_data['description']
        return data


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1000)


class UpdateReadingStatusForm(forms.ModelForm):
    class Meta:
        model = BookCollections
        fields = ('onPage', 'totalPage')


UpdateReadingStatusFormSet = forms.modelformset_factory(BookCollections, fields=('onPage', 'totalPage'))
