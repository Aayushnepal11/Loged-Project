from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from. forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """ The home page for Learning Log. """
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ Show all topics. """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'title': 'Learning_Logs/Topics',
        'topics': topics, 
        }
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Show a specific data for a topic. """
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    # Restrict the another user to access the data through the url added by the different user.
    if topic.owner != request.user:
        raise Http404
    enrty = topic.entry_set.order_by('-date_added')
    context = {
        'title': topic,
        'topic': topic,
        'entries': enrty,
        }
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Add a new topic. """
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            # Process the form request and save the data.
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect("learning_logs:topics")
    else:
        # Create a blank form
        form = TopicForm()
    # Displaying the form
    context = {
        'title': 'Learning_Logs/Topics',
        'form': form,
        }
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add a new entry for a particular topic. """
    topic = Topic.objects.get(id=topic_id)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            # Process the request when user press submit
            new_entry = form.save(commit=False)
            # Assign the new_enrty.topic to topic i.e. for example java to it's content.
            new_entry.topic = topic
            # Saving the foregin key role of the new_entry with the related_name i.e. entry_set.all().
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        # Create a blank entry form
        form = EntryForm()
    context = {
        'title': 'Learning_Logs/Entries',
        'topic': topic,
        'form': form
        }
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        # Returns the Initial Form with the pre-filled data
        form = EntryForm(instance=entry)
    context = {
        'title': f'Learning_Logs/Update/{entry_id}',
        'topic': topic,
        'entry': entry,
        'form': form
    }
    return render(request, 'learning_logs/edit_entry.html', context)
