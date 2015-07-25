from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
import urllib
import json
import urllib2
import re

def printLog(text):
	f = open("/data/wumengqiang/mytest/authDemo/githubAuth/log.ini",'w')
	f.write(str(text))
	f.close()
def loginView(request):
	return render(request,'githubAuth/login.html')
def githubCallbackView(request):
	code = request.GET.get('code')
	url ="https://github.com/login/oauth/access_token?client_id=%s&client_secret=%s&code=%s"%(settings.SOCIAL_AUTH_GITHUB_KEY,settings.SOCIAL_AUTH_GITHUB_SECRET,code);
	req = urllib2.urlopen(url)
	html = str(req.read())
	printLog(html)
	if re.match("error",html):
		return render(request, 'githubAuth/login.html') # login again
	elif re.match("access_token",html):
		html = re.split('[=&]',html)
		printLog(html)
		html = html[1]
	printLog(str(html))
	url = "https://api.github.com/user?access_token=%s"%html
	req = urllib2.urlopen(url)
	result = json.load(req)
	printLog(result)
	result = dict(result)
	return render(request,'githubAuth/welcome.html',{"result":result,"type":isinstance(result,dict)})
