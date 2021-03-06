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

def test_correct_error_min_score():
    
    response = client.post("/get_suggestions",
        json={"sentence":"I * horses", "min_score": 0.7})

    assert response.status_code == 200
    assert response.json()['details'] == 'No results to return. Probably min_score is too high.'
    
def test_correct_error_n_of_results():
    
    response = client.post("/get_suggestions",
        json={"sentence":"Me * me", "n_of_results": 3}
    )
    assert response.status_code == 200
    assert len (response.json()['data']) == 3   
   
def test_correct_error_n_of_results_and_words_only():
    
    response = client.post("/get_suggestions",
        json={"sentence":"I * dog", "n_of_results": 3, "words_only": True}
    )
    assert response.status_code == 200
    assert len (response.json()['data']) == 3 
    assert type(response.json()['data'][0]) == str

    
def test_correct_error_n_of_results_greater_than_five():
    
    response = client.post("/get_suggestions",
        json={"sentence":"I * dog", "n_of_results": 10})
    
    assert response.status_code == 200
    assert response.json()['details'] == 'n_of_results should be a real number in [1,5]'
    
    
def test_correct_error_min_score_wrong_val():
    
    response = client.post("/get_suggestions",
        json={"sentence":"I * dog", "min_score": 10})
    
    assert response.status_code == 200
    assert response.json()['details'] == 'min_score should be a real number in [0,1)'
