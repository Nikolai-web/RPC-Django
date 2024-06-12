from django.views.generic import FormView
from .forms import JSONRPCForm
from .rpc_client import rpc


class JSONRPCView(FormView):
    template_name = 'main_app/ui_form.html'
    form_class = JSONRPCForm
    success_url = '/'

    def form_valid(self, form):
        method = form.cleaned_data['method']
        params = form.cleaned_data['params']

        response_data = rpc(method, params)

        context = self.get_context_data(form=form, response_data=response_data)
        return self.render_to_response(context)
