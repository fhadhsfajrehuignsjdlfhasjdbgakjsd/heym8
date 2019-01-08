import uuid

from . import choices
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import redirect, render, render_to_response
from django.template.loader import render_to_string

from decorators import ajax_login_required
from HeyM8.settings import EMAIL_HOST_USER, SERVER_NAME

from . import forms, models

letter = '''Click here to confirm ->{}/users/confirm/{}. 
Link will become invalid in two days. 
If you didn't sign up for HeyM8, just ignore this message.'''#message to senf in email 


def SignInAndUp(request):
    if request.user.is_authenticated:
        return redirect("feed:feed", "tan")
    status = "right"
    signInNotice = ""
    signUpNotice = ""
    if request.is_ajax() and request.method == "POST":#if one of forms was sent to the server
        if request.META["HTTP_FORMNAME"] == "signInForm":#if sign in form was sent
            signInForm = forms.SignInForm(request.POST)
            if signInForm.is_valid():#check if form has no errors
                user = authenticate(email=signInForm.cleaned_data["Email"], password=signInForm.cleaned_data["Password"])
                if user is None:
                    status = "wrong"
                    signInNotice = "Wrong email or password."
                else:#if user with such email exists
                    if user.isDeleted:#if user has deleted his account
                        status = 'deleted'
                    if user.isBanned:
                        pass#tell he was banned
                    else:#if user exists, undeleted, unbanned and confirmed email
                        login(request, user)
                        if not signInForm.cleaned_data["RememberMe"]:
                            request.session.set_expiry(0)
                        signInNotice = '/'
            else:
                status = "wrong"
                signInNotice = "Input valid email."
        elif request.META["HTTP_FORMNAME"] == "signUpForm":#sign up form was sent
            signUpForm = forms.SignUpForm(request.POST)
            if signUpForm.is_valid():#check if form has no errors
                if models.User.objects.filter(email=signUpForm.cleaned_data["email"]).exists():#if user with such email was created(email could be uncorfimed)
                    user = models.User.objects.get(email=signUpForm.cleaned_data["email"])
                    if user.is_active:#if user with such email already exists
                        status = "wrong"
                        signUpNotice = "This email is already bound to account."
                    else:#if email wasn't confirmed
                        user.statistic_Info.confirmationKey = uuid.uuid4()
                        user.statistic_Info.save()
                        user.set_password(signUpForm.cleaned_data["password"])
                        user.username = signUpForm.cleaned_data["username"]
                        user.save()
                        user.email_user("HeyM8 confirmation letter.", letter.format(SERVER_NAME, user.statistic_Info.confirmationKey), EMAIL_HOST_USER)
                        status = "check mail"
                        signUpNotice = "Uou are registered! Check your mail to confirm your HeyM8 account)"
                else:#create new user
                    user = models.User.objects.create_user(username=signUpForm.cleaned_data["username"], 
                    email=signUpForm.cleaned_data["email"], password=signUpForm.cleaned_data["password"], 
                    is_active=False)
                    statisticInfo = models.StatisticInfo.objects.create(user=user, 
                    confirmationKey=uuid.uuid4(), isActive=False)
                    user.email_user("HeyM8 confirmation letter.", letter.format(SERVER_NAME, user.statistic_Info.confirmationKey), EMAIL_HOST_USER)
                    status = "check mail"
                    signUpNotice = "You are registered! Check your mail to confirm your HeyM8 account)"
            else:
                status = "wrong"
                signUpNotice = "Input valid email or valid username (username may contain only letters, digits and _.-+@)"
        return JsonResponse({"signUpNotice":signUpNotice, "status":status, "signInNotice":signInNotice,})
    else:#just render empty forms
        signInForm = forms.SignInForm()
        signUpForm = forms.SignUpForm()
        return render(request, 'users/signInAndUp_PC.html', 
        {'signInForm':forms.SignInForm(), 'signUpForm':forms.SignUpForm()})


def Logout(request):
    if request.user.is_authenticated:
        logout(request)        
    return redirect('/')


def ConfirmEmail(request, confirmationKey):#/users/confirm/{{confirmationKey}}
    #confirm user's email
    try:
        statisticInfo = models.StatisticInfo.objects.get(confirmationKey=confirmationKey)
    except ObjectDoesNotExist:#if no email with this confirmationKey was sent
        raise Http404()
    user = statisticInfo.user
    login(request, user)  
    user.uniqueURL = user.id
    user.is_active, statisticInfo.isActive = True, True #confirm email
    statisticInfo.confirmationKey = None
    personalInfo = models.PersonalInfo.objects.create(user=user)
    userSettings = models.UserSettings.objects.create(user=user)
    userBreakingHistory = models.UserBreakingHistory.objects.create(user=user)
    commonAlbum = models.UserAlbum.objects.create(name='Common', description="All pictures", custom=False, user=user)
    thoughtAlbum = models.UserAlbum.objects.create(name='Thoughts', description="Thoughts' pictures", custom=False, user=user)

    
    commonAlbum.save()
    thoughtAlbum.save()
    personalInfo.save()
    userSettings.save()
    userBreakingHistory.save()
    statisticInfo.save()
    user.save()
    return redirect("users:intro")


