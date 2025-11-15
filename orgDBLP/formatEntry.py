def simplify(s):
    if isinstance(s, (str)):
        return s
    elif isinstance(s, (list)):
        return ", ".join(s)
    else:
        raise Exception("Trying to concatenate the wrong type")

    
POTENTIAL_FIELDS = {
    "authors": ":AUTHORS: {}",
    "title"  : ":TITLE:   {}",
    "doi"    : ":DOI:     {}",
    "year"   : ":YEAR:    {}",
    "url"    : ":BIBTEX:  {}?view=bibtex",
    "ee"     : ":OFFICIAL:{}",
    "venue"  : ":VENUE:   {}",
    
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
        kept = False
        if k == "ee":
            if include_published:
                kept = True
        elif k in entry:
            kept = True
        if kept:
            result += POTENTIAL_FIELDS[k].format(simplify(entry[k])) + "\n"
    return result + ":END:"

