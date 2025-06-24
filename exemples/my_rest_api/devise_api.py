# HTTPException not from http.client but from fastapi
from fastapi import APIRouter , HTTPException

from devise import Devise, DeviseModel
from devise_service import DeviseService

router = APIRouter(prefix="/devise-api/v1/devises")

#NB: by default fastapi produces JSONResponse so dictionnary or list are automatically
# transform as json string , no need of json.dumps(...., ensure_ascii=False)

@router.get("/{id}" ) #NB method param id should have same name that PathVariable {id}
async def get_devise_by_id(id):
    return DeviseService().getDeviseById(id);

@router.post("/" ,status_code=201 )
async def create_devise(dev : DeviseModel):
    try :
        DeviseService().createDevise(dev);
        return dev;
    except Exception as e:
        raise HTTPException(status_code=409 , detail = str(e))


@router.put("/{id}" )
async def update_devise(id,dev : DeviseModel):
    try:
        dev.code =id;
        DeviseService().updateDevise(dev);
        return dev;
    except Exception as e:
        raise HTTPException(status_code=404 , detail = str(e))


@router.delete("/{id}", status_code=204 )
async def delete_devise(id):
    deletedDevise = DeviseService().deleteDeviseById(id);
    if deletedDevise==None :
        raise HTTPException(status_code=404, detail="no Devise (to Delete) found for key/code="+id)


@router.get("/" )
async def get_devises():
    return DeviseService().getDevises();

    """
    #V1:
    return [{"code": "USD", "name" : "Dollar" , "change" :1},
            {"code": "EUR", "name": "Euro", "change": 1.1} ];
            
    #V2:
    devisesObjects = [Devise('EUR', 'Euro', 1), Devise('USD', 'Dollar', 1.1)];
    return devisesObjects;
    """

    """
       #test singleton
       s1 = DeviseService(); s2= DeviseService();
       if id(s1) == id(s2):
           return  "Singleton works, both variables contain the same instance."
       else:
           return "Singleton failed, variables contain different instances."
    """

