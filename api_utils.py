import requests
import urllib.parse

def get_cid(name):
    try:
        name = urllib.parse.quote(name)
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON"

        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()
            return data['IdentifierList']['CID'][0]
    except:
        return None

    return None


def get_properties(cid):
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight,IUPACName/JSON"

        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            return res.json()
    except:
        return None

    return None


def get_smiles(cid):
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/record/JSON"

        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()
            compounds = data.get("PC_Compounds", [])

            if compounds:
                for prop in compounds[0].get("props", []):
                    if prop.get("urn", {}).get("label") == "SMILES":
                        return prop.get("value", {}).get("sval", "Not Available")
    except:
        pass

    return "Not Available"