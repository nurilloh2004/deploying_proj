from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf.document import pisaDocument
from django.conf import settings
from io import BytesIO


def html_to_pdf(template_src: str, context: dict = None):
    if context is None:
        context = {}
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisaDocument(BytesIO(html.encode("UTF-8")), dest = result, encoding='UTF-8', path=settings.STATIC_ROOT)
    return None if pdf.err else HttpResponse(result.getvalue(), content_type='application/pdf') 
