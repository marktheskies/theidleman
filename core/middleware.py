from .models import ProductCategory


class CategoriesMiddleware:
    """A simple middleware that injects categories into view context"""

    def __init__(self, get_response):
        self.get_response = get_response
        self.categories = ProductCategory.objects.all()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data["categories"] = self.categories
        return response
