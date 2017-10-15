import re

class CheckParameter:

    def valid_hour(self, hour):
        time_re = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
        return bool(time_re.match(hour))

    def valid_name_list(self, name):
        return re.match('^[\w-]+$', name)