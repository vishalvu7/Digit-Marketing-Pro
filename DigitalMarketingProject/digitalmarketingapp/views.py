from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from digitalmarketingapp.models import UserDetails


# Create your views here.

from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        usernamee = request.POST.get('username')
        passwords= request.POST.get('password')
        user = authenticate(request,username=usernamee, password=passwords)
        
        if user is not None and user.is_superuser:
            # usr = User.objects.get(username=user.username)
            request.session['userid'] = user.id
            
                
            return redirect('home')
        
        elif user is not None and not user.is_superuser:
            
            request.session['newuserid'] = user.id
            request.session['email'] = user.id
            request.session['mobile'] = user.id
            request.session['defaultbalance'] = user.id
            request.session['username'] = user.id
            
            
           
            
            newuser = UserDetails.objects.get(user_id=user.id)
           
            data = {"id":user.id,"email":user.email,"username":user.username,"mobile":newuser.mobiles,"defaultbalance":newuser.defaultbalance}
            return render(request,'user.html',{"data":data})
            
            
        
        else:
            print('not superuser')
            
            return render(request,'login.html')
    
    else:
        if 'userid' in request.session:    
    
            return render(request,'home.html')
        elif 'newuserid' in request.session:
            return render(request,'user.html')
        else:
            return render(request,'login.html')
          
@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def logout_user(request):
    if 'userid' in request.session: 

        del request.session['userid']
        
        return redirect('login')
    elif 'newuserid' in request.session:
        del request.session['newuserid']
        del request.session['email']
        del request.session['mobile']
        del request.session['defaultbalance']
        del request.session['username']
        
        return redirect('login')
    else:
        return redirect('login')


def passwordreset(request):
    if request.method == 'POST':
        username = request.POST['username']
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        
        user = authenticate(request,username=username, password=oldpassword)
        
        if user is not None and user.is_superuser:
            print('Super user')
            user.set_password(newpassword)
            user.save()
            return render(request, 'passwordreset.html',{'msg':"password changed successfully..."})

        
        
        else:
            return render(request, 'passwordreset.html',{'msg':"Invalid user..."})

        return render(request, 'passwordreset.html')
        
        
    return render(request, 'passwordreset.html')

def home(request):
    if request.method == 'POST':
        if 'userid' in request.session:
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            senderid = request.POST.get('senderid')
            
            users = User.objects.create_user(username=name, password=password, email=email)        
            users.save()
            print("my ids is")
            user = User.objects.get(username=name)
            print(user.id)
            
            userDetails = UserDetails(user = user,mobiles=mobile,defaultbalance=0,senderIds=senderid)
            userDetails.save()
            
            
            return render(request,'home.html',{'msg':"User created successfully..."})
        return render(request,'login.html')
        
    else:
        if 'userid' in request.session:
            return render(request,'home.html')
        else:
            return render(request,'login.html')
            
        
    
def whatsappcredit(request):
    if request.method == 'POST':
        if 'userid' in request.session:
        
            email = request.POST.get('email')
            credit = request.POST.get('whatsappcredits')
            
         
            users = User.objects.get(email=email)
            print(users.id)
            
            try:
                my_model = UserDetails.objects.get(user_id=users.id)
                my_model.defaultbalance = credit
                my_model.save()
            except:
                return render(request, 'whatsappcredit.html',{'msg':"User does not exists..."})
            
        
            emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)    
            
            
            return render(request,'whatsappcredit.html',{'users':emails,"msg":"whatsApp balance credited..."})
        else:
            return render(request,'login.html')
        
        
    else:
        if 'userid' in request.session:

            emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
            return render(request,'whatsappcredit.html',{'users':emails})
        else:
            return render(request,'login.html')




def my_iframe_view(request):
    if 'userid' in request.session:
        return render(request, 'iframe.html')
    else:
        return render(request, 'login.html')
        