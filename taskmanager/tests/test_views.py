from django.test import TestCase, Client
from django.urls import reverse
from main.models import Photos, Comment
from main.forms import CommentForm
from django.contrib.auth.models import User
from django.contrib import auth

class TestViews(TestCase):

    def setUp(self):
        self.photo_1 = Photos.objects.create(name="Grass", 
        image="C:\Storage\Programming\PythonProjects\Photography_website\taskmanager\files\photos\IMG_3349.jpg",
        category=['grass', 'green', 'nature'], description="Testing image description", year_photo="2022", rating="0")

        # self.user_for_testing = User.objects.create(username="comment_user")
        # self.user_for_testing.set_password('12345')
        # self.user_for_testing.save()
        

        # self.comment = Comment.objects.create(
        #     user=self.user_for_testing,
        #     photo=self.photo_1)            
        
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        
        self.home_url = reverse('home')       
        self.photography_url = reverse('photography', args=[self.photo_1.id])


    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
    
    def test_photography_page_GET(self):
        response = self.client.get(self.photography_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/photography.html')

    def test_user_is_logged(self):  
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        

    def test_comments_on_photo_page_POST(self):  
        # form = CommentForm(data={
        #     'content': 'testing comment from testing user'
        # })          
        response = self.client.post(self.photography_url, data={'content': 'testing comment from testing user'})       
        self.assertRedirects(response, reverse('photos'))
        # self.assertEquals(self.comment.content, 'testing comment from testing user')