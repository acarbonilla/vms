from django.forms import ModelForm

from core.models import Department


class DeptForm (ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DeptFormEdit(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

