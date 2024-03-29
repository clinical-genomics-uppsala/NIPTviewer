from dataprocessor.models import BatchRun, Flowcell, SamplesRunData, SampleType
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from reportvisualiser.utils import plots
from reportvisualiser.forms import SearchResult

import datetime
from dateutil.relativedelta import *


@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse("index"))
        else:
            context['login_error'] = "Invalid username or password"
            if request.POST['username']:
                context['username'] = request.POST['username']
    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))


@login_required
def index(request, time_selection=settings.DEFAULT_TIME_SELECTION):
    now = datetime.datetime.now()
    time_selection = int(time_selection)
    previous_time = now + relativedelta(months=-time_selection)

    if time_selection < 9999:
        flowcells = Flowcell.objects.filter(run_date__lte=now, run_date__gte=previous_time).order_by('-run_date')
        sample_run_data = SamplesRunData.objects.filter(flowcell_id__in=flowcells).order_by(
            '-flowcell_id__run_date').select_related().values('ff_formatted', 'flowcell_id__run_date',
                                                              'flowcell_id__flowcell_barcode', 'sample_id', 'sample_type__name')
        control_flowcell_data = SamplesRunData.objects.select_related(). \
            filter(flowcell_id__in=flowcells, sample_type=SampleType.objects.get(name="Control")). \
            order_by('-flowcell_id__run_date').values('sample_type__name', 'flowcell_id__run_date',
                                                      'flowcell_id__flowcell_barcode', 'ncd_13', 'ncd_18', 'ncd_21', 'ncd_x',
                                                      'ncd_y', 'sample_id', 'sample_type__name')
        num_flowcells = len(flowcells)
        num_samples = len(sample_run_data)
        total_num_flowcells = Flowcell.objects.count()
        total_num_samples = SamplesRunData.objects.count()
    else:
        flowcells = Flowcell.objects.all().order_by('-run_date')
        sample_run_data = SamplesRunData.objects.all().order_by('-flowcell_id__run_date').select_related(). \
            values('ff_formatted', 'flowcell_id__run_date', 'flowcell_id__flowcell_barcode', 'sample_id', 'sample_type__name')
        control_flowcell_data = SamplesRunData.objects.filter(sample_type=SampleType.objects.get(name="Control")). \
            select_related().order_by('-flowcell_id__run_date').values('sample_type__name', 'flowcell_id__run_date',
                                                                       'flowcell_id__flowcell_barcode', 'ncd_13', 'ncd_18',
                                                                       'ncd_21', 'ncd_x', 'ncd_y', 'sample_id',
                                                                       'sample_type__name')
        num_flowcells = total_num_flowcells = Flowcell.objects.count()
        num_samples = total_num_samples = SamplesRunData.objects.count()

    context = {
        'total_num_flowcells': total_num_flowcells,
        'total_num_samples': total_num_samples,
        'num_flowcells': num_flowcells,
        'num_samples': num_samples,
        'latest_flowcells': [],
        'latest_samples': [],
        'time_selection': time_selection,
        "search_form": SearchResult()
    }
    if num_flowcells > 0:
        context['latest_flowcells'] = flowcells[:5]
        context['latest_samples'] = sample_run_data[:5]

        if sample_run_data.exists():
            context.update(plots.fetal_fraction(data=sample_run_data))

        if control_flowcell_data.exists():
            context['ncd'] = plots.ncd_data(control_flowcell_data)

    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))
