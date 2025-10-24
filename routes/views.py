from django.http import JsonResponse
from .models import Airport, FlightPath
from django.shortcuts import render


def bellman_ford(request):
    source = request.GET.get('source', '').lower()
    destination = request.GET.get('destination', '').lower()

    all_airports = Airport.objects.all()
    graph = {airport.code.lower(): [] for airport in all_airports}
    all_paths = FlightPath.objects.all()

    for path in all_paths:
        graph[path.source.code.lower()].append((path.destination.code.lower(), path.distance))

    if source not in graph or destination not in graph:
        return JsonResponse({'error': 'Invalid source or destination.'})

    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for src in graph:
            for dest, weight in graph[src]:
                if distance[src] + weight < distance[dest]:
                    distance[dest] = distance[src] + weight

    if distance[destination] == float('inf'):
        return JsonResponse({'message': 'No path found.'})

    return JsonResponse({'source': source, 'destination': destination, 'shortest_distance': distance[destination]})

def home(request):
    return render(request, 'home.html')


