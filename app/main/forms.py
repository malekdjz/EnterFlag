from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=150,required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',max_length=150,required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    Email = forms.EmailField(required=True)

class ConfirmEmailForm(forms.Form):
    code = forms.CharField(required=True)

class TeamForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20,required=True)

class InviteTeammateForm(forms.Form):
    username = forms.CharField(label='username',max_length=150,required=True)

class KickTeammateForm(forms.Form):
    member = forms.ChoiceField(required=True)

class TransferOwnershipForm(forms.Form):
    member = forms.ChoiceField(required=True)
    
class SubmitChallangeForm(forms.Form):
    flag = forms.CharField(label='Flag',max_length=50,required=True)

class ChallangeForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20,required=True)
    link = forms.URLField(label='Link',required=True)
    description = forms.CharField(label='description',widget=forms.Textarea)
    dificulty = forms.CharField(label='Dificulty',required=True,max_length=20)
    category = forms.ChoiceField(label='Category',required=True)
    points = forms.IntegerField(required=True)
    flag = forms.CharField(label='Flag',required=True,max_length=50)
    event = forms.ChoiceField(label='Event',required=True)





