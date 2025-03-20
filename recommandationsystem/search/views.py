from elasticsearch_dsl import Q
from .documents import ProductDocument
from .models import Product
from django.http import JsonResponse
from .models import Product
from django.shortcuts import render
from django.core.paginator import Paginator

def search_view(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    per_page = 10

    search = ProductDocument.search()

    if query:
        # q = Q("wildcard", name=f"*{query}*") | Q("wildcard", tags=f"*{query}*") |Q("wildcard", category=f"*{query}*")  | Q("match_phrase_prefix", description=query)
        # search = search.query(q)

        search = ProductDocument.search().query(
                        'bool',
            should=[
                Q("match", name=query),  
                Q("match", tags=query),
                Q("match", category=query),
                Q("match", description=query)
            ],
            minimum_should_match=1
            )


    results = search.extra(size=10000).execute() 
    print('results',results)
    paginator = Paginator(results, per_page)
    paginated_results = paginator.get_page(page)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = {
            "products": [{"id": r.meta.id, "name": r.name, "category": r.category, "price": r.price} for r in paginated_results],
            "has_next": paginated_results.has_next(),
            "next_page": page + 1
        }
        return JsonResponse(response, safe=False)

    return render(request, 'search_results.html', {'query': query, 'results': paginated_results})
