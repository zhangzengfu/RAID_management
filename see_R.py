#coding:utf-8
import web
import subprocess
import re

render = web.template.render('templates/')

urls = (
	'','see',
	'/see','see',
)

app = web.application(urls,globals())

class see:
	def GET(self):
		look = subprocess.Popen("cat /proc/mdstat|grep '^md'|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)
		info = look.stdout.read()
		list = re.findall('md\d+',info)
		return render.see(list)
	def POST(self):
		f = web.input()
		g = f.get('id')
		h = 'mdadm -D /dev/' + g
		chakan = subprocess.Popen(h,shell=True,stdout=subprocess.PIPE)
		see = chakan.stdout.read()
		good = re.findall('.*',see)
		return render.see_s(good)

