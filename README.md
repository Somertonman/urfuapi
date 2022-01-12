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

Service responds with a a JSON list of dictionaries sorted by *score*


keys|score|sequence|token|token_str|
|-|-|-|-|-|
description|score of the given word|sentence string with given word|unique token ID|token word|
example|0.3510996401309967|i am urfu.|2572|am|

## Notebook for testing

https://colab.research.google.com/drive/1NvD5Nv-UJCybx4JYYTfJJCweNYaz5v_f?usp=sharing
