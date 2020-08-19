
class HTest:
    def __init__(
        self,
        statistic,
        parameter,
        p_value,
        estimate,
        conf_int,
        null_value,
        alternative,
        method,
        data_name
    ):
        self.statistic = statistic
        self.parameter = parameter
        self.p_value = p_value
        self.estimate = estimate
        self.conf_int = conf_int
        self.null_value = null_value
        self.alternative = alternative
        self.method = method
        self.data_name = data_name

    def __repr__(self):
        return "{}".format(self.p_value)


def prop_test(x, n, p=None, alternative="two.sided", conf_level=0.95, correct=True):
    return_val = HTest(
        statistic,
        parameter,
        p_value,
        estimate,
        conf_int,
        null_value,
        alternative,
        method,
        data_name
    )
    return return_val