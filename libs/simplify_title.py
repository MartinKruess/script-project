def simplify_title(full_title, shorts):
    parts = full_title.split("-")
    for short in shorts:
        if short in full_title:
            return short
            if "Visual Studio Code" in full_title:
                return "Visual Studio Code"
            # if len(parts[0].strip()) > 4:
            #     return f"{short} - {parts[0].strip()}"
            # elif len(parts) > 1:
            #     return f"{short} - {parts[1].strip()}"
    return full_title