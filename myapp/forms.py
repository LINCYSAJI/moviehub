from django import forms

from myapp.models import Movie

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-warning"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))
    
    
class MovieModelForm(forms.ModelForm):
    
    class Meta:
        
        model=Movie
        
        # fields=["title","year","director","run_time","language","genre","producer"]
        
        exclude=("id",)
        
        widgets={
        
            "title":forms.TextInput(attrs={"class":"form-control"}),

            "year":forms.TextInput(attrs={"class":"form-control"}),
        
            "director":forms.TextInput(attrs={"class":"form-control"}),
        
            "run_time":forms.NumberInput(attrs={"class":"form-control"}),
            
            "language":forms.TextInput(attrs={"class":"form-control"}),
            
            "genre":forms.TextInput(attrs={"class":"form-control"}),

            "producer":forms.TextInput(attrs={"class":"form-control"})

        }