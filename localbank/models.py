from django.db import models
from django.urls import reverse

# class MyModelName(models.Model):
#     """A typical class defining a model, derived from the Model class."""

#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
#     ...

#     # Metadata
#     class Meta:
#         ordering = ['-my_field_name']

#     # Methods
#     def get_absolute_url(self):
#         """Returns the URL to access a particular instance of MyModelName."""
#         return reverse('model-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.my_field_name


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Bankitem(models.Model):
    """Model representing a bank item"""
    bankItemName = models.CharField(max_length=200)
    itemAquiredOn = models.DateTimeField(auto_now_add=False)
    bankitemDescription = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    bankItemPrice = models.FloatField(help_text='The price of item when bought')
    # bank_item_description = models.CharField(max_length=2000)

    # class Meta:
    #     ordering = ['last_name', 'first_name']

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
        # isbn = models.CharField('ISBN', max_length=13, unique=True,
                             # help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        # return self.title
        return self.bankitemDescription

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('bankitem-detail', args=[str(self.id)])
        # pass