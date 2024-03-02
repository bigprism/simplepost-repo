from django.test import TestCase

class BlogPostModelTest(TestCase):
    def test_create_blog_post(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        self.assertEqual(blog_post.title, 'My Blog Post')
        self.assertEqual(blog_post.content, 'This is my blog post content.')
        self.assertEqual(blog_post.author, self.user)

from django.test import TestCase

class BlogPostListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog_post_list.html')

    def test_view_contains_all_blog_posts(self):
        BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get('/blog/')
        self.assertContains(response, 'My Blog Post')

from django.test import TestCase

class BlogPostDetailViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/')
        self.assertTemplateUsed(response, 'blog_post_detail.html')

    def test_view_contains_correct_blog_post(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/')
        self.assertContains(response, 'My Blog Post')

from django.test import TestCase

class BlogPostCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/blog/create/')
        self.assertTemplateUsed(response, 'blog_post_create.html')

    def test_view_contains_correct_form(self):
        response = self.client.get('/blog/create/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<input type="text" name="title" id="id_title"')
        self.assertContains(response, '<textarea name="content" id="id_content"')

from django.test import TestCase

class BlogPostUpdateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/update/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/update/')
        self.assertTemplateUsed(response, 'blog_post_update.html')

    def test_view_contains_correct_form(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/update/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, f'<input type="text" name="title" id="id_title" value="{blog_post.title}"')
        self.assertContains(response, f'<textarea name="content" id="id_content">{blog_post.content}</textarea>')

from django.test import TestCase

class BlogPostDeleteViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/delete/')
        self.assertTemplateUsed(response, 'blog_post_delete.html')

    def test_view_contains_correct_form(self):
        blog_post = BlogPost.objects.create(
            title='My Blog Post',
            content='This is my blog post content.',
            author=self.user
        )
        response = self.client.get(f'/blog/{blog_post.pk}/delete/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, f'<button type="submit" class="btn btn-danger">Delete</button>')

from django.test import TestCase

class BlogPostFormTest(TestCase):
    def test_valid_data(self):
        form = BlogPostForm(data={
            'title': 'My Blog Post',
            'content': 'This is my blog post content.',
            'author': self.user
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = BlogPostForm(data={
            'title': '',
            'content': '',
            'author': None
        })
        self.assertFalse(form.is_valid())