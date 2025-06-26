from django import forms

class NumberForm(forms.Form):
    a = forms.IntegerField(label='Enter first number', min_value=0)
    b = forms.IntegerField(label='Enter second number', min_value=0)
    c = forms.IntegerField(label='Enter third number', min_value=0)
    d = forms.IntegerField(label='Enter fourth number', min_value=0)
    e = forms.IntegerField(label='Enter fifth number', min_value=0)


#DEV# 