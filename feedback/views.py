from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback
from .forms import FeedbackForm


# Create your views here.
def home(request):
    context = {
        'categories': Feedback.CATEGORIES
    }
    if request.method == 'POST':
        f = Feedback()
        f.subject = request.POST.get('subject', '')
        f.category = request.POST.get('category', '')
        f.username = request.POST.get('username', '')
        f.email = request.POST.get('email', '')
        f.screenshot = ''
        f.description = request.POST.get('description', '')
        f.subscription = 'subscription' in request.POST
        f.status = '待处理'
        f.save()
        return HttpResponse('问题提交成功')
    return render(request, 'feedback/feedback.html', context)


def feedback_form(request):
    form = FeedbackForm(initial={'subject': '反馈问题标题'})
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            # data = dict(form.cleaned_data)
            # feedback = Feedback(**form.cleaned_data)
            # feedback.status = '待处理'
            # feedback.save()
            if request.FILES['screenshot']:
                upload_file(request.FILES['screenshot'])
            return redirect('/')
    return render(request, 'feedback/feedback-form.html', {'form': form})


def get_feedback_data(request):
    if request.method == 'GET':
        data = dict(request.GET)
        return HttpResponse(str(data))


def upload_file(f):
    with open('uploads\{}'.format(f.name), 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
