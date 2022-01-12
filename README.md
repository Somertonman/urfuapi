# urfuapi

Pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in this paper and first released in this repository. This model is uncased: it does not make a difference between english and English.

based on https://huggingface.co/bert-base-uncased


## API description

Service works with POST method on http://20.123.12.234:8000/root_get_suggestions

### Required format

{
  "sentence": "string"
}

### Response

Service responds with a a JSON list of dictionaries
|score|sequence|token|token_str|
|_____|________|_____|_________|
|score of the given word|||||

## Notebook for testing

https://colab.research.google.com/drive/1NvD5Nv-UJCybx4JYYTfJJCweNYaz5v_f?usp=sharing
