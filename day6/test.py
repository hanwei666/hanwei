import tornado.ioloop
import tornado.web
#pip install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('user')
        p = self.get_argument('pass')
        if u == 'abc' and p == '123':
            self.write('OK')
        else:
            self.write('NO')

    def post(self,*args,**kwargs):
        u = self.get_argument('user')
        p = self.get_argument('pass')
        print(u,p)
        self.write('POST')
application = tornado.web.Application([
    (r"/index",MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()