from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name='index'),

	path('new_user/', views.crear_usuario, name='new_user'),
	path('usuario_creado/', views.usuario_creado, name='usuario_creado'),
        
	path('lista_productos/', views.lista_productos, name='lista_productos'),
        
	path('user_cart/',views.user_cart, name='user_cart'),
        
	path('login', views.loginView, name='login'),
	path('auth', views.auth, name='auth'),
	path('logout', views.logoutView, name='logout'),


#
#	path('lista_proyectos/',views.lista_proyectos, name='lista_proyectos'),
#	
#	path('added_project/', views.added_project, name='added_project'),
#	path('add_proyecto', views.add_proyecto, name='add_proyecto'),
#	path('new_project/', views.new_project, name='new_project'),
#
#	path('edit_project/', views.edit_project, name='edit_project'),
#	path('upd_project', views.upd_project, name='upd_project'),	
#	path('modified_project/', views.modified_project, name='modified_project'),
#
#
#
#	path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
#	
#	path('new_student/',views.new_student, name ='new_student'),
#	path('add_student', views.add_student, name='add_student'),        
#	path('added_student/', views.added_student, name='added_student'),
#	
#	path('edit_student/', views.edit_student, name='edit_student'),
#	path('upd_student', views.upd_student, name='upd_student'),
#	path('modified_student/', views.modified_student, name='modified_student'),
#
#	path('delete_student', views.delete_student, name='delete_student'),
#	path('deleted_student', views.deleted_student, name='deleted_student'),
#
#
#
#	path('new_ramo/', views.new_ramo, name='new_ramo'),
#	path('added_ramo/', views.added_ramo, name='added_ramo'),
#	path('add_ramo', views.add_ramo, name='add_ramo'),
#	path('modificar_ramo', views.modificar_ramo, name='modificar_ramo'),
#
#
#
#	path('new_group',views.new_group, name = 'new_group'),
#	path('added_group/', views.added_group, name='added_group'),
#	path('add_group', views.add_group, name='add_group'),


        
]

