import sqlglot
import sqlglot.expressions as exp

def sql_parser(query):
    parsed = sqlglot.parse_one(query)
    
    table_name = parsed.find(exp.Table)
    row_values = []
    
    for row in parsed.find(exp.Values).expressions:
        for expression in row.expressions:
            if isinstance(expression, exp.Column):
                row_values.append(expression.this.this)
            elif isinstance(expression, exp.Literal):
                if expression.is_string:
                    row_values.append(expression.this)
                else:
                    row_values.append(int(expression.this))
            elif isinstance(expression, exp.Boolean):
                row_values.append(expression.this)
            else:
                row_values.append(expression.this if hasattr(expression, 'this') else expression)
        
    
    print(f"Название таблицы: {table_name}")
    print(f"Параметры: {row_values}")