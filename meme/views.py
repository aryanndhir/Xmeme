from django.shortcuts import render
from .models import Post
from django import forms
import requests
from django.contrib import messages
import datetime


# This class creates a form object to upload a meme
class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', "caption", "url"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'txtbox',
                'placeholder': 'Enter your full name'}),
            'caption': forms.TextInput(attrs={
                'class': 'txtbox',
                'placeholder': 'Be creative with the caption'}),
            'url': forms.URLInput(attrs={
                'class': 'txtbox',
                'placeholder': 'Enter URL of your meme here'})
        }

    # This function is used for its validation
    def clean(self):

        super(postform, self).clean()

        name = self.cleaned_data.get('name')
        caption = self.cleaned_data.get('caption')
        url = self.cleaned_data.get('url')
        post = Post.objects.filter(name=name, caption=caption, url=url).count()

        if post > 0:
            self._errors["name"] = self.error_class([''])

        return self.cleaned_data


# This class creates a form object to edit a meme
class editform(forms.ModelForm):
    class Meta:
        btn = forms.CharField()
        model = Post
        fields = ["id", "caption", "url"]
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'txtbox',
                'placeholder': 'Be more creative with the caption'}),
            'url': forms.URLInput(attrs={
                'class': 'txtbox',
                'placeholder': 'Enter URL of your meme here'})
        }

    # This function is used for its validation
    def clean(self):

        super(editform, self).clean()

        caption = self.cleaned_data.get('caption')
        url = self.cleaned_data.get('url')
        post = Post.objects.filter(caption=caption, url=url).count()

        if post > 0:
            self._errors['name2'] = self.error_class([''])

        return self.cleaned_data


# This function is called to create form objects,
# call REST APi and then render the html page
def home(request):
    result = {}

    if request.method == "POST":

        if 'name' not in request.POST:
            form = postform()
            form2 = editform(request.POST)
            if form2.is_valid():
                id = request.POST['id']
                response = requests.patch(
                    f'http://localhost:8081/memes/{id}',
                    data=request.POST)
            else:
                messages.info(
                    request, 'You have already posted this exact same meme')
        else:
            form = postform(request.POST)
            form2 = editform()
            if form.is_valid():
                response = requests.post(
                    'http://localhost:8081/memes',
                    data=request.POST)
            else:
                messages.info(
                    request, 'You have already posted this exact same meme')

    form = postform()
    form2 = editform()

    response = requests.get('http://localhost:8081/memes')
    result = response.json()

    for i in result:
        x = i["date_posted"]
        ans = datetime.datetime(int(x[0:4]), int(x[5:7]), int(x[8:10]), int(x[11:13]), int(x[14:16]))
        i["date_posted"] = ans.strftime("%b %d %Y %H:%M")

    context = {
        'posts': result,
        'form': form,
        'form2': form2
    }
    return render(request, 'meme/home.html', context)
