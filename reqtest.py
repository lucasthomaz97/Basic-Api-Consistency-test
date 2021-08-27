from requests import get
import pytest
import json

NAME = 'name'

def make_request(item, nome):
    r = get("https://zelda-api.apius.cc/api/"+item+"?name="+str(nome))
    qdata = json.loads(r.text)
    response = qdata.get('data') 
    return qdata, response

@pytest.mark.parametrize("item,nome",[("games","Zelda"),("staff","Shigeru")])
def test_validate_return(item, nome):
    qdata, response = make_request(item, nome)
        
    if qdata.get('success') == False:
        pytest.fail("Falha na Requisição"+ str(qdata))
    
    if qdata.get('count') > 0:
        for i in response:
            if nome not in i.get(NAME):
                pytest.fail('Dados inconsistentes: '+NAME+':'+i.get(NAME)+'\n Retorno esperado: '+item+':'+nome+' ')
    else:
        pytest.fail("Nenhum resultado retornado"+ str(qdata))

def test_the_test(item, nome):
    qdata, response = make_request(item, nome)
    print(response, type(response))