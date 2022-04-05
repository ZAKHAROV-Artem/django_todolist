from django import forms
from django.views.generic.edit import UpdateView
from .models import Tasks

class CreateForm(forms.ModelForm):
    class Meta:
        model = Tasks

        fields = ['title', 'content', 'is_finished', 'serious_category']
        widgets = {
            'title':forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'content':forms.Textarea(
                attrs={'class':'form-control'}
            ),
            'is_finished':forms.CheckboxInput(
                attrs={'class':'form-check-input'}
            ),
            'serious_category':forms.Select(
                attrs={'class':'form-control'}
            )
        }

# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = Tasks

#         fields = ['title', 'content', 'is_finished', 'serious_category']
#         widgets = {
#             'title':forms.TextInput(
#                 attrs={'class':'form-control'}
#             ),
#             'content':forms.Textarea(
#                 attrs={'class':'form-control'}
#             ),
#             'is_finished':forms.CheckboxInput(
#                 attrs={'class':'form-check-input'}
#             ),
#             'serious_category':forms.Select(
#                 attrs={'class':'form-control'}
#             )
#         }