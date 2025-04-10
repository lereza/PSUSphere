from django.forms import ModelForm
from django import forms
from .models import Organization, Student, OrgMember, College, Program

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class  OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"

class   StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"

# Search Form for Full Name and Date
class SearchForm(forms.Form):
    fullname = forms.CharField(max_length=100, required=False, label='Full Name')
    start_date = forms.DateField(widget=forms.SelectDateWidget(), required=False, label='Start Date')
    end_date = forms.DateField(widget=forms.SelectDateWidget(), required=False, label='End Date')