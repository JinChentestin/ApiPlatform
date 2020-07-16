from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def index(request):
    """
    index视图
    :param request:
    :return:
    """
    if request.method == 'GET':
        return HttpResponse("<h1>GET请求: 你好 中泰</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>POST请求: 你好 中泰</h1>")
    else:
        return HttpResponse("<h1>其他请求: 你好 中泰</h1>")


# 类视图
class IndexView(View):

    def get(self, request):
        return HttpResponse("<h1>GET请求: 你好 中泰</h1>")
        # 这个是返回HTML页面  return render(request, 'demo.html')

    def post(self, request):
        return HttpResponse("<h1>POST请求: 你好 中泰</h1>")

    def put(self, request):
        return HttpResponse("<h1>PUT请求: 你好 中泰</h1>")

    def delete(self, request):
        return HttpResponse("<h1>DEL请求: 你好 中泰</h1>")
