from django.shortcuts import render
from django.http import Http404
from jobs.models import Cities, JobTypes
from jobs.models import Job, Resume
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from jobs.forms import ResumeForm

# Create your views here.
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context =  {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    return render(request, 'joblist.html', context)

def detail(request, job_id):
    # print('进入这里啦')
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        # logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    # print(job.__dict__)
    return render(request, 'job.html', {'job': job})

class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'


class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree",
        "candidate_introduction", "work_experience", "project_experience"]


    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

    # 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial
    # 将简历与当前用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())