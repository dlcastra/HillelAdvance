def parse(query: str) -> dict:
    if '?' in query:
        query_parts = query.split('?')
        take_query_args = query_parts[1]  # Беремо частину пусилання після знаку "?"
        split_query_args = take_query_args.split('&')  # Якщо в цій частині присутній знак "&", то розбиваємо ще на частини
        query_dict = {}

        for attribute in split_query_args:
            attribute_parts = attribute.split('=')  # Ділемо все що залишилося на key: value

            if len(attribute_parts) == 2:
                attribute_key, attribute_value = attribute_parts
                query_dict[attribute_key] = attribute_value

        return query_dict

    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    return {}

# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
