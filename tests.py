from main import get_predictions

def no_search_token_in_the_string():
    assert get_predictions("Meme")['status'] == 'error'

def more_than_one_tokens_in_the_string():
    assert get_predictions("Me * me *")['status'] == 'error'

def correct_string():
    assert type(get_predictions("* me")[0]['token_str']) == str

no_search_token_in_the_string()
more_than_one_tokens_in_the_string()
correct_string()
