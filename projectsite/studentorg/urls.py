from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import (
    HomePageView,
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Search URL (if applicable)
    path('search/', views.search_view, name='search'),

    # Home page
    path('', HomePageView.as_view(), name='home'),

    # Organization URLs
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # Login and Logout URLs
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Organization member URLs
    path('orgMember_list/', OrgMemberList.as_view(), name='orgMem_list'),
    path('orgMember_list/add/', OrgMemberCreateView.as_view(), name='orgMem-add'),
    path('orgMember_list/<int:pk>/', OrgMemberUpdateView.as_view(), name='orgMem-update'),
    path('orgMember_list/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgMem-delete'),

    # Student list URLs
    path('student_list/', StudentList.as_view(), name='student_list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # College list URLs
    path('college_list/', CollegeList.as_view(), name='college_list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<int:pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Program list URLs
    path('program_list/', ProgramList.as_view(), name='program_list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]
