from django.shortcuts import render, redirect, get_object_or_404, reverse
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


def feedback_list(request):
    """信息列表页"""
    q = request.GET.get('q', '')
    items = Feedback.objects.all().filter(subject__contains=q).order_by('-posted_time')
    return render(request, 'feedback/feedback-list.html', {'items': items})


def feedback_detail(request, fid):
    """信息详情展示页"""
    # feedback = Feedback.objects.get(pk=fid)
    feedback = get_object_or_404(Feedback, pk=fid)
    return render(request, 'feedback/feedback-detail.html', {'item': feedback})


def feedback_edit(request, fid):
    """编辑特定id信息"""
    fb = get_object_or_404(Feedback, pk=fid)
    form = FeedbackForm(initial={
        'subject': fb.subject,
        'category': fb.category,
        'username': fb.username,
        'email': fb.email,
        'screenshot': fb.screenshot,
        'description': fb.description,
        'subscription': fb.subscription,
        'status': fb.status,
        'posted_time': fb.posted_time,
    })
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            # fb.subject = form.cleaned_data['subject']
            for k, v in form.cleaned_data.items():
                setattr(fb, k, v)
            fb.save()
            return redirect(reverse('feedback:feedback_list'))
    return render(request, 'feedback/feedback-edit.html', {'form': form})


def feedback_delete(request, fid):
    """删除信息"""
    f = get_object_or_404(Feedback, pk=fid)
    f.delete()
    return redirect(reverse('feedback:feedback_list'))
