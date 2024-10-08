from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.contrib import messages


# Create your views here.
@method_decorator(login_required, name='dispatch')
class StatusesIndex(View):
    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'statuses/index.html', {'statuses': statuses})


@method_decorator(login_required, name='dispatch')
class StatusFormCreate(View):
    def get(self, request):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('statuses_index')
        return render(request, 'statuses/create.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class StatusFormUpdate(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = StatusForm(instance=status)
        return render(
            request,
            'statuses/update.html',
            {'form': form, 'status_id': status_id}
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно изменен')
            return redirect('statuses_index')
        return render(request, 'statuses/create.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class StatusFormDelete(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        return render(request, 'statuses/delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        if status:  # ещё првоерку используется ли он где-то дял удаления
            status.delete()
            messages.success(request, 'Статус успешно удален')
        return redirect('statuses_index')
