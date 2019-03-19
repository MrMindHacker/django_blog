source venv/bin/activate && cd django_project && python manage.py runserver


"""
#views.py....................
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

#registers.hrml.......................
{% extends "blog/base.html"%}

{% block content %}
    <div class="content-section">
        <form method="post">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4"> Join Today </legend>
                {{ form }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outlline-info" type="submit">Sign Up</button>
            </div>
        </form>
        <div class="form-group">
            <small class="text-muted">
                Already Have An Account? <a class="ml-2" href="#">Sign In</a>
            </small>
        </div>
    </div>
{% endblock %}
"""
