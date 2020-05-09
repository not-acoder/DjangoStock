from django.shortcuts import render,redirect
from . models import stonk
from django.contrib import messages
from .forms import StonkForm
from itertools import chain 

def home(request): #pk_05107f1f034f40b591d7e34cf8322e18
	import requests 
	import json 

	if request.method=="POST":
		ticker=request.POST['ticker']
		api_request=requests.get("https://sandbox.iexapis.com/stable/stock/"+ticker+"/quote?token=Tpk_75827c160890477c83384eb6f11f386e")
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api="error.."
		return render(request,'home.html',{'api' : api ,})

	else:
		return render(request,'home.html',{'tchtch' : "enter a stonk ticker", })

	

	

def about(request):
	return render(request,'about.html',{})

def add_stonk(request):
	import requests 
	import json 

	if request.method=="POST":
		form=StonkForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,("stonk added"))
			return redirect('add')
	else:
		ticker=stonk.objects.all()
		output=[]
		for x in ticker:
			api_request=requests.get("https://sandbox.iexapis.com/stable/stock/"+str(x)+"/quote?token=Tpk_75827c160890477c83384eb6f11f386e")
			try:
				api=json.loads(api_request.content)
				output.append(api)
				result=list(chain(output,ticker))
			except Exception as e:
				api="error.."
		return render(request,'add_stonk.html',{'ticker' : ticker , 'output' : output , 'result' : result ,})

def delete(request , stonk_id):
	item=stonk.objects.get(pk=stonk_id)
	item.delete()
	messages.success(request,("Not stonks "))
	return redirect(add_stonk)

