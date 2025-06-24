
class Devise(object) :
#constructeur avec valeurs par défaut:
	def __init__(self,code=None,name=None,change=0) :
		self.code=code
		self.name=name
		self.change=change


from pydantic import BaseModel

class DeviseModel(BaseModel):
    code: str
    name: str
    change: float
