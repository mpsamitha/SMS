from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template

from .utils import render_to_pdf

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': '##', 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('marksedit.html', data)
        return HttpResponse(pdf, content_type='application/pdf')