from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_no_search_token_in_the_string():
    response = client.post("/get_suggestions/",
        json={"Meme"}
    )
    assert response.status_code == 200
    assert response['status'] == 'error'

def test_more_than_one_tokens_in_the_string():
    assert get_predictions("Me * me *")['status'] == 'error'

def test_correct_string():
    assert type(get_predictions("* me")[0]['token_str']) == str
