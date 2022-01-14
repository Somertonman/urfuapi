from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_no_search_token_in_the_string():
    response = client.post("/get_suggestions/",
        json={"sentence":"Meme"}
    )
    assert response.status_code == 307

def test_more_than_one_tokens_in_the_string():
    response = client.post("/get_suggestions/",
        json={"sentence":"Me * me *"}
    )
    assert response.status_code == 307

def test_correct_string():
    
    response = client.post("/get_suggestions/",
        json={"sentence":"* me""}
    )
    assert response.status_code == 200
    
    assert type(response.json())[0]['token_str']) == str
