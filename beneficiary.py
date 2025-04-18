beneficiaries = {}

def add_beneficiary(id,name):
    if id in beneficiaries:
        return "Already exists"
    beneficiaries[id] = name 
    return "beneficiary added"