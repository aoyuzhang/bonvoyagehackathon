from django.shortcuts import render

# Create your views here.
from .models import Bankitem

def localbank_index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Bankitem.objects.all().count()
    # num_instances = BookInstance.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    context = {
        # 'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
        'num_bankitems' : num_books,
        'num_visits' : num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'local_bank_index.html', context=context)


from django.views import generic

class BankitemListView(generic.ListView):
    model = Bankitem
    paginate_by = 10
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

class BankitemDetailView(generic.DetailView):
	model = Bankitem


from django.contrib.auth.mixins import LoginRequiredMixin

class BankitemsownedByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Bankitem
    template_name ='localbank/bankitemins_list_owned_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        # return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
        return Bankitem.objects.filter(belongsto=self.request.user)