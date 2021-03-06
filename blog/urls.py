from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:blog_id>/', views.PostDetailView.as_view, name='post_detail'),
    path('post/new/', views.CreatePOstView.as_view(),name='post_new'),
    path('post/<int:post_id>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:post_id>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:post_id>/comment/',views.add_comment_to_post,name='add_comment_to_post'),

]
