from django.urls import path
from . import views

app_name = "learning_logs"

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all the topics
    path('topics/', views.topics, name='topics'),
    # Details page for a specific topic
    path('topic/<int:topic_id>', views.topic, name='topic'),
    # For adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
