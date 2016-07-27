#coding:utf-8
import web
import subprocess
import re

render = web.template.render('templates/')

urls = (
	'','add',
	'/add','add',
	'/add_h','add_h',
)

app = web.application(urls,locals())

class add:
	def GET(self):
		look = subprocess.Popen("cat /proc/mdstat|grep '^md'|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)
                info = look.stdout.read()
                list = re.findall('md\d+',info)
                return render.add(list)
	def POST(self):
                f = web.input()
		global g
                g = f.get('id')
                raise web.seeother('/add_h')
class add_h:
	def GET(self):
		disk = subprocess.Popen("fdisk -l /dev/sdb|grep '^/dev/sdb'|grep 'Linux'|awk '{print $1,$4/1024}'",shell=True,stdout=subprocess.PIPE)
	        info = disk.stdout.read()
        	list1 = re.findall('/dev/sdb\d{1,2}',info)
        	list2 = re.findall('\d+\.\d+',info)
        	disk1 = subprocess.Popen("cat /proc/mdstat|grep 'sdb'",shell=True,stdout=subprocess.PIPE)
        	info1 = disk1.stdout.read()
        	list3 = re.findall('sdb\d{1,2}',info1)
        	for i in list3:
                	li = '/dev/' + i
                	if li in list1:
                        	ln = list1.index(li)
                        	list1.pop(ln)
                        	list2.pop(ln)
                	else:pass
		return render.add_h(list1,list2)
	def POST(self):
		f = web.input()
                g1 = f.get('disk')
                str1 = 'mdadm /dev/' + g + ' -a ' + g1
                da1 = subprocess.Popen(str1,shell=True,stdin=subprocess.PIPE)
                return render.add_s()
