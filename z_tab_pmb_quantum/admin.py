from django.contrib import admin

from .models import PmbWp, PmbWpCaL03
from . import models
from f_finance.models import PmbWpCaL04AccountsPayable, PmbWpCaL04AccountsReceivable
from l_actuals.models import PmbWpCaL04Actuals
from z_tab_pmb_quantum.models import PmbWpCaL04Quantum
from m_claims.models import PmbWpCaL04ClaimDetail
from r_risk.models import Risks


admin.site.register(models.PmbWp)
admin.site.register(models.PmbWpCaL03)
admin.site.register(models.PmbWpCaL04)
admin.site.register(models.ProjectDocument)
admin.site.register(models.ProjectComponent)
admin.site.register(models.ProjectDocumentComponent)
admin.site.register(models.PmbWpCaL04Quantum)