#A multinational company hires candidates across multiple departments. The company requires a Recruitment Lifecycle Management System to manage the complete hiring process, from job posting to employee onboarding. The system should streamline candidate applications, screening, interviews, offer generation, and hiring analytics.
class RecruitmentSystem:
    def __init__(self):
        self.jobs = {}
        self.candidates = {}
        self.applications = {}
        self.waiting_list = []

    def add_job(self, job_id, title, dept, min_gpa):
        self.jobs[job_id] = {"title": title, "dept": dept, "min_gpa": min_gpa}

    def register_candidate(self, cid, name, email, gpa):
        if cid in self.candidates:
            print("Candidate ID already exists")
        else:
            self.candidates[cid] = {"name": name, "email": email, "gpa": gpa}

    def search_candidate(self, identifier):
        for cid, details in self.candidates.items():
            if cid == identifier or details["email"] == identifier:
                return details
        return None

    def sort_candidates(self, by="name"):
        if by == "name":
            return sorted(self.candidates.items(), key=lambda x: x[1]["name"])
        elif by == "aptitude":
            return sorted(
                [(cid, self.candidates[cid]["name"], app["aptitude"])
                 for (cid, jid), app in self.applications.items()],
                key=lambda x: x[2] or 0,
                reverse=True
            )

    def apply_job(self, cid, job_id):
        if (cid, job_id) in self.applications:
            print("Already applied!")
            return
        if self.candidates[cid]["gpa"] < self.jobs[job_id]["min_gpa"]:
            print("Not eligible!")
            return
        self.applications[(cid, job_id)] = {"status": "Applied", "aptitude": None}

    def aptitude_test(self, cid, job_id, score):
        app = self.applications[(cid, job_id)]
        if app["status"] == "Rejected":
            print("Candidate already rejected")
            return
        app["aptitude"] = score
        app["status"] = "Aptitude Cleared" if score >= 60 else "Rejected"

    def technical_interview(self, cid, job_id, result):
        app = self.applications[(cid, job_id)]
        if app["status"] != "Aptitude Cleared":
            print("Not eligible for technical interview")
            return
        app["status"] = "Technical Cleared" if result == "Pass" else "Rejected"

    def hr_interview(self, cid, job_id, result):
        app = self.applications[(cid, job_id)]
        if app["status"] != "Technical Cleared":
            print("Not eligible for HR interview")
            return
        app["status"] = "HR Cleared" if result == "Pass" else "Rejected"

    def generate_offer(self, cid, job_id):
        app = self.applications[(cid, job_id)]
        if app["status"] == "HR Cleared":
            app["status"] = "Selected"
        else:
            print("Offer cannot be generated")

    def rank_candidates(self, job_id):
        scored = [(cid, app["aptitude"]) for (cid, jid), app in self.applications.items()
                  if jid == job_id and app["aptitude"] is not None]
        return sorted(scored, key=lambda x: x[1], reverse=True)

    def hiring_report(self):
        total = len(self.applications)
        selected = sum(1 for app in self.applications.values() if app["status"] == "Selected")
        rejected = sum(1 for app in self.applications.values() if app["status"] == "Rejected")
        print(f"Total: {total}, Selected: {selected}, Rejected: {rejected}")

    def add_to_waiting_list(self, cid):
        self.waiting_list.append(cid)

    def offer_from_waiting_list(self):
        if self.waiting_list:
            cid = self.waiting_list.pop(0)
            print(f"Offer given to candidate {cid}")


system = RecruitmentSystem()
system.add_job("J01", "Software Engineer", "IT", 7.0)
system.register_candidate("C01", "Alice", "alice@mail.com", 8.0)
system.register_candidate("C02", "Bob", "bob@mail.com", 6.5)

print("\n--- TC01 ---")
system.apply_job("C01", "J01")
system.apply_job("C01", "J01")

print("\n--- TC02 ---")
system.apply_job("C02", "J01")

print("\n--- TC03 ---")
system.aptitude_test("C01", "J01", 59)

print("\n--- TC04 ---")
system.aptitude_test("C01", "J01", 75)

print("\n--- TC05 ---")
system.technical_interview("C01", "J01", "Fail")

print("\n--- TC06 ---")
system.technical_interview("C01", "J01", "Pass")

print("\n--- TC07 ---")
system.hr_interview("C01", "J01", "Fail")

print("\n--- TC08 ---")
system.hr_interview("C01", "J01", "Pass")
system.generate_offer("C01", "J01")

print("\n--- TC09 ---")
print(system.search_candidate("alice@mail.com"))

print("\n--- TC10 ---")
print(system.sort_candidates(by="aptitude"))

print("\n--- TC11 ---")
system.hiring_report()

print("\n--- TC12 ---")
system.add_to_waiting_list("C02")
system.offer_from_waiting_list()
