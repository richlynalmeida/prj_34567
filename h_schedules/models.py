from django.db import models
from b_wbs.models import Discipline
from z_tab_pmb_quantum.models import PmbWpExecutionType, TabWpExecutionType


class TABSchedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    tab_wp_exe_type = models.ForeignKey(PmbWpExecutionType, on_delete=models.CASCADE, verbose_name='TAB Type Code', default=1)
    tab_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='TAB Schedule Code')
    tab_schedule_title = models.CharField(max_length=2000, blank=True, null=True, verbose_name='TAB Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='TAB Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='TAB Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='TAB Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='TAB Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='TAB Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='TAB Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='TAB Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='TAB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "TAB aka EB aka L03 Schedule"
        db_table = 'tab_schedule'
        app_label = 'h_schedules'
        ordering = ['tab_schedule_code']

    def __str__(self):
        return f"{self.tab_schedule_code} - {self.tab_schedule_title}"


class PMBSchedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    pmb_wp_exe_type = models.ForeignKey(PmbWpExecutionType, on_delete=models.CASCADE, verbose_name='PMB Type Code', default=1)
    tab_schedule = models.ForeignKey(TABSchedule, on_delete=models.CASCADE,
                                     verbose_name='TAB Schedule Code')
    pmb_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='CB Schedule Code')
    pmb_schedule_title = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CB Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='CB Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='CB Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='CB Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='CB Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB aka CB aka L04 Schedule"
        db_table = 'pmb_schedule'
        app_label = 'h_schedules'
        ordering = ['pmb_schedule_code']

    def __str__(self):
        return f"{self.pmb_schedule_code} - {self.pmb_schedule_title}"
