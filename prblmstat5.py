class Customer:
    def __init__(self, customer_name, mobile):
        self.customer_name = customer_name
        self.mobile = mobile


class RechargePlan:
    def __init__(self, plan_name, amount):
        self.plan_name = plan_name
        self.amount = amount


class Recharge:
    def generate_receipt(self, customer, plan):
        print("=" * 50)
        print("             RECHARGE RECEIPT")
        print("=" * 50)

        print(f"\nCustomer Name : {customer.customer_name}")
        print(f"\nPlan Selected : {plan.plan_name}")
        print(f"\nAmount Paid   : ₹{plan.amount}")

        print("\nStatus        : SUCCESSFUL")
        print("\n" + "=" * 50)


customer = Customer("Logan", "9876543210")
plan = RechargePlan("Unlimited 84 Days", 799)

recharge = Recharge()
recharge.generate_receipt(customer, plan)