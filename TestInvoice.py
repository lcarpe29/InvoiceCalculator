import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def qnt():
    qnt = 2
    return qnt

@pytest.fixture()
def unit_price():
    unit_price = 2.5
    return unit_price

@pytest.fixture()
def discount():
    discount = 7
    return discount

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_canAddProduct(invoice, qnt, unit_price, discount):
    invoice.addProduct(qnt, unit_price, discount)
    assert invoice.addProduct(qnt, unit_price, discount) == {'qnt' : 2, 'unit_price' : 2.5, 'discount' : 7}

def test_CanPrintReceipt(invoice, products):
    testReceipt = { 'items':{'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}, 'impure price' : 75,
                    'total discount': 5.62, 'pure price': 69.38}
    assert invoice.printReceipt(products) == testReceipt