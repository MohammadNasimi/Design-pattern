
class Friend:
    def __init__(self):
	    self.names = ['amir', 'kevin', 'jack', 'bob']
  
    def __iter__(self):
	    # for i in self.names:
		# 	 yield i
        return iter(self.names)

    def __next__(self):
	    copy_names = self.names
		for name in copy_names:
			return name
		else:
			raise StopIteration
   
fr = Friend()

for i in fr:
    print(i)
    
print( next(fr) )
print( next(fr) )
print( next(fr) )
print( next(fr) )