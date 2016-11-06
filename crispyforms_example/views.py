# -*- coding: utf-8 -*-
from django.shortcuts import render
from crispyforms_example.forms import MessageForm

def crispy_view(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'crispy.html', {'form': MessageForm()})