from django.shortcuts import render, redirect

#imports model to pass to html page
from .models import Video

#for vrform function
from .forms import VideoForm
# Create your views here.

def index(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    if request.method == 'POST':
        form = VideoForm(request.POST) #DOES NOT PROTECT AGAINST SQL INJECTION

        if form.is_valid():
            new_req = Video(videotitle=request.POST['videoname'],
            videodesc=request.POST['videodesc'])
            new_req.save() #save the POST
            return redirect('index') #redirects back to homepage
    else:
        form = VideoForm()

    context= {'form': form}

    return render(request, 'videorequest/vrform.html', context)
