from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
# The loader module is used to load templates from the filesystem.
# It provides a way to load templates by their name or path.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # op=""
    # for q in latest_question_list:
    #     op+=f"{q},"
    # if op=="":
    #     op="No questions available."
    # else:
    #     op=op[:-1]
    # return HttpResponse("latest question list "+op)
    
    template = loader.get_template("polls/index.html") # it looks into templates/polls/ directory for the index.html file.
    context = {"latest_question_list": latest_question_list} 
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
# The render() function is a shortcut that combines loading a template, filling it with context, and returning an HttpResponse object.

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)