from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from a_hr.models import Personnel, RaciMatrixDefinition, StakeholderRoles
from b_wbs.models import CostTypeClass, CostType, Department, Discipline, WBSType, WBS, FacilitySystem, \
    FacilitySystemDetail, TabWpExecutionType, PmbWpExecutionType, PmbWpStatusType
from e_commodities.models import CommodityType, Commodity
from f_contracts.models import Contract, TrendTypes
from g_measures.models import UOM
from h_schedules.models import TABSchedule, PMBSchedule
from d_mm.models import PurchaseOrder
from django.db import models
from d_mm.models import MaterialStatus
from e_commodities.models import CommodityDetail
from g_measures.models import MilepostTemplate


class PmbWp(models.Model):
    pmb_wp_exe_type = models.ForeignKey(PmbWpExecutionType, on_delete=models.CASCADE,
                                        verbose_name='PMB WP Execution Type ID', default=1)
    pmb_wp_status_type = models.ForeignKey(PmbWpStatusType, on_delete=models.CASCADE,
                                           verbose_name='PMB WP Status Type ID', default=1)
    wbs = models.ForeignKey(WBS, on_delete=models.CASCADE,
                            verbose_name='WBS ID', default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='CBWP Department ID', default=1)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   verbose_name='CBWP Discipline ID', default=1)
    pmb_schedule = models.ForeignKey(PMBSchedule, on_delete=models.CASCADE,
                                     verbose_name='PMB Schedule Activity ID', default=1)
    disc_start_date = models.DateTimeField(blank=True, null=True,
                                           verbose_name='Discretionary Start Date')
    disc_finish_date = models.DateTimeField(blank=True, null=True,
                                            verbose_name='Discretionary Finish Date')
    facility_system_detail = models.ForeignKey(FacilitySystemDetail, on_delete=models.CASCADE,
                                               verbose_name='CBWP Facility System Detail ID', default=1)
    pmb_wp_parent = models.ForeignKey('z_tab_pmb_quantum.PmbWp', on_delete=models.CASCADE,
                                             verbose_name='Parent ID', null=True, blank=True, default=1)
    primary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                       verbose_name='CBWP Primary Contact or Owner')
    secondary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                         verbose_name='CBWP Secondary Contact')
    pmb_wp_code = models.CharField(unique=True, max_length=55, verbose_name='PMB WP Code')
    pmb_wp_title = models.CharField(unique=True, max_length=200, blank=True, null=True, verbose_name='PMB WP Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB WP Details"
        db_table = 'pmb_wp'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_wp_code']

    def __str__(self):
        return f"{self.pmb_wp_code} - {self.pmb_wp_title}"


class PmbWpCaL03(models.Model):
    pmb_wp = models.ForeignKey(PmbWp, on_delete=models.CASCADE,
                               verbose_name='PMB WP ID', default=1)
    stakeholder_role = models.ForeignKey(StakeholderRoles, on_delete=models.CASCADE, verbose_name='Stakeholder Role ID',
                                        default=1)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='CBWP Cost Type ID',
                                  default=1)
    pmb_wp_ca_L03_code = models.CharField(unique=True, max_length=55, verbose_name='PMB WP CA L03 Code')
    pmb_wp_ca_L03_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                           verbose_name='PMB WP CA L03 Title')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # Quantification, Pricing, Hours and Costs
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    # Original Control Budget aka Final Estimate Budget
    ocb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='OCB Quantity', default=0)
    ocb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Hours', default=0)
    ocb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Costs', default=0)
    # Trend Control Budget
    tcb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='TCB Quantity', default=0)
    tcb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Hours', default=0)
    tcb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Costs', default=0)
    # Current Control Budget
    ccb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='CCB Quantity', default=0)
    ccb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Hours', default=0)
    ccb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Costs', default=0)
    # Trend Forecast Budget
    tfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='TFB Quantity', default=0)
    tfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Hours', default=0)
    tfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Costs', default=0)
    # Current Forecast Budget
    cfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='CFB Quantity', default=0)
    cfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Hours', default=0)
    cfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Costs', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "PMB WP CA L03 Details"
        db_table = 'pmb_wp_ca_L03'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_wp_ca_L03_code']

    def __str__(self):
        return f"{self.pmb_wp_ca_L03_code} - {self.pmb_wp_ca_L03_title}"


