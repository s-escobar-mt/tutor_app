from django.urls import path

from .views import HomePageView, TutorDetailView, ScheduleCreateView, SubjectUpdateView,ScheduleUpdateView, AddSubjectView, RemoveSubjectView, RemoveScheduleView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("tutor_detail/<int:pk>", TutorDetailView.as_view(), name="tutor_detail"),
    path('add-schedule/', ScheduleCreateView.as_view(), name='add_schedule'),
    path('edit-schedule/<int:pk>/', ScheduleUpdateView.as_view(), name='edit_schedule'),  # For editing schedule
    path('edit-subject/<int:pk>/', SubjectUpdateView.as_view(), name='edit_subject'),  # For editing subject
    path('add-subject/', AddSubjectView.as_view(), name='add_subject'),
    path('remove-subject/<int:subject_id>/', RemoveSubjectView.as_view(), name='remove_subject'), 
    path('remove-schedule/<int:schedule_id>/', RemoveScheduleView.as_view(), name='remove_schedule'),  # New URL pattern
]
