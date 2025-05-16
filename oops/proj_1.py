# ss
# We need to design and implement a class that will be used to represent bank accounts,
# we want the following functionality and characteristics:
#     - accounts are uniquely identified by an account number (Assume it will be passed in the initializer)
#     - account holders have a first and last name.
#     - accounts have an associated preferred time zome offset.
#     - balances need to be zero or highe, and shoulkd not be directly settable.
#     - but deposits and withdrwals can be made (given sufficient funds)
#         - if a withdrawal is attempted that would result in nagative funds, the transactions should be declined.
#     - a monthly interest rate exists and is applicable to all accounts uniformly. There should be a method that can be called to calculate the interest on the current balance using the current interest rate and add it to the balance.
#     - each deposit and withdrawal must generate a confirmation number composed of:
#         - the transaction type: D fopr deposit, and W for withdrawal, I for interest deposit, and X for declined (in which case the balance remains unaffected)
#         - the account number.
#         - the time the transaction was made, using UTC
#         - Aan incrementing, number (that increments across all accounts and transactions)
#         - for(external) simplicity assume that the transacton id starts at zero (or whatever number you choose) whenever the program starts
#         - the condition number should be returned from any of the transactions methods (deposit, withdraw,etc)
#     - create a method that, given a confirmation number, returns:
#         - the account number, transaction code (D, W, etc), datetime(UTC FORMAT), datetime (in whatever timezonbe is specified in the argument, but more human readable), the transaction id
#         - Make it so it is a nicely structure onject(so can use dotted notation to access the three attributes)
#         - I purposefully made it so the desired timezone is passed as an argument, Can you figure out why? (hint: does this method require information from any instance?)

class MyClass:
    pass

print(MyClass.__dict__)

import numbers
from datetime import timedelta, datetime
import itertools
from collections import namedtuple

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')
        
        self._name = name
        
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')
        
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minute offset must be interger.')
        
        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError('Minutes offset must be between -59 and 59 (inclusive).')
        
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')
        
        self._offset_hours  = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return (isinstance(other, TimeZone)) and \
            self._name == other.name and \
            self._offset_hours ==  other._offset_hours and \
            self._offset_minutes == other._offset_minutes        
            
    def __repr__(self):
        return (f"Timezone(name='{self.name}', " 
                f"offset_hours = {self._offset_hours}, "
                f"offset_minutes = {self._offset_minutes})")
        
# unit-testing
try:
    tz = TimeZone('ABC', 18, 0)
except ValueError as ex:
    print(ex)
    
# Transaction Numbers
class TransactionID:
    def __init__(self, start_id):
        self._start_id = start_id
        
    def next(self):
        self._start_id += 1
        return self._start_id
    
    
# class Account:
#     transaction_counter = TransactionID(100)
    
#     def make_transaction(self):
#         new_trans_id = Account.transaction_counter.next()
#         return new_trans_id
    
# class Account:
#     transaction_counter = itertools.count(100)
    
#     def make_transactions(self):
#         new_trans_id = next(Account.transaction_counter)
#         return new_trans_id
    
