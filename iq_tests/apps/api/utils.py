from ..verification.models import EQTest, IQTest, Test


def _create_iq_test():
    """Create new IQ Test."""
    iq_test = IQTest()
    iq_test.save()
    return iq_test


def _create_eq_test():
    """Create new EQ Test."""
    eq_test = EQTest()
    eq_test.save()
    return eq_test


def _create_tests_set(iq_test, eq_test):
    """Create new test set."""
    test = Test(iq_test=iq_test, eq_test=eq_test)
    test.save()
    return test


def create_new_test():
    """Create new test."""
    iq_test = _create_iq_test()
    eq_test = _create_eq_test()
    return _create_tests_set(iq_test, eq_test)
