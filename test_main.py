from main import get_predictions

def test_no_search_token_in_the_string():
    assert get_predictions("Meme")['status'] == 'error'

def test_more_than_one_tokens_in_the_string():
    assert get_predictions("Me * me *")['status'] == 'error'

def test_correct_string():
    assert type(get_predictions("* me")[0]['token_str']) == str
