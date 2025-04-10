from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

# Base Search ListView
class SearchListView(ListView):
    search_fields = []
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = super().get_queryset()
        if query:
            filters = Q()
            for field in self.search_fields:
                filters |= Q(**{f"{field}__icontains": query})
            qs = qs.filter(filters)
        return qs

# HomePageView (No Changes needed)
@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.all()
        context['students'] = Student.objects.all()
        context['orgMember'] = OrgMember.objects.all()
        context['colleges'] = College.objects.all()
        context['programs'] = Program.objects.all()
        return context

# Organization Views

class OrganizationList(SearchListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'org_list.html'
    paginate_by = 5
    search_fields = ['name', 'description']

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# Organization Member Views

class OrgMemberList(SearchListView):
    model = OrgMember
    context_object_name = 'orgMember'
    template_name = 'orgMem_list.html'
    paginate_by = 5
    search_fields = ['student__firstname', 'student__lastname', 'organization__name', 'organization__description']

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgMem_add.html'
    success_url = reverse_lazy('orgMem_list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgMem_edit.html'
    success_url = reverse_lazy('orgMem_list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgMem_del.html'
    success_url = reverse_lazy('orgMem_list')

# Student Views

class StudentList(SearchListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    paginate_by = 5
    search_fields = ['firstname', 'lastname', 'middlename', 'student_id', 'program__prog_name']

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student_list')

# College Views

class CollegeList(SearchListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college_list.html'
    paginate_by = 5
    search_fields = ['college_name']

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'colleg_add.html'
    success_url = reverse_lazy('college_list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college_list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college_list')

# Program Views

class ProgramList(SearchListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'program_list.html'
    paginate_by = 5
    search_fields = ['college__college_name', 'prog_name']

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program_list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program_list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program_list')
