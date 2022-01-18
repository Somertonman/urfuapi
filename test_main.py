from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_no_search_token_in_the_string():
    response = client.post("/get_suggestions",
        json={"sentence":"Meme"}
    )
    assert response.json()['details'] == 'Masked symbol * not found'

def test_more_than_one_tokens_in_the_string():
    response = client.post("/get_suggestions",
        json={"sentence":"Me * me *"}
    )
    assert response.json()['details'] == 'Masked symbol * found 2 times'

def test_correct_string():
    
    response = client.post("/get_suggestions",
        json={"sentence":"* me"}
    )
    assert response.status_code == 200
    
    assert response.json()['data'][0]['sequence'] == 'tell me'
