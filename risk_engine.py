def analyze_risk(name, cid, data, smiles):

    props = data['PropertyTable']['Properties'][0]

    formula = props.get('MolecularFormula', 'NA')
    weight = props.get('MolecularWeight', 0)
    iupac_name = props.get('IUPACName', 'Not Available')
    common_name = name.capitalize()

    try:
        weight = float(weight)
    except:
        weight = 0

    flags = []

    # RULES
    if weight > 500:
        flags.append("High Molecular Weight")

    if 150 < weight <= 500:
        flags.append("Moderate Molecular Weight")

    if 0 < weight < 100:
        flags.append("Small Molecule")

    if weight == 0:
        flags.append("Invalid Weight")

    if smiles == "Not Available":
        flags.append("Missing Structure")

    if len(smiles) > 100:
        flags.append("Complex Structure")

    # CLASSIFICATION
    if formula == "NA" and smiles == "Not Available":
        risk = "Insufficient Data"
    elif len(flags) == 0:
        risk = "Low Risk"
    elif len(flags) == 1:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    # SCORE (0–10 scale)
    score = min(len(flags) * 2, 10)

    # RECOMMENDATION
    if risk == "Low Risk":
        rec = "Ready for Virtual Screening"
    elif risk == "Medium Risk":
        rec = "Requires Manual Review"
    elif risk == "High Risk":
        rec = "Reject Molecule"
    else:
        rec = "Retry Input"

    return {
        "common_name": common_name,
        "iupac_name": iupac_name,
        "cid": cid,
        "formula": formula,
        "weight": weight,
        "smiles": smiles,
        "flags": flags,
        "risk": risk,
        "score": score,
        "recommendation": rec
    }