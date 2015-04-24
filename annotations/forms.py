from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Annotation

class AnnotationForm(ModelForm):
#class AnnotationForm(NgModelFormMixin, NgModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnotationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['start_time'].widget.attrs.update({'data-ng-model': 'item.start_time'})
        self.fields['end_time'].widget.attrs.update({'data-ng-model': 'item.end_time'})
        self.fields['text'].widget.attrs.update({'data-ng-model': 'item.text'})

    class Meta:
        model = Annotation
        fields = ['start_time', 'end_time', 'text']