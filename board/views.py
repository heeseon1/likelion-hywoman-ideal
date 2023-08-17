from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Post, Comment, Message, alarm_push
from .forms import PostForm, CommentForm, MessageForm
from django.views import View
from django.contrib.auth.models import User
from .models import VolunteerProfile
from .forms import VolunteerProfileForm



###Post

# 게시글 등록하기
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
            return redirect("board:community")

        context = {
            'form': form
        }

        return render(request, "board/post_register.html", context)


# 게시글 전체 보기
class community(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
            "title": "Board"
        }
        return render(request, "board/community.html", context)


# 게시글 상세보기
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


# 게시글 수정하기
class post_update(LoginRequiredMixin, UpdateView):
    model = Post  # 수정할 게시글의 모델을 명시적으로 지정
    form_class = PostForm
    template_name = "board/post_register.html"  # post_register.html을 재활용
    context_object_name = "form"
    def get_success_url(self):
        return reverse_lazy("board:post_detail", kwargs={"pk": self.object.pk})



#게시글 삭제하기
class post_delete(LoginRequiredMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'board/post_delete.html'
    def get_object(self):
        object = get_object_or_404(Post, id=self.kwargs['pk'])
        return object
    def get_success_url(self):
        return reverse_lazy("board:community")



###Comment
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        author = request.user

        if form.is_valid():
            content = form.cleaned_data['content']

            if isinstance(request.user, User):
                author = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, author=author)

                if author.category == False:
                    #if isinstance(post.author, User):
                    sender_username = author
                    alarm = alarm_push.objects.create(
                        user=post.author,
                        sender=sender_username,
                        post=post,
                        content=f'{sender_username}님의 댓글: {comment.content}'
                    )

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

#알림 보여주기
def alarm_list(request):
    alarms = alarm_push.objects.all()
    return render(request, 'board/alarm.html', {'alarms': alarms})

##댓글 수정하기
class CommentUpdate(View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(instance=comment)
        return render(request, 'board/comment_update.html', {'form': form, 'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('board:post_detail', pk=comment.post.pk)  # 이동할 URL 지정
        return render(request, 'board/comment_update.html', {'form': form, 'comment': comment})

class CommentDelete(View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        return render(request, 'board/confirm_comment_delete.html', {'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        post_pk = comment.post.pk
        comment.delete()
        return redirect('board:post_detail', pk=post_pk)


##매칭 화면
def matching_view(request):
    return render(request, 'board/matching.html')

def matching_view2(request):
    return render(request, 'board/matching2.html')

#봉사자 프로필 등록
class RegisterVolunteerProfileView(View):
    def get(self, request):
        form = VolunteerProfileForm()
        context = {
            "user": request.user,
            "form": form
        }
        return render(request, 'board/register_volunteer.html', context)

    def post(self,request):
        form = VolunteerProfileForm(request.POST)
        if form.is_valid():
            volunteerProfile = form.save(commit=False)
            volunteerProfile.user = request.user
            volunteerProfile.save()
            return redirect("board:volunteer_list")
        else:
            print(form.errors)

        context = {
            "user": request.user,
            'form':form
        }
        return render(request, "board/register_volunteer.html", context)

# 봉사자 프로필 보기
class VolunteerProfileView(View):
    def get(self, request, pk):
        profile = get_object_or_404(VolunteerProfile, pk=pk)
        user = profile.user
        return render(request, 'board/volunteer_profile.html', {'profile': profile, 'user': user})

#봉사자 목록 보기
def volunteer_list(request):
    profiles = VolunteerProfile.objects.all()
    return render(request, 'board/volunteer_list.html', {'profiles': profiles})

#봉사자 리뷰보기
class VolunteerReviews(View):
    def volunteer_reviews(request, volunteer_id):
        volunteer = get_object_or_404(VolunteerProfile, id=volunteer_id)
        reviews = Review.objects.filter(volunteer=volunteer.user)

        context = {
            'volunteer': volunteer,
            'reviews': reviews,
        }
        return render(request, 'board/volunteer_reviews.html', context)

#신고기능
def given_warning(request, pk):
    post = get_object_or_404(Post, pk=pk)
    reported_user = post.author

    if request.method == 'POST':
        reported_user.warning += 1
        reported_user.save()

        if reported_user.warning >= 5:
            reported_user.is_active = False
            reported_user.save()

        return redirect('board:community')

    return render(request, 'board/post_detail.html')


#메시지#
# class SendMessageView(LoginRequiredMixin, View):
#     template_name = 'board/send_message.html'
#
#     def get(self, request, recipient_id):
#         recipient = get_object_or_404(User, id=recipient_id)
#         form = MessageForm()
#         context = {
#             'recipient': recipient,
#             'form': form,
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request, recipient_id):
#         recipient = get_object_or_404(User, id=recipient_id)
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.recipient = recipient
#             message.save()
#             messages.success(request, 'Message sent successfully!')
#             return redirect('messages:inbox')
#         context = {
#             'recipient': recipient,
#             'form': form,
#         }
#         return render(request, self.template_name, context)
#
# class InboxView(LoginRequiredMixin, View):
#     template_name = 'board/inbox.html'
#
#     def get(self, request):
#         received_messages = Message.objects.filter(recipient=request.user)
#         context = {
#             'received_messages': received_messages,
#         }
#         return render(request, self.template_name, context)
