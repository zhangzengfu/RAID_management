#coding:utf-8
import web
import cre_R1
import cre_R5
import cre_R6
import cre_R10
import see_R
import del_R
import add_h
import del_h
render = web.template.render('templates/')
urls = (
	'','hello',
	'/hello','hello',
	'/See RAIDS',see_R.app,
	'/Delete RAID',del_R.app,
	'/Create RAID5',cre_R5.app,
	'/Create RAID6',cre_R6.app,
	'/Create RAID10',cre_R10.app,
	'/Create RAID1',cre_R1.app,
	'/Add hot-spare',add_h.app,
	'/Delete hot-spare',del_h.app,
)
app = web.application(urls,globals())

class hello:
	def GET(self):
		return render.create()
	def POST(delf):
		f = web.input()
		g = f.get('id')
		h = '/' + g
		raise web.seeother(h)

if __name__ == "__main__":
	app.run()

















