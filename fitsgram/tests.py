from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(user = self.user)
        self.profile.save()
        self.image = Image(id=1,image = 'path/to/image',image_name='test',image_caption='test caption',user=self.user,profile=self.profile)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

        #Testing Save method
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        
