from datetime import datetime

from carparts.sternman_engine import SternmanEngine

from carparts.nubbin_battery import NubbinBattery


class Palindrome(SternmanEngine, NubbinBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + super.battery_life)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
