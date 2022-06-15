from .models import Category


def menu_links(request):
    links = Category.objects.all()  # fetches all category from category models
    return dict(links=links)  # returns links as dictionaries
