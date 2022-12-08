from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

# request - запрос
# render - предоставление
# response - ответ