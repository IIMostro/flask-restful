from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

server = app.create_app()
http_server = HTTPServer(WSGIContainer(server))
http_server.listen(3456)  #flask默认的端口
IOLoop.instance().start()