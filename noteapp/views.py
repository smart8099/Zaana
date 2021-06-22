from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Notes_Form
from .models import Notes
from django.shortcuts import get_object_or_404
def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            print(user)
            auth.login(request,user)
            messages.success(request,f'welcome{user.username} ')
            return redirect('create_note')

        else:
            messages.error(request,"invalid credentials")  
            return redirect('create_note')

    else:

        return render(request,"logins.html")  


def registerpage(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "that username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "that email is already taken")
                    return redirect('register')
                else:
                    new_user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                        email=email, username=username, password=password)
                    messages.success(request,'account created successfully')
                    return redirect('login')



        else:
            # message that passwords don't match
            messages.error(request, messages.ERROR, 'passwords do not match')
            return redirect('register')

        # check user

    else:
        return render(request, 'registration.html')    


#why choose zana
def why_zaana(request):
    return render(request, 'Why.html')


def policy(request):
    return render(request,'policy.html')    

def about(request):
    return render(request,'About.html')    

def password_reset(request):
    if request.method =='POST':

        print(True)
    else:
         return render(request,"Password_reset.html")    



def createnote(request):
    

    if request.method == "GET":
        form = Notes_Form()
        return render(request,'create_notes.html',{"form":form})

    else:
        form = Notes_Form(request.POST)
        print(form.is_valid())
        print(form.errors.as_text)
        
        if form.is_valid():
            obj = form.save(commit = False)

            obj.user = request.user
            print(request.user)
            print(obj.user)
            obj.save()
            form = Notes_Form()
            messages.success(request, "Successfully created")
            messages.success(request,'data added successfully')
            
        else:
            messages.error(request,'there are errors in your form')    
        return redirect('register')

def signout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"Goodbye")
        return redirect('login')    

@login_required
def edit_note(request,id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(Notes, id = id)
  
    # pass the object as instance in form
    form = Notes_Form(request.POST or None, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('view_note')
  
    # add form dictionary to context
    context["form"] = form
  
    return render(request, "update_view.html", context)
   
@login_required
def delete_note(request,id):
    if request.method == 'POST':

        obj = get_object_or_404(Notes, id = id)
        obj.delete()
        return redirect('view_note')
    return render(request,'delete_view.html')
	
@login_required    
def view_notes(request,id):
    print(request)
    
    context = {'Notes':Notes.objects.filter(id=id)}
    return render(request,'view_notes.html',context)
    
@login_required    
def search_note(request):
    search_value = request.POST['search']
    print(search_value)
    context = {"results":Notes.objects.filter(title = search_value)}
    
    return render(request,'note_search.html',context)      



from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def download_note(request,id):
    try:
        note = Notes.objects.get(id = id)     #you can filter using order_id as well
    except:
            return HttpResponse("505 Not Found")
    data = {
        'username':note.user_id,
        'title':note.title,
        'note':note.note,


    }
    pdf = render_to_pdf('notepdf.html', data)

    if pdf:

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Note_%s.pdf" %(data['title'])
        content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
        return HttpResponse("Not found")


@login_required
def quotes(request):
    import random
    if request.user.is_authenticated:
    
    
        quote =[
            "Programmer: A machine that turns coffee into code.",
            'Computers are fast; programmers keep it slow.',
            'When I wrote this code, only God and I understood what I did. Now only God knows',
            'A son asked his father (a programmer) why the sun rises in the east, and sets in the west. His response? It works, don’t touch!',
            'How many programmers does it take to change a light bulb? None, that’s a hardware problem',
            'Programming is like sex: One mistake and you have to support it for the rest of your life',
            'Programming can be fun, and so can cryptography; however, they should not be combined',
            'Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.',
            'Copy-and-Paste was programmed by programmers for programmers actually',
            'Always code as if the person who ends up maintaining your code will be a violent psychopath who knows where you live',
            'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it',
            'Algorithm: Word used by programmers when they don’t want to explain what they did',
            'Software and cathedrals are much the same — first we build them, then we pray',
            'There are two ways to write error-free programs; only the third works',
            'If debugging is the process of removing bugs, then programming must be the process of putting them in',
            '99 little bugs in the code. 99 little bugs in the code. Take one down, patch it around. 127 little bugs in the code',
            'Remember that there is no code faster than no code',
            'No code has zero defects',
            'A good programmer is someone who always looks both ways before crossing a one-way street',
            'Deleted code is debugged code',

        ]    

        ans=random.choice(quote)
        context ={"quote_of_the_day":ans}
        return render(request,'quote.html',context)
    else:
        return redirect('login')    



         