from datetime import date
from django.shortcuts import render

posts= [
    {
        "slug": "ahnaf-with-juna",
        "img": "withjuna.jpg",
        "author": "Shamun",
        "date": date (2024, 7 , 21),
        "title": "Ahnaf",
        "excerpt": "Say something about this column!",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis eum quam unde. Earum voluptates, laudantium dolore neque recusandae dolorum adipisci fugit labore vitae quas soluta eum exercitationem dolor magnam rem?
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis eum quam unde. Earum voluptates, laudantium dolore neque recusandae dolorum adipisci fugit labore vitae quas soluta eum exercitationem dolor magnam rem?
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis eum quam unde. Earum voluptates, laudantium dolore neque recusandae dolorum adipisci fugit labore vitae quas soluta eum exercitationem dolor magnam rem?
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis eum quam unde. Earum voluptates, laudantium dolore neque recusandae dolorum adipisci fugit labore vitae quas soluta eum exercitationem dolor magnam rem?
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis eum quam unde. Earum voluptates, laudantium dolore neque recusandae dolorum adipisci fugit labore vitae quas soluta eum exercitationem dolor magnam rem?

        """
        
    }
]
# Create your views here.
def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-details.html" )