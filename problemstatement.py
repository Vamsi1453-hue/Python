from collections import defaultdict
candidates=[];jobs=[];scores={}
def add_candidate(n,e,skills): cid=len(candidates)+1; candidates.append({'id':cid,'name':n,'email':e,'skills':set(skills),'applied':[]}); return cid
def add_job(t,req): jid=len(jobs)+1; jobs.append({'id':jid,'title':t,'req':set(req),'apps':[]}); return jid
def apply(cid,jid): candidates[cid-1]['applied'].append(jid); jobs[jid-1]['apps'].append(cid)
def score(cid,tech,hr): scores[cid]=tech+hr
def shortlist(jid,minscore): j=jobs[jid-1]; return [(c['id'],c['name'],scores.get(c['id'],0)) for cid in j['apps'] for c in (candidates[cid-1],) if j['req'].issubset(c['skills']) and scores.get(c['id'],0)>=minscore]
if __name__=='__main__':
    a=add_candidate('Alice','a@x.com',['Python','SQL']); b=add_candidate('Bob','b@x.com',['Java','SQL'])
    j1=add_job('Backend',['Python','SQL'])
    apply(a,j1); apply(b,j1)
    score(a,8,7); score(b,6,5)
    print(shortlist(j1,13))
