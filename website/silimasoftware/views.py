from .core import (
    HttpResponse,
    SMTPException,
    View,
    secrets,
    requests,
    bleach,
    json,
    is_ajax,
    is_get,
    render,
    log,
    render,
    push_msg,
    time,
    send_mail,
    get_msgs,
    forbidden,
)
from .context import Context


class silimasoftware(View, Context):
    def dispatch(self, request, page="home", function="index"):
        self.page = bleach.clean(page)
        self.function = bleach.clean(function)
        self.template_path = f"pages/{self.page}/index.html"
        self.javascript_path = f"js/{self.page}.js"
        if request.POST.get("action"):
            self.action = bleach.clean(request.POST.get("action"))
        else:
            self.action = self.page
        return super(silimasoftware, self).dispatch(request)

    def post(self, request):
        try:
            self.get_context()
        except Exception as e:
            log(e)
            return HttpResponse(
                json.dumps({"Failed to proccess the request!"}),
                content_type="application/json",
            )

        return HttpResponse(json.dumps(self.context), content_type="application/json")

    def get(self, request):
        try:
            self.get_context()
        except Exception as e:
            log(e)
            push_msg(
                self.request, "Failed to find the page or resource!", "alert-warning"
            )
            return render(self.request, "index.html", {"template": "src/error.html"})

        return render(self.request, "index.html", self.context)

