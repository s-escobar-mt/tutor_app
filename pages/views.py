from django.views.generic import TemplateView, DetailView,ListView,CreateView
from accounts.models import CustomUser, Schedule

class HomePageView(ListView):
    model=CustomUser
    template_name = "home.html"

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutors'] = CustomUser.objects.all()  # Add users to the context
        return context
    '''
class TutorDetailView(DetailView):
    model =CustomUser
    template_name = "tutor_detail.html"
    context_object_name='tutor'

class AddHoursView(CreateView):
    model=Schedule
    template_name="add_hours.html"