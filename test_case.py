from beneficiary import add_beneficiary , beneficiaries

def test_add_beneficiart():
    beneficiaries.clear()

    result = add_beneficiary("R001" , "thrisha")
    assert result == "beneficiary added" , f"expected 'beneficiary added' , but got {result}"
    assert beneficiaries == {"R001": "thrisha"},  f"expected {{'R001':'thrisha'}} , but got {beneficiaries}"

    test_add_beneficiart()