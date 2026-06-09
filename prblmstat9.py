class Member:
    def __init__(self, member_name):
        self.member_name = member_name


class MembershipPlan:
    def __init__(self, plan_name, monthly_fee):
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee


class Gym:
    def __init__(self, duration):
        self.duration = duration

    def generate_receipt(self, member, plan):
        total_fee = self.duration * plan.monthly_fee

        print("=" * 50)
        print("             MEMBERSHIP RECEIPT")
        print("=" * 50)

        print(f"\nMember Name : {member.member_name}")
        print(f"\nPlan        : {plan.plan_name}")
        print(f"\nDuration    : {self.duration} Months")

        print(f"\nTotal Fee   : ₹{total_fee}")

        print("\n" + "=" * 50)


member = Member("Ava")
plan = MembershipPlan("Premium", 2000)

gym = Gym(6)
gym.generate_receipt(member, plan)