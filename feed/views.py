from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import redirect, render, render_to_response
from django.template.loader import render_to_string


@login_required
def feed(request, section, contentTemplate="feed/content/feed_content_PC.html", rmTemplate="feed/rm/feed_rm_PC.html", mainTemplate='feed/feed_PC.html'):

    def GetContext(section):
        context = {}
        if section == 'tan':
            context['note'] = 'Here will be thoughts and news'
        elif section == 't':
            context['note'] = 'Here will be thoughts'
        elif section == 'n':
            context['note'] = 'Here will be news'
        elif section == 'r':
            context['note'] = 'Here will be recommended'
        else:
            raise Http404
        return context

    if request.is_ajax():
        if "HTTP_MORE" in request.META:#load more news in same section
            pass
        else:#we need to return content and right menu
            context = GetContext(section)
            content = render_to_string(contentTemplate, context)
            if request.GET["reqRM"]:#if right menu is required
                rm = render_to_string(rmTemplate, context)
                return JsonResponse({"content":content, "rm":rm})
            return JsonResponse({"content":content})
    else:
        context = GetContext(section)
        context['uniqueURL'] = request.user.uniqueURL
        context['username'] = request.user.username
        return render(request, mainTemplate, context)
