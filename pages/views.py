from django.views.generic import DetailView,ListView,CreateView,UpdateView, View
from accounts.models import CustomUser, Schedule, Subject
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import ScheduleForm, SubjectForm, AddSubjectForm
from django.shortcuts import redirect, get_object_or_404, render

class HomePageView(ListView):
    model=CustomUser
    template_name = "home.html"
    def get_queryset(self):
        # Get the Tutor group
        tutor_group = Group.objects.get(name='Tutors')
        # Filter users that are in the Tutor group
        return CustomUser.objects.filter(groups=tutor_group)

class TutorDetailView(DetailView):
    model = CustomUser
    template_name = "tutor_detail.html"
    context_object_name='tutor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_tutor'] = self.request.user == self.object  # Check if the logged-in user is the tutor
        return context

class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'add_schedule.html'
    success_url = reverse_lazy("home")  # Redirect after success

    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.save()  # Save the schedule instance
        self.request.user.schedule.add(schedule)  # Link the schedule to the current user
        return super().form_valid(form)

class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule_form.html'  # Create this template
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Schedule.objects.filter(customuser=self.request.user)
    
class RemoveScheduleView(View):
    def post(self, request, schedule_id):
        schedule = get_object_or_404(Schedule, id=schedule_id)
        request.user.schedule.remove(schedule)  # Remove the schedule from the logged-in user
        return redirect('tutor_detail', pk=request.user.pk)  # Redirect back to tutor detail page
    
class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'  # Create this template
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Subject.objects.filter(customuser=self.request.user)
    
class AddSubjectView(View):
    def get(self, request):
        form = AddSubjectForm()
        return render(request, 'add_subject.html', {'form': form})

    def post(self, request):
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()  # Save the subject to create it first
            request.user.subjects.add(subject)  # Add the subject to the logged-in user
            return redirect('tutor_detail', pk=request.user.pk)  # Redirect back to tutor detail page
        return render(request, 'add_subject.html', {'form': form})

class RemoveSubjectView(View):
    def post(self, request, subject_id):
        subject = get_object_or_404(Subject, id=subject_id)
        request.user.subjects.remove(subject)  # Remove the subject from the logged-in user
        return redirect('tutor_detail', pk=request.user.pk)  # Redirect back to the tutor detail page