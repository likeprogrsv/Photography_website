from django.test import TestCase
from main.models import Photos


class PhotosModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Photos.objects.create(
            name="Grass - Testing image name",
            image=(r'C:\Storage\Programming\PythonProject'
                   r'\Photography_website\taskmanager\files'
                   r'\photos\IMG_3349.jpg'),
            category=['grass', 'green', 'nature'],
            description="Testing image description",
            year_photo="2022",
            rating="0")

    def test_name_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_image_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')

    def test_category_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_description_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_rating_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_year_label(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('year_photo').verbose_name
        self.assertEquals(field_label, 'year photo')

    def test_object_name(self):
        image = Photos.objects.get(id=1)
        expected_name = image.name
        self.assertEquals(expected_name, str(image))

    def test_name_maxlength(self):
        image = Photos.objects.get(id=1)
        field_label = image._meta.get_field('name').max_length
        self.assertEquals(field_label, 200)

    def test_rating_value(self):
        image = Photos.objects.get(id=1)
        field_label = image.rating
        self.assertTrue(field_label <= 5)

    def test_year_value(self):
        image = Photos.objects.get(id=1)
        field_label = image.year_photo
        self.assertTrue(2013 < field_label <= 2120)
