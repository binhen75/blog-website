from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test+user", password="test", email="asd@gmail.com"
        )
        cls.post = Post.objects.create(
            title="Title",
            body="Body",
            author=cls.user,
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "Title")         
        self.assertEqual(self.post.body, "Body")        
        self.assertEqual(self.post.author.username, self.user.username)        
        self.assertEqual(str(self.post), "Title")   
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
    
    def test_response_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_response_individual_post(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Body")
        self.assertContains(response, "Title")
        self.assertContains(response, "test+user")

    def test_individual_content(self):
        response = self.client.get(reverse("single_post", kwargs={"pk":self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Body")
        self.assertContains(response, "Title")
        self.assertContains(response, "test+user")
    
    def test_post_createview(self):
        response = self.client.post(reverse("post_new"),
                                    {
                                        "title": "New title",
                                        "body": "New text",
                                        "author": self.user.id,
                                    })
        self.assertEqual(response.status_code, 302) #confirms that a 302 redirect occurs  
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(reverse("post_edit", args="1"),
                                    {
                                        "title": "Changed title",
                                        "body": "Changed text",
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Changed title")
        self.assertEqual(Post.objects.last().body, "Changed text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)




