"""Tests for cursing.nword check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.dreyers import wan_intensifiers_and_throat_clearers as chk


class TestCheck(Check):
    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_intensifiers(self):
        """Wan intensifiers"""
        assert self.passes("""The flower is pretty.""")
        assert self.passes("""The world is not just.""")
        assert not self.passes("""Pretty pretty good.""")
        assert not self.passes("""That went pretty badly.""")
        assert not self.passes("""Would you just stop.""")
        assert self.passes("""The so-called head of state.""")
        assert not self.passes("""That's so cool.""")
        assert self.passes("""The automation of administrative decisionmaking -- so-called cyberdelegation -- is already ongoing.""")
