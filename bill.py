productTax = 0.5  # productTax 5cents
makingCharge = 0.10  # productMakingCharges = 10cents
infrastructureBill = 0.10  # infrastructure bill = 10$
CapitalGains = 1

CoffeeItems = {

    "Cappuccino": 4,
    "Express": 3,
    "Americano": 2.50,
    "coldCoffee": 2

}

OtherItems = {

    "Biscuit": 3,
    "Cookies": 1,
    "chocochips": 0.50,
    "chillichips": 0.50,
    "granularmodular chips": 1.50,
    "Margarettapizza": 2.50,
    "newyorksilicastylepizza": 3,
    "Thesiliconvalleypizza": 5,
    "tangytwistpizza": 1.50

}


class BillPayment:
    totalBill = CapitalGains + productTax + makingCharge + infrastructureBill

    def coffeePayment(self, data):
        for i in data:
            self.totalBill += CoffeeItems[i]
        return self.totalBill

    def extraElementPayment(self, data):
        for i in data:
            self.totalBill += CoffeeItems[i]
        return self.totalBill

