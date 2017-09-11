from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import reverse
from django.template import Template, Context


# Create your views here.
def home(request):
    return HttpResponse('你好呀')


def rsp_attr(request):
    """手动构造响应"""
    rsp = HttpResponse(content='Django', content_type='text/plain', charset='utf-8')
    rsp.content = 'WEB'
    rsp.write('网站开发')
    rsp.writelines(['aaa', 'bbb', 'ccc'])
    rsp.flush()
    return rsp


def rsp_redirect(request):
    """响应转跳"""
    rsp = HttpResponseRedirect(reverse('learn:home'))
    return rsp


def rsp_json(request):
    """响应json"""
    import datetime
    emp = {'name': 'Cyril', 'age': 20, 'birthdate': datetime.date(1993, 3, 3)}
    rsp = JsonResponse(emp)
    return rsp


def rsp_header(request):
    """自定义 响应头部"""
    rsp = HttpResponse('自定义头部信息')
    rsp['Age'] = 20
    # del rsp['Age']
    return rsp


def rsp_download(request):
    """作为附件下载"""
    f = open('static/data.txt', 'r', encoding='utf8')
    rsp = HttpResponse(content=f, content_type='application/force-download')
    rsp['content-Disposition'] = 'attachment;filename = readme.txt'
    return rsp


def tmp_loading(request):
    """载入模板"""
    # template = Template('当前课程是：{{course_title}}')
    # context = Context({'course_title': 'django web 开发'})
    # return HttpResponse(template.render(context), request)
    from django.template import loader
    # template = loader.get_template('tmp-1.html')
    # template = loader.select_template(['tmp-1.html', ])
    # context = Context({'course_title': 'django web 开发'})
    # return HttpResponse(template.render(context, request))
    return HttpResponse(loader.render_to_string('tmp-1.html', {'course_title': 'Python Django'}, request))


def tem_render(request):
    """快捷方式 呈现模板及上下文数据"""
    return render(request, 'tmp-1.html', {'course_title': 'Web 全栈开发'})


def tmp_article(request):
    return render(request, 'article.html')


def dtl_syntax(request):
    """django Template Language 语法"""
    import datetime
    context = {
        'title': 'Python Django',
        'course': {'title': 'Django 教程', 'price': 59, 'pubdate': datetime.date.today()},
        'students': ['Tom', 'Jerry', 'Mike', ]
    }
    return render(request, 'learn/dtl-syntax.html', context)


def dtl_tags(request):
    """标签"""
    import datetime
    context = {
        'input': '<input type = "text">',
        'title': 'Python Django',
        'course': {'title': 'Django 教程', 'price': 59, 'pubdate': datetime.date.today()},
        'students': ['Tom', 'Jerry', 'Mike', 'Jhon', 'Petter', ]
    }
    return render(request, 'learn/dtl-tags.html', context)


def dtl_filter(request):
    """过滤器 修改变量显示"""
    import datetime
    context = {
        'input': '<input type = "text">',
        'title': 'Python Django',
        'course': {'title': 'django 教程', 'price': 59, 'pubdate': datetime.datetime.now()},
        'students': ['Tom', 'Jerry', 'Mike', 'Jhon', 'Petter', ],
        'var1': True,
        'var2': False,
        'var3': None,
        'lorem': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis corporis distinctio dolores doloribus, eaque facilis fugiat incidunt minus necessitatibus nemo nobis provident quia, quos sapiente sunt, ullam velit. Repudiandae, sit!',
        'lorem_html': '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis corporis distinctio dolores doloribus, eaque facilis fugiat incidunt minus necessitatibus nemo nobis provident quia, quos sapiente sunt, ullam velit. Repudiandae, sit!</p>',
    }
    return render(request, 'learn/dtl-filter.html', context)


def dtl_tmp_inheritance(request):
    """模板继承与扩展"""
    return render(request, 'sub-1.html')


def dtl_tmp_inheritance2(request):
    return render(request,'sub-2.html')
