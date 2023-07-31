from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.views.generic import View, UpdateView
from .models import Post, Comment
from .forms import PostForm, CommentForm


###Post


# class Delete(View):
#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         post.delete()
#         return redirect('blog:list')
# 게시글 등록하기


# def post_register(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'board/post_register.html', {'form': form})

class post_register(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            "form": form,
            "title": "Board"
        }
        return render(request, "board/post_register.html", context)

    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("board:post_list")

        context = {
            'form': form
        }

        return render(request, "board/post_register.htm", context)


# 게시글 전체 보기
class post_list(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
            "title": "Board"
        }
        return render(request, "board/post_list.html", context)

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'board/post_list.html', {'posts': posts})

# 게시글 상세보기
# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     return render(request, 'board/post_detail.html', {'post': post})


class post_detail(View):

    def get(self, request, pk):
        post = Post.objects.prefetch_related('comment_set').get(pk=pk)
        comments = post.comment_set.all()
        comment_form = CommentForm()

        context = {
            "title": "Board",
            "post_id": pk,
            "post_title": post.title,
            "post_author": post.author,
            "post_contents": post.contents,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, 'board/post_detail.html', context)



###Comment
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            author = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, author=author)
            except ObjectDoesNotExist as e:
                print('게시물이 존재하지 않습니다.', str(e))
            except ValidationError as e:
                print('오류가 발생했습니다.', str(e))
            return redirect('board:post_detail', pk=pk)

        context = {
            'title': 'Board',
            'post_id': pk,
            'comment': post.comment_set.all(),
            'comment_form': form
        }
        return render(request, 'board/post_detail.html', context)


class CommentDelete(View):
    def post(self, request, pk):
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, pk=pk)
            post_id = comment.post.id
            if comment.author == request.user:
                comment.delete()
                return redirect(comment.post.get_absolute_url())
            else:
                return HttpResponse('You are not allowed to delete this comment')
        return redirect('board/post_detail.html')



