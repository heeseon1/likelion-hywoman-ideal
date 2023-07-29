from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# 게시글 등록하기
def post_register(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_register.html', {'form': form})


# 게시글 전체 보기
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts': posts})

# 게시글 상세보기
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'board/post_detail.html', {'post': post})

