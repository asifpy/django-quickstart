from crudbuilder.abstract import BaseCrudBuilder

from .models import Team, Player
from .forms import PlayerForm


class PlayerCrud(BaseCrudBuilder):
    model = Player
    search_feilds = ['name']
    tables2_fields = ('name',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10
    modelform_excludes = ['created_by', 'updated_by']
    login_required = True
    custom_modelform = PlayerForm
