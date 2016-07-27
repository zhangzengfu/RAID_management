#coding:utf-8
import web
import subprocess
import re

render = web.template.render('templates/')

urls = (
        '','cr6'
)

app = web.application(urls,globals())

class cr6:
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

                return render.cre_R6(list1,list2)
        def POST(self):
                f = web.input(disk=[])
                g = f.get('disk')
                h = ' '.join(g)
                lh = h.split()
                a = len(lh)
                b = str(a)
                if f.get('size'):
			j = f.get('size')
			k = int(j)
			l = str(k*1024/(a-2))
			str1 = 'mdadm -C /dev/md3 -l6 -n' + b + ' -z' + l + ' ' + h
                else:
			str1 = 'mdadm -C /dev/md3 -l6 -n' + b + ' ' + h
		mda1 = subprocess.Popen(str1,shell=True,stdin=subprocess.PIPE)
                mda1.communicate('yes')
                return render.cre_s()



