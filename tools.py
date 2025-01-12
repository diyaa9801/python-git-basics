def convert_lod_to_dol(lod):
    """Convert a list of dictionaries (LoD) to a dictionary of lists (DoL).

    Transforms a list of dictionaries, where each dictionary represents a row of data, 
    into a dictionary of lists, where each key has a list of values corresponding to that key's values across rows.

    Args:
        lod (list of dict): A list of dictionaries, each dictionary containing key-value pairs 
            representing columns and their values for a single row.

    Returns:
        dict: A dictionary of lists, where each key has a list of values aggregated from each row.
    """
    dol = {}
    
    for row in lod:
        for key, value in row.items():
            if key not in dol:
                dol[key] = []
            dol[key].append(value)
    
    return dol


def convert_dol_to_lod(dol):
    """Convert a dictionary of lists (DoL) to a list of dictionaries (LoD).

    Transforms a dictionary of lists, where each key is associated with a list of values,
    into a list of dictionaries, where each dictionary represents a row with values for each key.

    Args:
        dol (dict): A dictionary where each key has a list of values representing column data.

    Returns:
        list of dict: A list of dictionaries, each containing a single row of data with key-value pairs.
    """
    # Calculating the number of rows
    first_column = list(dol.values())[0] 
    num_rows = len(first_column)

    lod = []
    
    for i in range(num_rows):
        row = {}

        for key in dol:
            row[key] = dol[key][i]
        
        lod.append(row)
    
    return lod

def create_markdown_table(data):
    """Prints dol_or_lod in a table format, handling both lod and dol formats.

    Args:
        dol_or_lod (by definition, lod or dol): The format to be printed in table.

     Returns:
        Table: A string based table whose a pre-designed format.
    """
    # Determine if the input is lod or dol
    if isinstance(data, list):  # lod
        headers = data[0].keys() if data else []
        rows = [[row[header] for header in headers] for row in data]
        
    elif isinstance(data, dict):  # dol
        headers = data.keys()
        rows = list(zip(*data.values()))
    else:
        print("Unsupported data format")
        return

    # Print table header
    header_line = "| " + " | ".join(headers) + "|"
    separator_line = "| " + " | ".join("-----" for item in headers) + " |"
    print(header_line)
    print(separator_line)
    
    # Print each row
    for row in rows:
        print("| " + " | ".join(str(item) for item in row) + " |")






