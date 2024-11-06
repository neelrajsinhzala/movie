from django.shortcuts import render
import requests

# View to render the selection form
def select_search(request):
    return render(request, 'select_search.html')

# View to process search request
def search_view(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        search_type = request.POST.get('search_type')
        first_air_date_year = request.POST.get('first_air_date_year')
        # Call the appropriate function based on the selection
        if search_type == 'movie':
            return movie_search(request, search_term)
        elif search_type == 'tv':
            return tv_shows(request, search_term, first_air_date_year)

# Function to fetch movie data
def movie_search(request, search_term):
    search_term = request.POST.get('search_term')
    url = f"https://api.themoviedb.org/3/search/movie?query={search_term}&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MGYyYTkwNzY2MzI1MzdkYTUwZjUxNmQ2MGIxMzFhYyIsIm5iZiI6MTczMDg2NzI3Ny4yODkwNzA4LCJzdWIiOiI2NzI5ZmVlYWQwYzA3MmFkNDhmNTFiOTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.o-BoIxukfIu419TZKONGvwZu6ahgncCNuA7ogOLjBWg"
    }
    response = requests.get(url, headers=headers)
    data = response.json().get('results', [])
    return render(request, 'movie.html', {'data': data, 'search_term': search_term})

# Function to fetch TV series data
def tv_shows(request,search_term, first_air_date_year):
    search_term = request.POST.get('search_term')
    first_air_date_year = request.POST.get('first_air_date_year')
    url = f"https://api.themoviedb.org/3/search/tv?query={search_term}&first_air_date_year={first_air_date_year}&include_adult=true&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MGYyYTkwNzY2MzI1MzdkYTUwZjUxNmQ2MGIxMzFhYyIsIm5iZiI6MTczMDg2NzI3Ny4yODkwNzA4LCJzdWIiOiI2NzI5ZmVlYWQwYzA3MmFkNDhmNTFiOTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.o-BoIxukfIu419TZKONGvwZu6ahgncCNuA7ogOLjBWg"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        data = response_data.get('results', [])
        print(data)
    else:
        data = []
    return render(request, 'tv.html', {'data': data})

def movie_details(request, id):
    url = f"https://api.themoviedb.org/3/movie/{id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MGYyYTkwNzY2MzI1MzdkYTUwZjUxNmQ2MGIxMzFhYyIsIm5iZiI6MTczMDg2NzI3Ny4yODkwNzA4LCJzdWIiOiI2NzI5ZmVlYWQwYzA3MmFkNDhmNTFiOTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.o-BoIxukfIu419TZKONGvwZu6ahgncCNuA7ogOLjBWg"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        movie_details = response.json()
    else:
        movie_details = {}
    return render(request, 'movie_details.html', {'movie_details' : movie_details})

def tv_details(request, id):
    # Define the Movie Details API endpoint with the provided movie ID
    url = f"https://api.themoviedb.org/3/tv/{id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MGYyYTkwNzY2MzI1MzdkYTUwZjUxNmQ2MGIxMzFhYyIsIm5iZiI6MTczMDg2NzI3Ny4yODkwNzA4LCJzdWIiOiI2NzI5ZmVlYWQwYzA3MmFkNDhmNTFiOTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.o-BoIxukfIu419TZKONGvwZu6ahgncCNuA7ogOLjBWg"
    }
    # Fetch the detailed information for the movie
    response = requests.get(url, headers=headers)
    # Check if the response is successful
    if response.status_code == 200:
        tv_details = response.json()
        print(tv_details)
    else:
        tv_details = {}  # Fallback in case of an error
    # Render the template with the movie details
    return render(request, 'tv_details.html', {'tv_details': tv_details})
