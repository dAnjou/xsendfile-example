import os

from django.http import HttpResponse, Http404
from django.template import Context, Template
from django.conf import settings

from sendfile import sendfile


def serve_file(request, path):
    path = os.path.join(settings.SENDFILE_ROOT_DIR, path)

    if os.path.isfile(path):
        return sendfile(request, path)

    elif os.path.isdir(path):
        files = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                files.append(f)
        t = Template("""
<link rel="icon" href="data:;base64,iVBORw0KGgo=">
<ul>
    {% for f in files %}<li>
        <a href="./{{ f }}">{{ f }}</a>
    </li>{% endfor %}
</ul>""")
        return HttpResponse(t.render(Context({"files": files})))

    raise Http404()
