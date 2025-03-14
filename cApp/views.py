from django.shortcuts import render, redirect, HttpResponse # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import * # type: ignore
from django.db.models import Q # type: ignore
# Create your views here.
def index(request):
    return render(request, "index.html")

def userReg(request):
    msg = ''
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cPassword = request.POST['cPassword']
        state = request.POST['state']
        department = request.POST['department']
        designation = request.POST['designation']
        building_name = request.POST['building_name']
        street = request.POST['street']
        city = request.POST['city']
        pincode = request.POST['pincode']
        district = request.POST['district']
        if password == cPassword:
            if User.objects.filter(username=email).exists():
                msg = "Username already exists"
            else:
                user = User.objects.create_user(
                    username=email, password=password,is_active=0)
                customer = Users.objects.create(name=name, 
                                                email=email,
                                                phone=phone,
                                                user=user,
                                                state=state,
                                                department=department,
                                                designation=designation,
                                                building_name=building_name,
                                                street=street,
                                                city=city,
                                                pincode=pincode,
                                                district=district)
                user.save()
                customer.save()
                msg = "Registration successful"
        else:
            msg = "Password dosen't match"
    return render(request, "userReg.html", {"msg": msg})

def login(request):
    msg = ""
    if (request.POST):
        email = request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                return redirect("/adminHome")
            else:
                data = Users.objects.get(email=email)
                request.session['uid'] = data.id
                return redirect('/userHome')
        else:
            msg = "Invalid Credentials"
    return render(request, "login.html", {"msg": msg})


def adminHome(request):
    return render(request, "adminHome.html")

def adminUsers(request):
    data = Users.objects.filter(user__is_active=1)
    dataIn = Users.objects.filter(user__is_active=0)
    return render(request, "adminUsers.html", {"data": data,"dataIn": dataIn})

def adminUpdateUsers(request):
    id = request.GET["id"]
    status = request.GET["status"]
    cat = User.objects.get(id=id)
    cat.is_active = status
    cat.save()
    return redirect("/adminUsers")

def adminAnalysis(request):
    from .analysis2 import main
    for_f1 = ''
    for_f2 = ''
    crime = ''
    error = ''
    if request.POST:
        crime = request.POST["crime"]
        try:
            f1, f2 = main(crime)
            for_f1 = Analysis.objects.create(details=f'Year Wise Report of {crime} Cases')
            for_f2 = Analysis.objects.create(details=f'All India Wise Report of {crime} Cases')
            with open(f1, 'rb') as f:
                for_f1.img.save(f1, f, save=True)
            with open(f2, 'rb') as f:
                for_f2.img.save(f2, f, save=True)
            for_f1.save()
            for_f2.save()
        except:
            error = 'Data Not Found'
    return render(request, "adminAnalysis.html", {"f1":for_f1,"f2":for_f2, "crime":crime, "error":error})

def adminAnalysisState(request):
    from .analysis2 import state_main
    for_f1 = ''
    crime = ''
    state = ''
    error = ''
    if request.POST:
        crime = request.POST["crime"]
        state = request.POST["state"]
        try:
            f1 = state_main(crime,state)
            for_f1 = Analysis.objects.create(details=f'Year Wise Report of {crime} Cases')
            with open(f1, 'rb') as f:
                for_f1.img.save(f1, f, save=True)
            for_f1.save()
        except:
            error = 'Data Not Found'

    return render(request, "adminAnalysisState.html", {"f1":for_f1, "crime":crime, "error":error,"state":state})

# def adminAnalysis(request):
#     from .analysis import main_rape, for_state_rape, main_murder, for_state_murder, main_police_hr, for_state_police
#     f1,f2,f3 = main_rape()
#     for_f1 = Analysis.objects.create(details='Year Wise Violence Against Women Report')
#     for_f2 = Analysis.objects.create(details='All India Violence Against Women Report')
#     for_f3 = Analysis.objects.create(details='Age Wise Violence Against Women Report')
#     with open(f1, 'rb') as f:
#         for_f1.img.save(f1, f, save=True)
#     with open(f2, 'rb') as f:
#         for_f2.img.save(f2, f, save=True)
#     with open(f3, 'rb') as f:
#         for_f3.img.save(f3, f, save=True)
#     for_f1.save()
#     for_f2.save()
#     for_f3.save()

