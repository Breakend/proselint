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

    def test_smoke(self):
        """Basic smoke test for cursing.nword."""
        assert self.passes("""The flower is pretty.""")
        assert self.passes("""The world is not just.""")
        assert not self.passes("""Pretty pretty good.""")
        assert not self.passes("""That went pretty badly.""")
        assert not self.passes("""Would you just stop.""")