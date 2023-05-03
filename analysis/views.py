from django.shortcuts import redirect, render
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from analysis.forms import TwittertextForm
from analysis.prediction import textclean

# Create your views here.


def dematlogin(request):    
    if request.method == "POST":
        form = TwittertextForm(request.POST)
        files = request.POST
        
        if form.is_valid():
            da = form.cleaned_data
            tweet = da['text']
            result = textclean(tweet)
            
            context = {
                    'resumes': result,
                }
            return render(request, 'base.html', context)
    else:
        form = TwittertextForm()
    return render(request, 'base.html', {'form': form})


