from account import Account
import streamlit as st

class Manager:
    def __init__(self, manager_id=99999, pin=1234):
        self.manager_id = manager_id
        self.pin = pin

    def view_bank_vault(self, accounts):
        total_balance = sum(ph.balance for ph in accounts)
        return f"Total Bank Vault Balance: {total_balance}"

    def view_all_accounts(self, accounts):
        return [f"Account: {ph.name}, Balance: {ph.balance}" for ph in accounts]