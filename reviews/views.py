from django.shortcuts import render, get_object_or_404
from .models import Wine, Review
from django.views import generic
from .forms import ReviewForm
import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
class ReviewList(generic.ListView):
    template_name = 'reviews/review_list.html'
    context_object_name = 'latest_review_list'

    def get_queryset(self):
        return Review.objects.order_by('-pub_date')[:9]


class ReviewDetail(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'


class WineList(generic.ListView):
    template_name = 'reviews/wine_list.html'
    context_object_name = 'wine_list'

    def get_queryset(self):
        return Wine.objects.order_by('-name')


def wine_detail(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    form = ReviewForm()
    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})


@login_required(login_url='reviewers:login')
def add_review(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.wine = wine
            review.user_name=request.user.username#the request uses username to refer to the active user
            review.pub_date = datetime.datetime.now()
            review.save()
            return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))
    else:
        form = ReviewForm()
    return render(request, 'reviews/wine_detail.html', {'form': form, 'wine': wine})


def user_review_list(request, username=None):
    if not username:
        username=request.user.username
    latest_review_list=Review.objects.filter(user_name=username).order_by('-pub_date')
    return render(request, 'reviews/user_review_list.html', {'latest_review_list':latest_review_list, 'username':username})













