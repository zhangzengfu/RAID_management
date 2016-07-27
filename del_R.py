#coding:utf-8
import web
import subprocess
import re

render = web.template.render('templates/')

urls = (
        '','hello',
        '/del','hello',
)

app = web.application(urls,globals())

look = subprocess.Popen("cat /proc/mdstat|grep '^md'|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)
info = look.stdout.read()
list = re.findall('md\d+',info)

class hello:
        def GET(self):
		look = subprocess.Popen("cat /proc/mdstat|grep '^md'|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)
		info = look.stdout.read()
		list = re.findall('md\d+',info)
                return render.delete(list)
	def POST(self):
		f = web.input()
		g = f.get('id')
		h = 'mdadm -S /dev/' + g
		shanchu = subprocess.Popen(h,shell=True,stdout=subprocess.PIPE)
		return render.del_s(g)


