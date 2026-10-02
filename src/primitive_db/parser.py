import sqlglot
import sqlglot.expressions as exp

def sql_parser(query, command_name):
    match command_name:
        case "select":
            before_where = query.split("where")[0]
            table_name = before_where[2]
            where_data = [word.strip() for word in query.split("where")[1].strip().split("=")]

            return [command_name, table_name, where_data]

        case "update":
            after_set = query.split("set")[1]
            before_where = after_set.split("where")[0]
                    
            set_data = [word.strip() for word in before_where.strip().split("=")]
        
            where_data = [word.strip() for word in after_set.split("where")[1].strip().split("=")]
                    
            return [table_name, set_data, where_data]












    parsed = sqlglot.parse_one(query)

    table = parsed.find(exp.Table)
    table_name = table.name
    
    match command_name:
        case "insert":
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
            
            return [table_name, row_values]
        
        case "select" | "delete":
            where_values = parsed.find(exp.Where)
            return [table_name, where_values]

        case "update1":
            set_values = parsed.find(exp.Set)
            where_values = parsed.find(exp.Where)


            set_values = {}
            if set_values:
                for expression in set_values.expressions:
                    if isinstance(expression, exp.EQ):
                        column_name = expression.left.sql()
                        column_value = expression.right.sql()
                        set_values[column_name] = column_value

            return [table_name, where_values]

        case "update":
            after_set = query.split("set")[1]
            before_where = after_set.split("where")[0]
            
            set_data = [word.strip() for word in before_where.strip().split("=")]

            where_data = [word.strip() for word in after_set.split("where")[1].strip().split("=")]
            
            return [table_name, set_data, where_data]

