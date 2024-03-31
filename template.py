import abc 

class Top(abc.ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()
        
    def first_common(self):
        print('this is first common')
    def second_common(self):
        print('this is second common')

    @abc.abstractmethod
    def third_require(self):
        pass
    @abc.abstractmethod
    def fourth_require(self):
        pass
    
    
class One(Top):
    def third_require(self):
        print('this is third  require from to  One')

    def fourth_require(self):
        print('this is fourth  require from to One')


class Two(Top):
    def third_require(self):
        print('this is third  require from to Two')

    def fourth_require(self):
        print('this is fourth  require from to Two')
        
        

def client(get_class):
    get_class.template_method()
    
client(Two())
        