#     m1,m2,m3,m4 = main_murder()
#     for_m1 = Analysis.objects.create(details='Year Wise Murder Cases Report')
#     for_m2 = Analysis.objects.create(details='All India Murder Cases Report')
#     for_m3 = Analysis.objects.create(details='Age Murder Cases Report')
#     for_m4 = Analysis.objects.create(details='Gender Murder Cases Report')
#     with open(m1, 'rb') as f:
#         for_m1.img.save(m1, f, save=True)
#     with open(m2, 'rb') as f:
#         for_m2.img.save(m2, f, save=True)
#     with open(m3, 'rb') as f:
#         for_m3.img.save(m3, f, save=True)
#     with open(m4, 'rb') as f:
#         for_m4.img.save(m4, f, save=True)
#     for_m1.save()
#     for_m2.save()
#     for_m3.save()
#     for_m4.save()

#     p1,p2,p3 = main_police_hr()
#     for_p1 = Analysis.objects.create(details='Year Wise Human Rights Violations Caes Report')
#     for_p2 = Analysis.objects.create(details='All India Human Rights Violations Report')
#     for_p3 = Analysis.objects.create(details='Category Wise Human Rights Violations Report')
#     with open(p1, 'rb') as f:
#         for_p1.img.save(p1, f, save=True)
#     with open(p2, 'rb') as f:
#         for_p2.img.save(p2, f, save=True)
#     with open(p3, 'rb') as f:
#         for_p3.img.save(p3, f, save=True)
#     for_p1.save()
#     for_p2.save()
#     for_p3.save()
#     return render(request, "adminAnalysis.html", {"f1":for_f1,"f2":for_f2, "f3":for_f3, "m1":for_m1,"m2":for_m2, "m3":for_m3, "m4":for_m4,"p1":for_p1,"p2":for_p2, "p3":for_p3})

# def adminAnalysisState(request):
#     from .analysis import main_rape, for_state_rape, main_murder, for_state_murder, main_police_hr, for_state_police
#     for_p1 = ''
#     for_p2 = ''
#     for_p3 = ''
#     for_f1 = ''
#     for_f2 = ''
#     for_m1 = ''
#     for_m2 = ''
#     for_m3 = ''
#     for_m4 = ''

#     if request.POST:
#         state = request.POST['state']
#         crime = request.POST['crime']
#         print("================================================================================")
#         print(crime)
#         print(state)
#         print("================================================================================")
#         try:
#             if crime == 'Violence Against Women':
#                 f1, f2 = for_state_rape(state)
#                 print("----------------------------------------------------------------")
#                 print(f1,f2)
#                 print("----------------------------------------------------------------")
#                 for_f1 = Analysis.objects.create(details=f'Year Wise Violence Against Women Report @ {state}')
#                 for_f2 = Analysis.objects.create(details=f'Age Wise Violence Against Women Report @ {state}')
#                 with open(f1, 'rb') as f:
#                     for_f1.img.save(f1, f, save=True)
#                 with open(f2, 'rb') as f:
#                     for_f2.img.save(f2, f, save=True)
#                 for_f1.save()
#                 for_f2.save()
#                 return render(request, "adminAnalysisState.html", {"f1":for_f1, "f2":for_f2,"case":crime,"state":state})
#             elif crime == 'Murder Case':
#                 f1, f2, f3 = for_state_murder(state)
#                 print("----------------------------------------------------------------")
#                 print(f1,f2)
#                 print("----------------------------------------------------------------")
#                 for_f1 = Analysis.objects.create(details=f'Year Wise Violence Against Women Report @ {state}')
#                 for_f2 = Analysis.objects.create(details=f'Age Wise Violence Against Women Report @ {state}')
#                 for_f3 = Analysis.objects.create(details=f'Gender Wise Violence Against Women Report @ {state}')
#                 with open(f1, 'rb') as f:
#                     for_f1.img.save(f1, f, save=True)
#                 with open(f2, 'rb') as f:
#                     for_f2.img.save(f2, f, save=True)
#                 with open(f3, 'rb') as f:
#                     for_f3.img.save(f3, f, save=True)
#                 for_f1.save()
#                 for_f2.save()
#                 for_f3.save()
#                 return render(request, "adminAnalysisState.html", {"f1":for_f1, "f2":for_f2, "f3":for_f3, "case":crime,"state":state})
#             elif crime == 'Human Rights Violations By Police':
#                 f1, f2 = for_state_police(state)
#                 print("----------------------------------------------------------------")
#                 print(f1,f2)
#                 print("----------------------------------------------------------------")
#                 for_f1 = Analysis.objects.create(details=f'Year Wise Human Rights Violations By Police Report @ {state}')
#                 for_f2 = Analysis.objects.create(details=f'Category Wise Human Rights Violations By Police Report @ {state}')
#                 with open(f1, 'rb') as f:
#                     for_f1.img.save(f1, f, save=True)
#                 with open(f2, 'rb') as f:
#                     for_f2.img.save(f2, f, save=True)
#                 for_f1.save()
#                 for_f2.save()
#                 return render(request, "adminAnalysisState.html", {"f1":for_f1, "f2":for_f2, "case":crime,"state":state})
#         except:
#             return render(request, "adminAnalysisState.html", {"error":"No Data Found"})