#Account number  
class Account:
    transaction_counter = itertools.count(100) 
    _interest_rate = 0.5 # percent
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'regected': 'X'
        }
    
    
    def __init__(self, account_number, first_name, last_name, timezone = None, initial_balance = 0):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self.full_name = first_name + ' ' + last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0,0,0)
        self.timezone = timezone
        self._balance = Account.validate_real_number(initial_balance, min_value=0)
        
    @property
    def account_number(self):
        return self._account_number   
            
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = self.validate_and_set_name('_first_name', value, 'First Name')
        
    @last_name.setter
    def last_name(self, value):
        self._last_name = self.validate_and_set_name('_last_name', value, 'Last Name')
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object.')
        self._timezone = value
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    
    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real()):
            raise ValueError('Interest rate must be a real number.')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')   
        cls._interest_rate =  value
        
        
    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}- {self.account_number}-{dt_str}-{next(Account.transaction_counter)}'


    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is not None and value < min_value:
            raise ValueError(f'VALUE MUST BE AT LEAST {min_value}')
        return value
  
  
    def validate_and_set_name(self, attr_name,value, field_title):
        if len(str(value).strip()) == 0 or value is None:
            raise ValueError('Field title cannot be empty.')
        setattr(self.attr_name, value)
   
    @staticmethod
    def parse_confirmation_code(confirmation_code, prefrereed_time_zone=None):
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('invalid confirmation code')
        transaction_code, account_number, raw_dt_utc, transaction_id = parts
        
        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError  as ex:
            raise ValueError('Invalid transaction datetime') from ex #for beck tracking
        # print(ex.__cause__)
        
        if prefrereed_time_zone is None:
            prefrereed_time_zone = TimeZone('UTC', 0, 0) 
            
        if not isinstance(prefrereed_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.') 
        
        Confirmation = namedtuple('Confirmation', 'account_number transaction_number transaction_id time_utc time')
        dt_preferred = dt_utc + prefrereed_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({prefrereed_time_zone.name})"
        return Confirmation(account_number,transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)   

    def deposit(self, value):
        value = Account.validate_real_number(value, 0.01)
        transaction_code = Account._transaction_codes['deposit']
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += value
        return conf_code
    
    def withdraw(self, value):
        value = Account.validate_real_number(value, 0.01)
        accepted = False
        if self.balance - value < 0:
            transaction_code = Account._transaction_codes['regected']
        else:
            accepted = True
            transaction_code = Account._transaction_codes['withdraw'] 
            
        conf_Code = self.generate_confirmation_code(transaction_code)
        if accepted:
            self._balance -= value
        return conf_Code
    
    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance += interest
        return conf_code
        
# 
a = Account('A100',' Eric', 'Idle', timezone = TimeZone('MST', -7, 0), initial_balance=100)
print(a.balance)
print(a.deposit(150.2))
print(a.balane)
print(a.withdraw(0.02))
Account.set_interest_rate(1.0)
print(a.get_interest_rate())
print(a.pay_interest())
print(a.balance)

# Unit Testing
# integration testing
import unittest

def run_test(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestAccount(unittest.TestCase):
    # def setUp(self):
    #     print('running setup')
    #     self.x = 100
        
    # def test_ok(self):
    #     self.assertEqual(1, 0)
    #     # assertEqual = shows you exact error as well!.
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone('TZ', 1, 30)
        self.balance = 100.00
        self.withdrawal_amount = 200
        
    def create_account(self):
        return Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)   
        
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=1, minutes=-30), tz.offset)
        
    def test_timezone_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezone_not_equal(self):
        tz = TimeZone('ABC', -1, -30)

        test_timezones = (
            TimeZone('DEF', -1, 30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, 30),
            # TimeZone('ABC', -1, -30),
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number = f'Test # {i}'):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        # account_number = 'A100'
        # first_name = 'FIRST'
        # last_name = 'LAST'
        # tz = TimeZone('TZ', 1, 30)
        # balance = 100.00
        # use setup method
        a = self.create_account()
        
        self.assertEqual(self.account_number, a.account_number)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name , a.last_name)
        self.assertEqual(self.first_name + ' ' + self.last_name, a.full_name)
        self.assertEqual(self.tz, a.timezone)
        self.assertEqual(self.balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        self.first_name = ''
        
        # you can reference from setup as well
        with self.assertRaises(ValueError):
            self.create_account()
            
    def test_create_min_balance(self):
        self.balance = -100.00
        
        with self.assertRaises(ValueError):
            a = self.create_account()
            
    def test_account_withdraw_ok(self):
        a = self.create_account()
        
        conf_code = a.withdraw(self.withdraw_amount)
        self.assertIn(conf_code.startswith('W-'))
        self.assertEqual(self.balance-self.withdraw_amount,a.balance )
        
    def test_withdraw_overdraw(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        withdraw_amount = 200
        a = Account(account_number, first_name, last_name, initial_balance = balance)
        
        conf_code = a.withdraw(withdraw_amount)
        self.assertIn(conf_code.startswith('X-'))
        self.assertEqual(balance, a.balance)

    