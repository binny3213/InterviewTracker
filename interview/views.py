from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Interview
from .forms import InterviewForm,SignUpForm
from django.db.models.functions import ExtractMonth
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy

# Sign up form

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('interview:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



#about the web app- short explenation
class AboutView(TemplateView):
    template_name = 'interview/about.html'
 
 #interview delete option - confirm if really want   
class InterviewDeleteView(DeleteView):
    model = Interview
    template_name = 'interview/interview_confirm_delete.html'
    success_url = reverse_lazy('interview:home')

    def get_queryset(self):
        return Interview.objects.filter(user=self.request.user)

#interviews list - all the interviews of a user
@login_required
def interview_list(request):
    interviews = Interview.objects.filter(user=request.user).order_by('-date')
    interview_count = interviews.count()
    return render(request,'interview/interview_list.html',
                  {'interviews':interviews,
                    'interview_count':interview_count})
    
#home view - graphs and interview_counter, add,update buttons
@login_required
def home(request):
    interviews = Interview.objects.filter(user=request.user).order_by('date')
    interview_count = interviews.count()
    return render(request, 'interview/home.html', {
        'interview_count': interview_count,
        'interviews': interviews,      
    })

#add new interview
@login_required
def create_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.user = request.user
            interview.save()
            return redirect('interview:home')
    else:
        form = InterviewForm()
    return render(request, 'interview/interview_form.html',{'form':form})

# interview detail - all the fields related to the specific interview
@login_required
def interview_detail(request, pk):
    interview = get_object_or_404(Interview, pk=pk, user=request.user)
    return render(request, 'interview/interview_detail.html', {'interview': interview})

# update certain interview
@login_required
def update_interview(request,pk):
    interview = get_object_or_404(Interview,pk=pk,user=request.user)
    if request.method == 'POST':
        form = InterviewForm(request.POST,instance = interview)
        if form.is_valid():
            form.save()
            return redirect('interview:home')
    else:
        form = InterviewForm(instance=interview)
    return render(request, 'interview/interview_form.html', {'form': form, 'interview': interview})   


    