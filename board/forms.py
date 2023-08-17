from django import forms
from .models import Post, Comment, Message
from .models import VolunteerProfile, TimeSlot
from .models import AvailableDate
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows' : '3', 'cols' : '30'})
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': '3', 'cols': '30'})
        }

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time']

TimeSlotFormset = forms.inlineformset_factory(
    AvailableDate,
    TimeSlot,
    form=TimeSlotForm,
    extra=1,
    can_delete=False,
)

class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ['name', 'content', 'level']

class AvailableDateForm(forms.ModelForm):
    class Meta:
        model = AvailableDate
        fields = ['date', 'time_slots']