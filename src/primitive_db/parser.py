import sqlparse

def sql_parser(query):
    parsed_statements = sqlparse.parse(query)
    statement = parsed_statements[0]
    print(parsed_statements[0][3])
    print("\n")

    for token in statement.tokens:
        print(f"Тип: {token.ttype} | Значение: {repr(token.value)} | Группа: {token.is_group}")