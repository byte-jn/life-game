def replace_umlauts(data):
    if isinstance(data, str):
        data = (data.replace("(Ae)", "Ä")
        .replace("(ae)", "ä")
        .replace("(Oe)", "Ö")
        .replace("(oe)", "ö")
        .replace("(Ue)", "Ü")
        .replace("(ue)", "ü")
        .replace("(sz)", "ß"))
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace_umlauts(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace_umlauts(data[i])
    return data