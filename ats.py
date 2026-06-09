candidates = {}
jobs = {}
scores = {}

def add_candidate(name, skills):
    cid = len(candidates) + 1
    candidates[cid] = {"name": name, "skills": set(skills)}
    return cid

def add_job(title, req):
    jid = len(jobs) + 1
    jobs[jid] = {"title": title, "req": set(req), "applicants": []}
    return jid

def apply(cid, jid):
    jobs[jid]["applicants"].append(cid)

def score(cid, total):
    scores[cid] = total

def shortlist(jid, min_score):
    job = jobs[jid]
    return [
        (cid, candidates[cid]["name"])
        for cid in job["applicants"]
        if job["req"].issubset(candidates[cid]["skills"])
        and scores.get(cid, 0) >= min_score
    ]

alice = add_candidate("Alice", ["Python", "SQL"])
bob = add_candidate("Bob", ["Java", "SQL"])
backend = add_job("Backend", ["Python", "SQL"])
apply(alice, backend)
apply(bob, backend)
score(alice, 15)
score(bob, 11)
print(shortlist(backend, 13))