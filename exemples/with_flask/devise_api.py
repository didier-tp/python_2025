
from flask  import Flask , jsonify , abort , request
app = Flask(__name__)

from devise import Devise
from devise_service import DeviseService

api_prefix="/devise-api/v1/devises" #default sever url in dev mode: http://localhost:5000

#NB: by default flask and fastapi produces JSONResponse so dictionnary or list of dictionary are automatically
# transform as json string , no need of json.dumps(...., ensure_ascii=False) or falsk.jsonify()

# util function for convertir data object to dictionary 
def asJsonSerializableDict(objOrCol):
    #print("type=",type(objOrCol))
    if isinstance(objOrCol,(list,tuple)):
        return [ obj.__dict__ for obj in objOrCol ]
    else: 
        return objOrCol.__dict__
    
def asDict(objOrCol): # shorter function name for frequent calls
    return asJsonSerializableDict(objOrCol) 

@app.get(f"{api_prefix}/<id>" ) #NB method param id should have same name that PathVariable <id>
def get_devise_by_id(id):
    try:
        print("(get_devise_by_id() call with id=" , id)
        return asDict(DeviseService().getDeviseById(id))
    except Exception as e:
        abort(404,f"Devise not found for id={id}")


@app.post(f"{api_prefix}" )
def create_devise():
    try :
        data = request.get_json() # (as dict if possible) from POST request body
        #print("jsonData received(as disct) in post mode",data)
        dev=Devise(data['code'],data['name'],data['change'])
        #print("devise received in post mode",dev)
        DeviseService().createDevise(dev)
        #return asDict(dev) # with default status code = 200/OK
        return asDict(dev) , 201 # with specific status code = 201/CREATED
    except Exception as e:
        abort(409,str(e))


@app.put(f"{api_prefix}/<id>" )
def update_devise(id):
    try:
        data = request.get_json() # (as dict if possible) from PUT request body
        #print("jsonData received(as disct) in put mode",data)
        dev=Devise(data['code'],data['name'],data['change'])
        #print("devise received in put mode",dev)
        dev.code =id
        DeviseService().updateDevise(dev)
        return asDict(dev) # with default status code = 200/OK
    except Exception as e:
         abort(404,str(e))


@app.delete(f"{api_prefix}/<id>" ) 
def delete_devise(id):
    deletedDevise = DeviseService().deleteDeviseById(id)
    if deletedDevise==None :
        abort(404,f"no Devise (to Delete) found for key/code=={id}")
    else:
        #return "devise was sucessfully deleted" # with default status code = 200/OK
        return '', 204 # with specific status code = 204/NO_CONTENT


@app.get(f"{api_prefix}/" )
def get_devises():
    return asDict(DeviseService().getDevises()) #will be automatically JSON serializd by jsonify() of flask

    #default flask behavior : 
    # if return resAsDict or resAsCollectionOfDict 
    # automatic return  jsonify(resAsDict)

    '''
    #V1:
    return [{"code": "USD", "name" : "Dollar" , "change" :1},
            {"code": "EUR", "name": "Euro", "change": 1.1} ]
    '''
    
    """
    #V2:
    devisesObjects = [Devise('EUR', 'Euro', 1), Devise('USD', 'Dollar', 1.1)]
    devisesObjectsAsDicts = [ d.__dict__ for d in devisesObjects ] 
    print("devisesObjectsAsDicts=",devisesObjectsAsDicts)
    devisesObjectsAsDicts = asJsonSerializableDict(Devise('GBP','Livre',0.99))
    print("devisesObjectsAsDicts=",devisesObjectsAsDicts)
    devisesObjectsAsDicts = asJsonSerializableDict([Devise('EUR', 'Euro', 1), Devise('USD', 'Dollar', 1.1), Devise('JPY','Yen',112.0)])
    print("devisesObjectsAsDicts=",devisesObjectsAsDicts)
    return devisesObjectsAsDicts
    """

    """
       #test singleton
       s1 = DeviseService(); s2= DeviseService();
       if id(s1) == id(s2):
           return  "Singleton works, both variables contain the same instance."
       else:
           return "Singleton failed, variables contain different instances."
    """

