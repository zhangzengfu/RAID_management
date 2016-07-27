#coding:utf-8
import web
import subprocess
import re

render = web.template.render('templates/')

urls = (
        '','dele',
        '/dele','dele',
        '/dele_h','dele_h',
)

app = web.application(urls,locals())

class dele:
        def GET(self):
                look = subprocess.Popen("cat /proc/mdstat|grep '^md'|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)
                info = look.stdout.read()
                list = re.findall('md\d+',info)
                return render.dele(list)
	def POST(self):
                f = web.input()
                global g
                g = f.get('id')
                raise web.seeother('/dele_h')
class dele_h:
	def GET(self):
		lujing = 'mdadm -D /dev/' + g + "|grep '/dev/sd'|grep 'spare'"
		disk = subprocess.Popen(lujing,shell=True,stdout=subprocess.PIPE)
		info = disk.stdout.read()
		list = re.findall('/dev/sdb\d{1,2}',info)
		return render.del_h(list)
	def POST(self):
		f = web.input()
		g1 = f.get('disk')
		str1 = 'mdadm /dev/' + g + ' -f ' + g1
		str2 = 'mdadm /dev/' + g + ' -r ' + g1
		faulty = subprocess.Popen(str1,shell=True,stdout=subprocess.PIPE)
		delete = subprocess.Popen(str2,shell=True,stdout=subprocess.PIPE)
		return render.dele_s()





