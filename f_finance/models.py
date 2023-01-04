from django.db import models
# from j_cb.models import CBWP
from djmoney.models.fields import MoneyField
from z_tab_pmb_quantum.models import PmbWpCaL04


class PmbWpCaL04AccountsReceivable(models.Model):
    pmb_wp_ca_L04 = models.ForeignKey(PmbWpCaL04, on_delete=models.CASCADE, verbose_name='PMB WP CA L04 ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ar_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Receivable Costs on Calendar Date', default=0)
    ar_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Receivable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('pmb_wp_ca_L04', 'calendar_date'),)
        verbose_name_plural = "PMB WP CA L04 Accounts Receivable"
        db_table = 'pmb_wp_ca_L04_ar'
        app_label = 'f_finance'
        ordering = ['pmb_wp_ca_L04', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.pmb_wp_ca_L04))


class PmbWpCaL04AccountsPayable(models.Model):
    pmb_wp_ca_L04 = models.ForeignKey(PmbWpCaL04, on_delete=models.CASCADE, verbose_name='PMB WP CA L04 ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ap_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Payable Costs on Calendar Date', default=0)
    ap_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Payable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('pmb_wp_ca_L04', 'calendar_date'),)
        verbose_name_plural = "PMB WP CA L04 Accounts Payable"
        db_table = 'pmb_wp_ca_L04_ap'
        app_label = 'f_finance'
        ordering = ['pmb_wp_ca_L04', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.pmb_wp_ca_L04))
