from django.http import JsonResponse


def blog_post_list_api(request):
    blog_posts = BlogPost.objects.all()
    data = []
    for blog_post in blog_posts:
        data.append({
            'id': blog_post.id,
            'title': blog_post.title,
            'content': blog_post.content,
            'author': blog_post.author.username,
            'publication_date': blog_post.publication_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse(data, safe=False)


def blog_post_detail_api(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    data = {
        'id': blog_post.id,
        'title': blog_post.title,
        'content': blog_post.content,
        'author': blog_post.author.username,
        'publication_date': blog_post.publication_date.strftime('%Y-%m-%d %H:%M:%S')
    }
    return JsonResponse(data)


def blog_post_create_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        blog_post = BlogPost.objects.create(
            title=data['title'],
            content=data['content'],
            author=request.user
        )
        return JsonResponse({
            'id': blog_post.id,
            'title': blog_post.title,
            'content': blog_post.content,
            'author': blog_post.author.username,
            'publication_date': blog_post.publication_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'error': 'POST request required'}, status=400)


def blog_post_update_api(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'PUT':
        data = json.loads(request.body)
        blog_post.title = data['title']
        blog_post.content = data['content']
        blog_post.save()
        return JsonResponse({
            'id': blog_post.id,
            'title': blog_post.title,
            'content': blog_post.content,
            'author': blog_post.author.username,
            'publication_date': blog_post.publication_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'error': 'PUT request required'}, status=400)


def blog_post_delete_api(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'DELETE':
        blog_post.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'DELETE request required'}, status=400)