"""Tests for cursing.nword check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.dreyers import common_misspelling as chk


class TestCheck(Check):
    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk
        
    def test_misspellings(self):
        # Misspellings
        assert self.passes("""I aided the sick""")
        assert self.passes("""I aid the sick""")
        assert not self.passes("""I aide the sick""")
