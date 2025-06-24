//************** SPECIF CRUD ********

window.onload=function(){
	//(document.getElementById("inputId")).disabled=true; //if auto_incr
	initListeners(); 
}

function objectFromInput(){
	let code = (document.getElementById("inputId")).value;
	//if(code=="")numero=null;
	
	let name = (document.getElementById("inputName")).value;
	let change = (document.getElementById("inputChange")).value;
	
	document.getElementById("spanMsg").innerHTML="";
	let obj = { code : code,
				name : name,
	            change : parseFloat(change)
	            };
	return obj;
}

function displayObject(obj){
	(document.getElementById("inputId")).value=obj.code;
	(document.getElementById("inputName")).value=obj.name;
	(document.getElementById("inputChange")).value=obj.change;
}

function insertRowCells(row,obj){
	(row.insertCell(0)).innerHTML = obj.code;
	(row.insertCell(1)).innerHTML = obj.name;
	(row.insertCell(2)).innerHTML = obj.change;
}


function blankObject(){
	return {code:"" , name: "" , change : 0 };
}

function getWsBaseUrl(){
	return "../devise-api/v1/devises";
}

//obj = object with values to check
//action = "add" or "update" or ...
function canDoAction(action,obj){
	ok=true; //by default
	if(obj.code==null || obj.code == "")
	  ok=false;
	if(obj.name==null || obj.name == "")
	  ok=false;
	if(obj.change==null)
	  ok=false;
	return ok;
}
