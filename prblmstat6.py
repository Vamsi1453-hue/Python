class Client:
    def __init__(self, client_name):
        self.client_name = client_name


class Project:
    def __init__(self, project_name, hourly_rate):
        self.project_name = project_name
        self.hourly_rate = hourly_rate


class Invoice:
    def __init__(self, hours_worked):
        self.hours_worked = hours_worked

    def generate_invoice(self, client, project):
        total = self.hours_worked * project.hourly_rate

        print("=" * 50)
        print("                CLIENT INVOICE")
        print("=" * 50)

        print(f"\nClient Name   : {client.client_name}")
        print(f"Project Name  : {project.project_name}")

        print(f"\nHours Worked  : {self.hours_worked}")
        print(f"\nTotal Amount  : ₹{total}")

        print("\n" + "=" * 50)


client = Client("Olivia")
project = Project("Portfolio Website", 1000)

invoice = Invoice(20)
invoice.generate_invoice(client, project)