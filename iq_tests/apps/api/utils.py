from ..verification.models import EQTest, IQTest


def create_iq_test():
    """Create new IQ Test."""
    iq_test = IQTest()
    iq_test.save()
    return iq_test


def create_eq_test():
    """Create new EQ Test."""
    eq_test = EQTest()
    eq_test.save()
    return eq_test
