from crudbuilder.abstract import BaseCrudBuilder

from core.models import Post


class PostCrud(BaseCrudBuilder):
    model = Post
    search_fields = ['name']
    tables2_fields = ('name',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10
    modelform_excludes = ['created_by', 'updated_by']
    login_required = True
