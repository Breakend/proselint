# -*- coding: utf-8 -*-
"""TODO

---
layout:     post
source:     Benjamin Dreyer
title:      Dreyer's English
date:       2014-06-10 12:31:19
categories: writing
---

TODO
"""
from proselint.tools import existence_check, memoize
import spacy

from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")

def check(text):
    """Check the text."""
    errors = []
    err = "dreyers.common_misspellings"

    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern = [
        {'LOWER' : 'aide', 'POS' : "VERB"}
    ]
    matcher.add('AIDE_AS_A_VERB', None, pattern)

    matches = matcher(doc)

    spans = [doc[start:end] for match_id, start, end in matches]
    for match_id, start, end in matches:
        errors.append((
            doc[start].idx,
            doc[end].idx + 2,
            err,
            u"Aide used as a verb. Aid is the verb, aide is the noun meaning: 'an assistant to an important person, especially a political leader.'",
            None))
    return errors