#     return render(request, "adminAnalysisState.html")



def udp(request):
    ChatAdmin.objects.all().delete()
    return redirect("/adminHome")



def adminPrediction(request):
    from .prediction2 import main, state_main
    error = ''
    result = ''
    crime_list = ''
    con = ''
    if request.POST:
        state = request.POST['state']
        crime = request.POST['crime']
        year = int(request.POST['year'])
        try:
            if state == 'All':
                result, crime_list = main(crime,year)
                # crime_list = list(crime_list)
                crime_list = crime_list.values.tolist()
                print(crime_list)
            else:
                result, crime_list = state_main(state,crime,year)
                # crime_list = list(crime_list)
                print("////////////////////////////////")
                crime_list = crime_list.values.tolist()
                print(type(crime_list))
            for_res = result.split(":")
            for_res = for_res[-1]
            for_res = int(for_res)
            print(for_res)
            last_one = crime_list[-1]
            count_last_one = int(last_one[-1])
            count_result = int(for_res)
            if count_result > count_last_one:
                con = "Crime rate will increase"
            else:
                con = "Crime rate will decrease"
        except:
            error = "Data Not Found"
    return render(request, "adminPrediction.html", {"error":error, "result":result,"crime_list":crime_list, "con":con})

def adminchats(request):
    ops = Users.objects.filter(user__is_active=1)
    return render(request, "adminchats.html", {"ops":ops})

def adminChat(request):
    uid = request.GET["id"]
    url = request.GET['url']
    us = Users.objects.get(id=uid)
    if request.method == "POST":
        msg = request.POST['msg']
        db = ChatAdmin.objects.create(users=us, message=msg, sender='Admin')
        db.save()
    messages = ChatAdmin.objects.filter(users__id=uid)
    return render(request, "adminChat.html", {"messages":messages, "url":url})

def adminCrime(request):
    data = CrimeFiles.objects.exclude(users=None)
    return render(request, "adminCrime.html", {"data": data})


def userHome(request):
    uid = request.session['uid']
    user = Users.objects.get(id=uid)
    request.session['state'] = user.state
    return render(request, "userHome.html", {"user": user})

def userAnalysis(request):
    uid = request.session['uid']
    user = Users.objects.get(id=uid)
    state = user.state
    from .analysis2 import state_main

    for_f1 = ''
    crime = ''
    error = ''


    if request.POST:
        crime = request.POST['crime']
        print("================================================================================")
        print(crime)
        print("================================================================================")
        try:
            f1 = state_main(crime,state)
            for_f1 = Analysis.objects.create(details=f'Year Wise Report of {crime} Cases')
            with open(f1, 'rb') as f:
                for_f1.img.save(f1, f, save=True)
            for_f1.save()
        except:
            error = 'Data Not Found'

    return render(request, "userAnalysis.html", {"f1":for_f1, "crime":crime, "error":error,"state":state})

