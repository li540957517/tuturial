from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.response import TemplateResponse
from django.template import loader


# Create your views here.
def home(request):
    return render(request, 'hello/home.html')


def course_year(request, year):
    return HttpResponse('课程:{}'.format(year))


def course_year_month(request, year, month):
    return HttpResponse(f'课程：{year}-{month}')


def view_redirect(request):
    return redirect(reverse('hello:hello-course_year_month', args=('2016', '05')))


def view_contact(request):
    html = '<html><body><h1>联系我们</h1></body></html>'
    return HttpResponse(html)


# 返回错误
def product_info(request, pid):
    pid = int(pid)
    if pid <= 10:
        return HttpResponse(f'产品详情{pid}')
    else:
        return HttpResponseNotFound(f'未找到匹配的信息{pid}')
        # raise Http404('该产品不存在')


# 视图呈现模板
def help_center(request):
    context = {
        'title': 'Django 实战',
    }
    return render(request, 'hello/help.html', context)
    # template = loader.get_template('hello/help.html')
    # return HttpResponse(template.render(context,request))
    # return TemplateResponse(request,'hello/help.html',context)


# 获取请求相关信息
def request_info(request):
    context = {
        'data': {
            'scheme': request.scheme,
            'path': request.path,
            'method': request.method,
            'encoding': request.encoding,
            'content_type': request.content_type,
            'querystring_name': request.GET['name'],
            'querystring_id': request.GET['id'],
            'host': request.get_host(),
            'port': request.get_port(),
            'full_path': request.get_full_path(),
            'is_ajax': request.is_ajax(),
            'IP': request.META.get('REMOTE_ADDR'),
            'User-Agent': request.META.get('HTTP_USER_AGENT'),
            'Meta': request.META,
        }
    }
    return render(request, 'hello/request.html', context)
