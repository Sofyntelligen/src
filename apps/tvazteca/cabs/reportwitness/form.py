from django import forms


class ReportWitness(forms.Form):
    list_type_report = forms.Select()
    list_sub_report = forms.Select()
    list_action_report = forms.Select()
    radios1 = forms.BooleanField()
    radios2 = forms.BooleanField()
    radios3 = forms.BooleanField()
    radios4 = forms.BooleanField()
    commentArea = forms.CharField()