class PmbWpCaL04(models.Model):
    pmb_wp_ca_L03 = models.ForeignKey(PmbWpCaL03, on_delete=models.CASCADE,
                                      verbose_name='PMB WP CA L03 ID', default=1)
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE,
                                       verbose_name='CBWP Commodity Type ID', default=1)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='CBWP Commodity ID', default=1)
    pmb_wp_ca_L04_code = models.CharField(unique=True, max_length=55, verbose_name='PMB WP CA L04 Code')
    pmb_wp_ca_L04_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                           verbose_name='PMB WP CA L04 Title')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # Quantification, Pricing, Hours and Costs
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    # Current Forecast Budget
    bac_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='BAC Quantity', default=0)
    bac_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='BAC Hours', default=0)
    bac_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='BAC Costs', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "PMB WP CA L04 Details"
        db_table = 'pmb_wp_ca_L04'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_wp_ca_L04_code']

    def __str__(self):
        return f"{self.pmb_wp_ca_L04_code} - {self.pmb_wp_ca_L04_title}"


class ProjectComponent(models.Model):
    # A project component technically is a unique thing on a project, however we need the ability to reuse it
    # with the same identification across multiple functions. For e.g A pump "ABC-001" needs to be identified
    # and tracked during installation, but it 'may' need to be identified and tracked again during startup. These are
    # two separate activities with individual costs. For now, let us group the 'id' along with the 'function' for
    # uniqueness on the project.
    project_component_code = models.CharField(unique=True, max_length=25, verbose_name='Project Component Code')
    project_component_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                               verbose_name='Project Component Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Component Comments')

    # qty to be added here as this would represent client base quantities.

    class Meta:
        managed = True
        verbose_name_plural = "Project Components"
        db_table = 'project_component'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_component_code']

    def __str__(self):
        return str('%s' % self.project_component_code)


class ProjectDocument(models.Model):
    project_document_code = models.CharField(unique=True, max_length=25, verbose_name='Project Document Code')
    project_document_title = models.CharField(unique=True, max_length=100, verbose_name='Project Document Title')
    revision_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='Revision No')
    revision_status = models.CharField(max_length=55, blank=True, null=True, verbose_name='Revision Status')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Release Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Document Comments')
    document_attachment = models.FileField(blank=True, null=True, upload_to='Documents/',
                                           verbose_name='Document Attachment')
    document_url = models.URLField(blank=True, null=True, max_length=250,
                                   verbose_name='Document URL')

    class Meta:
        managed = True
        verbose_name_plural = "Project Documents"
        db_table = 'project_document'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_document_code']

    def __str__(self):
        return str('%s' % self.project_document_code)


class ProjectDocumentComponent(models.Model):
    # This is a junction table which joins a component with a document. It is the best form of uniqueness, but can be
    # overkill on some projects. The idea is to use (link) this unified widget in the csl_d_deliverables app for
    # tracking. The premise being that a unified_widget may still be on a very high level for tracking and may
    # need to be broken down some more for takeoff and tracking.
    project_document_component_code = models.CharField(unique=True, max_length=25,
                                                       verbose_name='Project Unified Document Component Code',
                                                       default='Test')
    project_document_component_title = models.CharField(unique=True, blank=True, null=True, max_length=100,
                                                        verbose_name='Project Unified Document Component Code Title')
    project_component = models.ForeignKey(ProjectComponent,
                                          on_delete=models.CASCADE, verbose_name='Project Component ID', default=1)
    project_document = models.ForeignKey(ProjectDocument,
                                         on_delete=models.CASCADE, verbose_name='Project Document ID', default=1)

    class Meta:
        managed = True
        verbose_name_plural = "Project Unified Documents Components"
        db_table = 'project_document_component'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_document_component_code']

    def __str__(self):
        return str('%s' % self.project_document_component_code)


