from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["homepage_count_button_props"] = {
            "isAuthenticated": user.is_authenticated,
            "count": user.count if user.is_authenticated else None,
        }

        return context
