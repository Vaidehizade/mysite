from django import forms
# from .models import YourCustomUser


class CreateListForm(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)


# class SignUpForm(UserCreationForm):

#    class Meta:
#       model = YourCustomUser #this is the "YourCustomUser" that you imported at the top of the file  
#       fields = ('username', 'password1', 'password2') #etc etc, other fields you want displayed on the form)