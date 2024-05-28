from django.shortcuts import render

class IndexController:
  def home(request):
    return render(request, "index.html")
