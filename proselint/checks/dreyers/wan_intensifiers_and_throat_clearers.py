# -*- coding: utf-8 -*-
"""Chapter 1. Tidying Up Your Prose

---
layout:     post
source:     Benjamin Dreyer
title:      Dreyer's English
date:       2014-06-10 12:31:19
categories: writing
---

Avoid Wan Intensifiers

"""
from proselint.tools import existence_check, memoize
import spacy

from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")

def check(text):
    """Check the text."""
    err = "dreyers.wan_intensifiers_and_throat_clearers"
    msg = u"Go without writing these terms, they're not really useful"

    # always
    l = [
        "very",
        "rather",
        "really",
        "quite",
        "in fact",
        "of course",
        "surely",
        "that said",
        "actually"
    ]

    errors = existence_check(text, l, err, msg, ignore_case=True)

    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern = [
        {'LOWER' : 'pretty', "OP" : "+"}, # pretty pretty good
        {'POS': {"IN": ['VERB', "ADJ", "ADV"]}, "OP" : "+"}
    ]
    matcher.add('PRETTY', None, pattern)

    pattern = [
        {'LOWER' : 'so', "OP" : "+"}, # pretty pretty good
        {'POS': {"IN": ['VERB', "ADJ", "ADV"]}, "OP" : "+"}
    ]
    matcher.add('SO', None, pattern)

    # pattern = [
    #     {'LOWER' : 'pretty', "OP" : "+"}, # pretty pretty badly
    #     {'POS': 'ADV', "OP" : "+"}
    # ]
    # matcher.add('PRETTY_ADV', None, pattern)
    pattern = [
        {'LOWER' : 'just', 'POS' : {"IN" : ["ADJ", "ADV"]}}, # just stop
        {'POS': {"IN": ['VERB', "ADJ", "ADV"]}, "OP" : "+"}
    ]
    matcher.add('JUST', None, pattern)
    matches = matcher(doc)

    spans = [doc[start:end] for match_id, start, end in matches]
    for match_id, start, end in matches:
        errors.append((
            doc[start].idx,
            doc[end].idx + 2,
            err,
            msg,
            None))
    return errors