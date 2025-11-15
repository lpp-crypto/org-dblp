def simplify(s):
    if isinstance(s, (str)):
        return s
    elif isinstance(s, (list)):
        return ", ".join(s)
    else:
        raise Exception("Trying to concatenate the wrong type")

    
POTENTIAL_FIELDS = {
    "authors": ":AUTHORS: {}\n",
    "title": ":TITLE: {}\n",
    "doi": ":DOI: {}\n",
    "year": ":YEAR: {}\n",
    "url" : ":BIBTEX: {}?view=bibtex\n",
    "ee" : ":PUBLISHED: {}\n",
    "venue": ":VENUE: {}\n",
    
}


def org_format(entry, url):
    if "title" not in entry:
        raise Exception("A title is needed!")
    elif entry["title"][-1] == ".": # dropping '.' if necessary
        entry["title"] = entry["title"][:-1] 
    include_published = True
    if url == "":
        if "ee" in entry:
            url = entry["ee"]
            include_published = False
        else:
            url = ""
    result = "** [[{}][{}]]\n".format(url, entry["title"])
    result += ":PROPERTIES:\n"
    for k in POTENTIAL_FIELDS:
        if k == "ee":
            if include_published:
                result += POTENTIAL_FIELDS[k].format(simplify(entry[k]))
        elif k in entry:
            result += POTENTIAL_FIELDS[k].format(simplify(entry[k]))
    return result + ":END:"

