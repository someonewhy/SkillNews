# SkillNews
Итоговая по 5 модулю
Вводные команды в shell
Запустите консоль Django с помощью команды python manage.py shell.
Импортируйте необходимые модели и объекты:
from django.contrib.auth.models import User
from myapp.models import Author, Category, Post, PostCategory, Comment
Создайте двух пользователей и два объекта модели Author:
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
Создайте четыре категории:
category1 = Category.objects.create(name='Sports')
category2 = Category.objects.create(name='Politics')
category3 = Category.objects.create(name='Education')
category4 = Category.objects.create(name='Technology')
Создайте две статьи и одну новость и свяжите их с категориями:
post1 = Post.objects.create(author=author1, post_type='article', title='Article 1', content='Content 1')
post2 = Post.objects.create(author=author2, post_type='article', title='Article 2', content='Content 2')
post3 = Post.objects.create(author=author1, post_type='news', title='News 1', content='Content 3')
post1.categories.add(category1, category2)
post2.categories.add(category3, category4)
post3.categories.add(category1, category3)
Создайте четыре комментария к разным объектам модели Post:
comment1 = Comment.objects.create(post=post1, user=user1, text='Comment 1')
comment2 = Comment.objects.create(post=post2, user=user2, text='Comment 2')
comment3 = Comment.objects.create(post=post3, user=user1, text='Comment 3')
comment4 = Comment.objects.create(post=post1, user=user2, text='Comment 4')
Примените функции like() и dislike() для корректировки рейтингов объектов:
post1.like()
post2.dislike()
comment1.like()
comment3.like()
comment4.dislike()
Обновите рейтинги пользователей:
author1.update_rating()
author2.update_rating()
Выведите username и рейтинг лучшего пользователя:
best_author = Author.objects.order_by('-rating').first()
best_author.user.username
best_author.rating
Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи:
best_post = Post.objects.filter(post_type='article').order_by('-rating').first()
best_post.created_at
best_post.author.user.username
best_post.rating
best_post.title
best_post.preview()
Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье:
post = Post.objects.get(id=1)  # Здесь 1 - это идентификатор статьи, замените его на нужный вам
comments = Comment.objects.filter(post=post)
for comment in comments:
    print(f"Дата: {comment.created_at}")
    print(f"Пользователь: {comment.user.username}")
    print(f"Рейтинг: {comment.rating}")
    print(f"Текст: {comment.text}")
    print("------------------------")


