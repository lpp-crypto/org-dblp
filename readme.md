# org-dblp


## Idea

In order to manage a bibliography using orgmode files in emacs, it is convenient to be able to generate org headings containing bibliography information. This project provides this by querying [https://dblp.org/](DBLP) and parsing the result.


## Installation

Run the following command to install a small executable written in `python` that handles the heavy lifting (DBLP query, parsing of the result, orgmode formatting of the result):

```sh
pip intall git+https://github.com/lpp-crypto/org-dblp
```

Then, add the following `elisp` function to your emacs configuration file. It wraps the python script so it can be queried directly from emacs.

```elisp
(defun org-dblp(query url)
  (interactive
   (list
    (read-string "query: ")
    (read-string "open URL: ")))
  (with-current-buffer
      (switch-to-buffer "org-dblp")
      (org-mode)
      (insert (shell-command-to-string
               (format
                "~/.local/bin/orgDBLP_query -u \"%s\" -q \"%s\"" ; <-- !TODO! update this path
                url
                query)))))
```


## Usage

Once you have done the steps above, you simply need to interactively call the `org-dblp` function, and fill in the form that appeared:
- `query` is the query that will be sent to DBLP. The more specific, the better.
- `open URL` is intended to contain the URL to an open access copy of the paper.

This creates a new buffer called `org-dblp` that contains a sequence of org headings corresponding to the papers matching the query. For example, the query `transistor leo perrin crypto` followed by the URL `https://eprint.iacr.org/2025/282` (which corresponds to the open access version of this paper) yields:

```org
* [[https://eprint.iacr.org/2025/282][Transistor: a TFHE-Friendly Stream Cipher]] :mine:
:PROPERTIES:
:AUTHORS: Jules Baudrin, Sonia Belaïd, Nicolas Bon, Christina Boura, Anne Canteaut, Gaëtan Leurent, Pascal Paillier, Léo Perrin, Matthieu Rivain, Yann Rotella, Samuel Tap
:TITLE: Transistor: a TFHE-Friendly Stream Cipher
:DOI: 10.1007/978-3-032-01901-1_17
:YEAR: 2025
:BIBTEX: https://dblp.org/rec/conf/crypto/BaudrinBBBCLPPRRT25?view=bibtex
:PUBLISHED: https://doi.org/10.1007/978-3-032-01901-1_17
:VENUE: CRYPTO
:END:
```

You can then select the heading actually corresponding to the paper you are interested in and paste it to your personal bibliography.

If you want to remove such headings from the output of `org-roam-find`, you can add another specific property (namely, `:ROAM_EXCLUDE: t`), or use the functions at the end of [./elisp.el](./elisp.el). They assume that all paper headings have the tag `paper`, which can be enforced by tweaking the function `formatEntry.org_format`, or by having `#+filetags: :paper:` at the top of the file containing the papers.

## Acknowledgement

The code used to query DBLP is heavily inspired by [https://github.com/alumik/dblp-api/](dblp-api), by [https://github.com/alumik/](@alumik).


