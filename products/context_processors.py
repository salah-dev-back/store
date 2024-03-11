from products.models import Basket


def baskets(request):
    user = request.user
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        return {'baskets': basket}
    else:
        return []