@ajax_login_required
@login_required
def Intro(request, mainTemplate='users/intro_PC.html'):#/users/intro
    #introduce service to user
    return render(request, mainTemplate)


#how many albums to upload for one request
nOfAlbumsToUpload = 25#const
@ajax_login_required
@login_required
def UserPage(request, uniqueURL, contentTemplate='users/content/user_Page_content_PC.html', rmTemplate='users/rm/user_Page_rm_PC.html', mainTemplate='users/user_Page_PC.html'):#/users/{{uniqueURL}}

    def GetContext(request, uniqueURL):
        context = {}
        context['uniqueURL'] = request.user.uniqueURL
        context['username'] = request.user.username
        context['status'] = request.user.personal_Info.status
        context['gender'] = request.user.personal_Info.gender
        context['mainPicture'] = request.user.settings.mainPicture.url if request.user.settings.mainPicture else '' 
        context['owner'] = request.user.uniqueURL == uniqueURL
        if not context['owner']:
            context['allowedToSeePics'] = True
        else:
            context['allowedToSeePics'] = request.user.settings.whoCanSeeMyAlbums == "all"
        context['albums'] = request.user.albums.values_list('name', 'description', 'mainPicture', 'id', 'custom')[:nOfAlbumsToUpload] if context['allowedToSeePics'] else None
        return context

    context = GetContext(request, uniqueURL)
    if request.is_ajax():#return data as Json
        content = render_to_string(contentTemplate, context, request=request)
        if request.GET["reqRM"]:
            rm = render_to_string(rmTemplate, context)
            return JsonResponse({"content":content, "rm":rm})
        return JsonResponse({"content":content})
    else:#just render page
        return render(request, mainTemplate, context)


@ajax_login_required
@login_required
def EditStatus(request):
    if request.method =="POST" and request.is_ajax():# upload new status
        request.user.personal_Info.status = request.POST["status"]
        request.user.personal_Info.save()
        if request.POST["status"] == "":
            newStatus = "Nothing yet"
        else:
            newStatus = request.POST["status"]
        return JsonResponse({"newStatus":newStatus})
    else:#raise not found
        raise Http404


@ajax_login_required
@login_required
def NewThought(request):
    if request.method =="POST" and request.is_ajax():#if new thought was sent
        
        return JsonResponse({})
    else:#raise not found
        raise Http404


@ajax_login_required
@login_required
def GetPictures(request):
    if request.method =="POST" and request.is_ajax():# upload new status
        
        return JsonResponse({})
    else:#raise not found
        raise Http404


@ajax_login_required
@login_required
def Settings(request, section, contentTemplate="users/content/settings_content_PC.html", rmTemplate="users/rm/settings_rm_PC.html", mainTemplate='users/settings_PC.html'):#/users/settings

    def GetContext(section):
        context = {}
        context['uniqueURL'] = request.user.uniqueURL
        context['section'] = section
        if section == "pi":
            context['currentUsername'] = request.user.username
            context['genders'] = choices.GENDERS
            context['currentGender'] = request.user.personal_Info.gender
            context['languages'] = choices.LANGUAGES
            context['currentLanguages'] = request.user.personal_Info.languages
            context['currentDob'] = str(request.user.personal_Info.dob)
        elif section == "i":
            pass
        elif section == 'p':
            pass
        elif section == 'e':
            pass
        return context

    if request.method == "POST" and request.is_ajax():#save changes
        JSONContext = {}
        if section == "pi":
            user = request.user
            if (request.POST["username"]) and (user.username != request.POST["username"]):
                request.user.username = request.POST["username"]
            if ("deleteProfilesDob" in request.POST) and (request.POST["deleteProfilesDob"]):
                request.user.personal_Info.dob = None
            elif (request.POST["dob"]) and (user.personal_Info.dob != request.POST["dob"]):
                request.user.personal_Info.dob = request.POST["dob"]
                JSONContext['showDeleteProfilesDob'] = True
            if (request.POST["gender"]) and (user.personal_Info.gender != request.POST["gender"]):
                request.user.personal_Info.gender = request.POST["gender"]
            if (request.POST.getlist("languages")) and (user.personal_Info.languages != request.POST.getlist("languages")):
                request.user.personal_Info.languages = request.POST.getlist("languages")
            user.save()
            user.personal_Info.save()
            JSONContext["message"] = "Changes applied)"
        elif section == "i":
            pass
        elif section == 'p':
            pass
        elif section == 'e':
            pass
        return JsonResponse(JSONContext)

    context = GetContext(section)
    if request.method == "GET" and request.is_ajax():#return necessary html
        content = render_to_string(contentTemplate, context, request=request)
        if request.GET["reqRM"]:
            rm = render_to_string(rmTemplate, context)
            return JsonResponse({"content":content, "rm":rm, })
        return JsonResponse({"content":content})
    else:#render forms
        return render(request, mainTemplate, context)


def AlbumPictures(request, albumID, mainTemplate="base/album_Pictures_PC.html"):#albim pics are always opened in new tab
    context = {}
    album = models.UserAlbum.objects.get(id=albumID)
    context['owner'] = request.user == album.user
    context['pictures'] = album.pictures.order_by('uploadTime')
    context['uniqueURL'] = request.user.uniqueURL
    return render(request, mainTemplate, context)