class PmbWpCaL04Quantum(models.Model):
    pmb_wp_ca_L04 = models.ForeignKey(PmbWpCaL04, on_delete=models.CASCADE,
                                      verbose_name='PMB WP CA L04 ID', default=1)
    quantum_code = models.CharField(unique=True, max_length=55, verbose_name='PMB WP CA L04 Code')
    quantum_title = models.CharField(unique=True, max_length=200, blank=True, null=True,
                                     verbose_name='PMB WP CA L04 Title')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # Quantification, Pricing, Hours and Costs
    # uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    # Current Forecast Budget
    bac_quantum_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='BAC Quantum Quantity', default=0)
    # cfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                 verbose_name='CFB Hours', default=0)
    # cfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                 verbose_name='CFB Costs', default=0)
    project_document_component = models.ForeignKey(ProjectDocumentComponent, blank=True, null=True,
                                                   on_delete=models.CASCADE,
                                                   verbose_name='Project Document Component ID',
                                                   default=1)
    material_status = models.ForeignKey(MaterialStatus, on_delete=models.CASCADE,
                                        verbose_name='Material Status ID', default=1)
    commodity_detail = models.ForeignKey(CommodityDetail, on_delete=models.CASCADE,
                                         verbose_name='Commodity Detail ID', default=1)
    milepost_template = models.ForeignKey(MilepostTemplate, on_delete=models.CASCADE,
                                          verbose_name='Milepost Template ID', default=1)
    # cad_id = models.CharField(max_length=55, blank=True, null=True, verbose_name='CAD ID')
    mp_01_date_p = models.DateTimeField(verbose_name='1st Planned MP Date', blank=True, null=True, )
    mp_01_date_e = models.DateTimeField(verbose_name='1st Earned MP Date', blank=True, null=True, )
    mp_02_date_p = models.DateTimeField(verbose_name='2nd Planned MP Date', blank=True, null=True, )
    mp_02_date_e = models.DateTimeField(verbose_name='2nd Earned MP Date', blank=True, null=True, )
    mp_03_date_p = models.DateTimeField(verbose_name='3rd Planned MP Date', blank=True, null=True, )
    mp_03_date_e = models.DateTimeField(verbose_name='3rd Earned MP Date', blank=True, null=True, )
    mp_04_date_p = models.DateTimeField(verbose_name='4th Planned MP Date', blank=True, null=True, )
    mp_04_date_e = models.DateTimeField(verbose_name='4th Earned MP Date', blank=True, null=True, )
    mp_05_date_p = models.DateTimeField(verbose_name='05th Planned Milepost Date', blank=True, null=True, )
    mp_05_date_e = models.DateTimeField(verbose_name='05th Earned Milepost Date', blank=True, null=True, )
    mp_06_date_p = models.DateTimeField(verbose_name='06th Planned Milepost Date', blank=True, null=True, )
    mp_06_date_e = models.DateTimeField(verbose_name='06th Earned Milepost Date', blank=True, null=True, )
    mp_07_date_p = models.DateTimeField(verbose_name='07th Planned Milepost Date', blank=True, null=True, )
    mp_07_date_e = models.DateTimeField(verbose_name='07th Earned Milepost Date', blank=True, null=True, )
    mp_08_date_p = models.DateTimeField(verbose_name='08th Planned Milepost Date', blank=True, null=True, )
    mp_08_date_e = models.DateTimeField(verbose_name='08th Earned Milepost Date', blank=True, null=True, )
    mp_09_date_p = models.DateTimeField(verbose_name='09th Planned Milepost Date', blank=True, null=True, )
    mp_09_date_e = models.DateTimeField(verbose_name='09th Earned Milepost Date', blank=True, null=True, )
    mp_10_date_p = models.DateTimeField(verbose_name='10th Planned Milepost Date', blank=True, null=True, )
    mp_10_date_e = models.DateTimeField(verbose_name='10th Earned Milepost Date', blank=True, null=True, )

    class Meta:
        managed = True
        verbose_name_plural = "PMB WP CA L04 Quantum Details"
        db_table = 'pmb_wp_ca_L04_quantum'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['quantum_code']

    def __str__(self):
        return f"{self.quantum_code} - {self.quantum_title}"
