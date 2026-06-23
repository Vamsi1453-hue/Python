jobs = {}
candidates = {}
applications = {}
waiting_list = []

def add_job(job_id, title, dept, min_cgpa):
    jobs[job_id] = {"title": title, "dept": dept, "min_cgpa": min_cgpa}

def register_candidate(cid, name, email, cgpa):
    if cid in candidates:
        print("Candidate ID already exists!")
    else:
        candidates[cid] = {"name": name, "email": email, "cgpa": cgpa}

def apply_job(cid, job_id):
    if (cid, job_id) in applications:
        print("Already applied!")
        return
    if candidates[cid]["cgpa"] < jobs[job_id]["min_cgpa"]:
        print("Not eligible!")
        return
    applications[(cid, job_id)] = {"status": "Applied", "aptitude": None}

def aptitude_test(cid, job_id, score):
    app = applications[(cid, job_id)]
    app["aptitude"] = score
    if score >= 60:
        app["status"] = "Aptitude Cleared"
    else:
        app["status"] = "Rejected"

def technical_interview(cid, job_id, result):
    app = applications[(cid, job_id)]
    if app["status"] != "Aptitude Cleared":
        print("Not eligible for technical interview")
        return
    app["status"] = "Technical Cleared" if result == "Pass" else "Rejected"

def hr_interview(cid, job_id, result):
    app = applications[(cid, job_id)]
    if app["status"] != "Technical Cleared":
        print("Not eligible for HR interview")
        return
    app["status"] = "HR Cleared" if result == "Pass" else "Rejected"

def generate_offer(cid, job_id):
    app = applications[(cid, job_id)]
    if app["status"] == "HR Cleared":
        app["status"] = "Selected"
    else:
        print("Offer cannot be generated")

def rank_candidates(job_id):
    scored = [(cid, app["aptitude"]) for (cid, jid), app in applications.items() if jid == job_id and app["aptitude"] is not None]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked

def add_to_waiting_list(cid):
    waiting_list.append(cid)

def offer_from_waiting_list():
    if waiting_list:
        cid = waiting_list.pop(0)
        print(f"Offer given to candidate {cid}")

def search_candidate(identifier):
    for cid, details in candidates.items():
        if cid == identifier or details["email"] == identifier:
            return details
    return None

def sort_candidates(by="name"):
    if by == "name":
        return sorted(candidates.items(), key=lambda x: x[1]["name"])
    elif by == "aptitude":
        return sorted(applications.items(), key=lambda x: x[1]["aptitude"] or 0, reverse=True)

def hiring_report():
    total = len(applications)
    selected = sum(1 for app in applications.values() if app["status"] == "Selected")
    rejected = sum(1 for app in applications.values() if app["status"] == "Rejected")
    print(f"Total: {total}, Selected: {selected}, Rejected: {rejected}")

add_job("J01", "Software Engineer", "IT", 7.0)
register_candidate("C01", "Alice", "alice@mail.com", 8.0)
register_candidate("C02", "Bob", "bob@mail.com", 6.5)

print("\n--- TC01 ---")
apply_job("C01", "J01")
apply_job("C01", "J01")

print("\n--- TC02 ---")
apply_job("C02", "J01")

print("\n--- TC03 ---")
aptitude_test("C01", "J01", 59)

print("\n--- TC04 ---")
aptitude_test("C01", "J01", 75)

print("\n--- TC05 ---")
technical_interview("C01", "J01", "Fail")

print("\n--- TC06 ---")
technical_interview("C01", "J01", "Pass")

print("\n--- TC07 ---")
hr_interview("C01", "J01", "Fail")

print("\n--- TC08 ---")
hr_interview("C01", "J01", "Pass")
generate_offer("C01", "J01")

print("\n--- TC09 ---")
print(search_candidate("alice@mail.com"))

print("\n--- TC10 ---")
print(sort_candidates(by="aptitude"))

print("\n--- TC11 ---")
hiring_report()

print("\n--- TC12 ---")
add_to_waiting_list("C02")
offer_from_waiting_list()
