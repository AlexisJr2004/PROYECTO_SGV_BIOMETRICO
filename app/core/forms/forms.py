from django import forms
from app.core.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone = forms.CharField(max_length=20, required=False)
    dni = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)
    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), required=False)
    address = forms.CharField(max_length=255, required=False)
    gender = forms.ChoiceField(choices=Customer.GENDER_CHOICES, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dni', 'phone', 'email', 'image', 'address', 'gender', 'date_of_birth', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['phone'].initial = self.instance.phone
            self.fields['dni'].initial = self.instance.dni
            self.fields['address'].initial = self.instance.address
            self.fields['gender'].initial = self.instance.gender
            self.fields['date_of_birth'].initial = self.instance.date_of_birth
            self.fields['latitude'].initial = self.instance.latitude
            self.fields['longitude'].initial = self.instance.longitude