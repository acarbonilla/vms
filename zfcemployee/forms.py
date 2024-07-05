from django.contrib.auth.models import User
from django.forms import ModelForm

from core.models import EmpName


class ProfileForm(ModelForm):
    class Meta:
        model = EmpName
        fields = "__all__"

    def __init__(self, user, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = User.objects.filter(id=user.id)
