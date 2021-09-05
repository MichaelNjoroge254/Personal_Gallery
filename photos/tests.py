from django.test import TestCase
from .models import Category,Photo

# Create your tests here.

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.favourite= Category(name = 'Favourite')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.favourite,Category))

    #Testing Save Method
    def test_save_method(self):
        self.favourite.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)


class photoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.saved= photo(name = 'Saved')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.saved,Photo))

    #Testing Save Method
    def test_save_method(self):
        self.saved.save_photo()
        photos = photo.objects.all()
        self.assertTrue(len(photos) > 0)
