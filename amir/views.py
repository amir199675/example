from django.shortcuts import render
from .forms import *



from rest_framework.views import APIView
from datetime import datetime , timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
import requests
import json
from .serializers import *
from rest_framework.response import Response



# Create your views here.


class BookApiView(APIView):
	def get(self, request, format=None):
		hours = Book.objects.all()
		serializer = Bookserializers(hours, many=True)
		return Response(serializer.data)

class AuthApiView(APIView):
	def get(self, request, format=None):
		authors = Author.objects.all()
		serializer = Authserializers(authors, many=True)
		return Response(serializer.data)


def index(request):
	now = datetime.today()
	how = now + timedelta(days=1)

	one = datetime.strptime('00:30:00', '%H:%M:%S').time()
	ffa =datetime.combine(how,one)

	auth = Author.objects.all()
	data = {'UserApiKey':'578cdf057764feb86880e3d2','SecretKey':'13491375amirelyas'}
	r = requests.post('https://RestFulSms.com/api/Token',data=data)
	amir = json.loads(r.text)
	amir = amir['TokenKey']
	headers = {'x-sms-ir-secure-token':amir}
	r = requests.post(url='https://RestFulSms.com/api/VerificationCode',headers = headers,data={'Code':'13755','MobileNumber':'09157683586'})
	amir = r.text
	return render(request,'index.html',locals())



def saveauthor(request):
	if request.method == 'POST' and 'uform_button' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		user = User(username=username,email=email,password=password)
		user.save()
		profile = Userprofile(user_id_id=username,phone_number=phone_number)
		profile.save()
		return render(request,'index.html',context={})

	else:
		return render(request, 'index.html', context={})