import abc


class AbastractHandler(abc.ABC):
    @abc.abstractmethod
    def set_next(self,handler):
        pass
    
    @abc.abstractmethod
    def handler(self,request):
        pass
    
    
class BaseHandler(AbastractHandler):
    _set_handler = None
    def set_next(self, handler):
        self._set_handler = handler
        return handler
    
    def handler(self, request):
        if self._set_handler:
            return self._set_handler.handler(request)
        return None
    
class HandlerOne(BaseHandler):
    def handler(self, request):
        if 0<= request <=10:
            print(f'handlerone is processing this request {request}')
        else:
            return super().handler(request)
        
        
class HandlerTwo(BaseHandler):
    def handler(self, request):
        if 10<= request <=20:
            print(f'handlertwo is processing this request {request}')
        else:
            return super().handler(request)
            
            
class DefaultHandler(BaseHandler):
    def handler(self, request):
            print(f'handler defualt is processing this request {request}')
            
            
def client(handle,request):
    for num in request:
        handle.handler(num)

num = [3,14,31,9]

h_one = HandlerOne()
h_two = HandlerTwo()
h_d = DefaultHandler()

h_one.set_next(h_two).set_next(h_d)
client(h_one,num)
