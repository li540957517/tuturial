import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set_cookie(request):
    """写入Cookie"""
    rsp = HttpResponse('写入Cookie')
    rsp.set_cookie('came', '1', max_age=600)
    rsp.set_cookie('language', value='zh-CN', expires=datetime.datetime(2017, 10, 1, 0, 0))
    return rsp


def get_cookie(request):
    """Cookie读取"""
    lang = request.COOKIES.get('language', 'en-US')
    if 'came' in request.COOKIES:
        return HttpResponse(f'欢迎再次访问我们的网站!您设置的语言是:{lang}')
    return HttpResponse(f'欢迎第一次访问我们的网站！您设置的语言是:{lang}')


def delete_cookie(request):
    """删除Cookie"""
    if 'language' in request.COOKIES:
        rsp = HttpResponse()
        rsp.delete_cookie('language')
        return rsp


def set_session(request):
    """设置Session"""
    request.session['course'] = 'Python Django'
    request.session.set_expiry(0)  # 单位为秒，如果为0表示和浏览器生命周期相同
    return HttpResponse('写入Session["course"]')


def get_session(request):
    """读取Session"""
    course = request.session.get('course', None)
    return HttpResponse(course if course else '未找到')


def clear_session(request):
    """删除Session"""
    request.session.flush()
    return HttpResponse('Session清除完毕！')
