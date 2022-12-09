class Bill:
    _courses_2 = 2195
    _courses_3 = 2695
    _deposit_pp = 500
    _deposit = 7500
    _total = 0
    toPay_2s = 0
    toPay_3s = 0

    def charge_2c(self, amount):
        self._total += amount * self._courses_2
        self.toPay_2s += 1 * amount

    def charge_3c(self, amount):
        self._total += amount * self._courses_3
        self.toPay_3s += 1 * amount

    def pay_2c(self, amount):
        self._total -= self._courses_2 * amount
        self.toPay_2s -= 1 * amount
        # Decrements the deposit as it goes
        self._deposit -= self._deposit_pp * amount

    def pay_3c(self, amount):
        self._total -= self._courses_3 * amount
        self.toPay_3s -= 1 * amount
        # Decrements the deposit as it goes
        self._deposit -= self._deposit_pp * amount

    def charge_specific(self, charge):
        self._total += charge * 100

    def pay_specific(self, toPay):
        self._total -= toPay * 100

    def get_total(self):
        return self._total / 100

    def get_deposit(self):
        return self._deposit / 100
