def parse(query: str) -> dict:
    return {}


# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if '=' in query:
        query_parts = query.split(';')
        query_dict = {}

        for attribute in query_parts:
            attribute = attribute.strip()

            if '=' in attribute:
                attribute_parts = attribute.split('=')

                key = attribute_parts[0]
                value = attribute_parts[1] if len(attribute_parts) == 2 else '='.join(attribute_parts[1:])
                query_dict[key] = value

        # print(query_dict)
        return query_dict

    return {}


# parse_cookie("name=Dima=User;age=28;")
if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('age=28=Years=Old;') == {'age': '28=Years=Old'}
    assert parse_cookie('name=Dima=User;age=28=Years;') == {'name': 'Dima=User', 'age': '28=Years'}
    assert parse_cookie('name=Dima=User=UserID=123456;age=28=Years;') == {'name': 'Dima=User=UserID=123456', 'age': '28=Years'}
    assert parse_cookie('name=" ";') == {'name': '" "'}
    assert parse_cookie('name=;') == {'name': ''}
    assert parse_cookie('name=/[}=-@!$%^?:"~;') == {'name': '/[}=-@!$%^?:"~'}
