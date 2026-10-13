import json


def sql_parser(query, command_name):
    table_name = query.split()[2]
    match command_name:
        case "select":
            if len(query.split()) > 3:
                before_where = query.split("where")[0]
                
                table_name = query.split()[2]
                
                where_data = [word.strip() for word in query.split("where")[1]
                .strip().split("=")]

                return [table_name, where_data]
            else:
                return [table_name, None]

        case "update":
            table_name = query.split()[1]
            after_set = query.split("set")[1]
            before_where = after_set.split("where")[0]
                    
            set_data = [word.strip() for word in before_where.strip().split("=")]
        
            where_data = [word.strip() for word in after_set.split("where")[1]
            .strip().split("=")]
                    
            return [table_name, set_data, where_data]

        case "insert":
            table_name = query.split()[2]
            row_values = query.split("values")[1].strip()

            rows = tuple(json.loads(row_values.replace('(', '[').replace(')', ']')))

            return [table_name, list(rows)]

        case "delete":
            before_where = query.split("where")[0]
            table_name = query.split()[2]
            where_data = [word.strip() for word in query.split("where")[1]
            .strip().split("=")]

            return [table_name, where_data]

