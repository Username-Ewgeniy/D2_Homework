#Запустить оболочку shell:

#python manage.py shell

#Импортировать модели:

from newapp.models import *

#1. Создать двух пользователей:

user1 = User.objects.create(username='Иван', first_name='Иванов')
user2 = User.objects.create(username='Петр', first_name='Петров') 


#2. Создать два объекта модели Author, связанные с пользователями:

Author.objects.create(authorUser=user1) 


Author.objects.create(authorUser=user2)  

#3. Добавить 4 категории в модель Category:

Category.objects.create(name='IT')

Category.objects.create(name='Образование') 

Category.objects.create(name='Спорт')

Category.objects.create(name='Политика')


#4. Добавить 2 статьи и 1 новость:

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Иван')), categoryType='NW', title='Название новости 1', text='Текст новости 1')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Иван')), categoryType='AR', title='Название статьи 2', text='Текст статьи 2')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Петр')), categoryType='AR', title='Название статьи 3', text='Текст статьи 3')


#5. Присвоить статьям/новостям категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)

c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Образование')
c3 = Category.objects.get(name='Спорт') 
c4 = Category.objects.get(name='Политика')

p1.postCategory.add(c1)
p1.postCategory.add(c2) 
p2.postCategory.add(c1, c2) 
p3.postCategory.add(c3, c4)


#6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий):

Comment.objects.create(commentUser=User.objects.get(username='Иван'), commentPost= Post.objects.get(pk=1), text='Текст комментария 1')

Comment.objects.create(commentUser=User.objects.get(username='Иван'), commentPost= Post.objects.get(pk=2), text='Текст комментария 2')

Comment.objects.create(commentUser=User.objects.get(username='Петр'), commentPost= Post.objects.get(pk=3), text='Текст комментария 3')

Comment.objects.create(commentUser=User.objects.get(username='Петр'), commentPost= Post.objects.get(pk=1), text='Текст комментария 4')

#7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов:

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like() 
Post.objects.get(pk=3).dislike() 
Post.objects.get(pk=3).dislike()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike() 
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).dislike() 
Comment.objects.get(pk=3).like()


#8. Обновить рейтинги пользователей:

Author.objects.get(authorUser=User.objects.get(username='Иван')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Петр')).update_rating()
a = Author.objects.get(authorUser=User.objects.get(username='Петр')) 
a.ratingAuthor

Author.objects.get(authorUser=User.objects.get(username='Иван')).ratingAuthor

#9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта):

best = Author.objects.all().order_by('-ratingAuthor').values('authorUser__username', 'ratingAuthor')[0]
print(best)


#10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье:

best_post = Post.objects.all().order_by('-rating').values('dateCreation', 'author__authorUser__username', 'rating', 'title')[0]
print(best_post)

#11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье:

best_p = Post.objects.all().order_by('-rating')[0]
print(best_p) 

comm_best_p = Comment.objects.filter(commentPost__id = best_p.id).values('dateCreation', 'commentUser__username', 'rating', 'text')
print(comm_best_p)
