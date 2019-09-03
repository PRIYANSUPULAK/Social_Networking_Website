from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Name of the class must not match UserCreationForm
class UserCreateForm(UserCreateForm):

    class Meta:
        #fields of the model we want to use in the form
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'
