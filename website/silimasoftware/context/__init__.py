class Context:
    def get_context(self):
        self.context = {
            "current_page": self.request.path.split("/")[-2],
            "page": self.page,
            "function": self.function,
            "template": self.template_path,
            "javascript": [
                self.javascript_path,
            ],
        }
        try:
            self._page = self.context_factory()
        except Exception as e:
            raise e
        else:
            self.context |= self._page.context if self._page else self.no_context()

    def context_factory(self):
        func = {
            "home": self.no_context,
            "blog": self.no_context,
            "about": self.no_context,
            "contact": self.no_context,
        }
        return func[self.page](self)

    def no_context(*args, **kwargs):
        return {}