def userPrediction(request):
    from .prediction2 import main, state_main
    error = ''
    result = ''
    crime_list = ''
    con = ''
    state = request.session['state']
    if request.POST:
        crime = request.POST['crime']
        year = int(request.POST['year'])
        try:
            result, crime_list = state_main(state,crime,year)
            crime_list = crime_list.values.tolist()
            print(type(crime_list))

            for_res = result.split(":")
            for_res = for_res[-1]
            for_res = int(for_res)
            print(for_res)
            last_one = crime_list[-1]
            count_last_one = int(last_one[-1])
            count_result = int(for_res)
            if count_result > count_last_one:
                con = "Crime rate will increase"
            else:
                con = "Crime rate will decrease"
        except:
            error = "Data Not Found"
    return render(request, "userPrediction.html", {"error":error, "result":result,"crime_list":crime_list, "con":con})


def useradminchat(request):
    uid = request.session["uid"]
    url = 'userHome'
    us = Users.objects.get(id=uid)
    if request.method == "POST":
        msg = request.POST['msg']
        db = ChatAdmin.objects.create(users=us, message=msg, sender='Users')
        db.save()
    messages = ChatAdmin.objects.filter(users=us)
    return render(request, "useradminchat.html", {"messages":messages, "url":url})

def UserIndiaAnalysis(request):
    from .analysis2 import main
    for_f1 = ''
    for_f2 = ''
    crime = ''
    if request.POST:
        crime = request.POST["crime"]
        f1, f2 = main(crime)
        for_f1 = Analysis.objects.create(details=f'Year Wise Report of {crime} Cases')
        for_f2 = Analysis.objects.create(details=f'All India Wise Report of {crime} Cases')
        with open(f1, 'rb') as f:
            for_f1.img.save(f1, f, save=True)
        with open(f2, 'rb') as f:
            for_f2.img.save(f2, f, save=True)
        for_f1.save()
        for_f2.save()
    return render(request, "UserIndiaAnalysis.html", {"f1":for_f1,"f2":for_f2, "crime":crime})

def userAddCrime(request):
    uid = request.session["uid"]
    us = Users.objects.get(id=uid)
    msg = ''
    if request.POST:
        crimeno = request.POST['crimeno']
        date_reported = request.POST['date_reported']
        crimetype = request.POST['crimetype']
        location = request.POST['location']
        district = request.POST['district']
        state = request.session['state']
        description = request.POST['description']
        report = request.FILES['report']
        data = CrimeFiles.objects.create(date_reported=date_reported,crimetype=crimetype,location=location,district=district,state=state,description=description,report=report,users=us,crimeno=crimeno)
        data.save()
        msg = "Crime details added"
    return render(request, "userAddCrime.html", {"msg":msg})

def userViewCrime(request):
    uid = request.session["uid"]
    data = CrimeFiles.objects.filter(users=uid)
    if request.POST:
        search = request.POST['search']
        data = CrimeFiles.objects.filter(Q(users=uid) & Q(Q(crimeno=search) | Q(crimetype__contains=search) | Q(location__contains=search) | Q(district__contains=search) | Q(state__contains=search) | Q(description__contains=search)))

    return render(request, "userViewCrime.html", {"data": data})

def userUpdateCrimeFile(request):
    id = request.GET['id']
    data = CrimeFiles.objects.get(id=id)
    if request.POST:
        crimetype = request.POST['crimetype']
        location = request.POST['location']
        district = request.POST['district']
        state = request.session['state']
        description = request.POST['description']
        report = request.FILES['report']
        data.crimetype = crimetype
        data.location = location
        data.district = district
        data.state = state
        data.description = description
        data.report = report
        data.save()
        return redirect("/userViewCrime")
    return render(request, "userUpdateCrimeFile.html", {"data": data})






























