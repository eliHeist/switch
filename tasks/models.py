from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class TaskGroup(models.Model):
    name = models.CharField(max_length=20)
    is_global = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    class STATUSES(models.IntegerChoices):
        DEFAULT = 0, "DEFAULT"
        PROGRESS = 1, "PROGRESS"
        PAUSED = 2, "PAUSED"
        READY = 3, "READY"
        REVIEW = 4, "REVIEW"
        DECLINED = 5, "DECLINED"
        STOPPED = 10, "STOPPED"
    
    title = models.CharField(max_length=50)
    details = models.TextField(blank=True)
    
    task_group = models.ForeignKey(TaskGroup, related_name='tasks', on_delete=models.SET_NULL, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUSES.choices, default=STATUSES.DEFAULT)

    # people
    creator = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)
    tagged = models.ManyToManyField(User, related_name='tagged_tasks', blank=True)

    # time tracking
    track_start_time = models.DateTimeField(blank=True, null=True)
    track_end_time = models.DateTimeField(blank=True, null=True)

    # dates
    due_date = models.DateField(null=True)
    scheduled_start = models.DateTimeField(blank=True, null=True)
    scheduled_end = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title



