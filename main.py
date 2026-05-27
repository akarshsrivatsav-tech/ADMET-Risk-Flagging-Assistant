from api_utils import get_cid, get_properties, get_smiles
from risk_engine import analyze_risk
from report_generator import print_report

# -----------------------------
# AUTO-CORRECTION DICTIONARY
# -----------------------------
corrections = {
    "asprin": "aspirin",
    "caffine": "caffeine",
    "ibuprofin": "ibuprofen",
    "paracetmol": "paracetamol"
}

def main():
    while True:
        molecule = input("\nEnter molecule (or exit): ").strip()

        # EXIT CONDITION
        if molecule.lower() == "exit":
            print("👋 Exiting program...")
            break

        # -----------------------------
        # AUTO-SUGGESTION FEATURE
        # -----------------------------
        if molecule.lower() in corrections:
            suggestion = corrections[molecule.lower()]
            print(f"💡 Did you mean: {suggestion}? Using corrected input.")
            molecule = suggestion

        # -----------------------------
        # REFLECTION LOGIC (RETRY)
        # -----------------------------
        cid = get_cid(molecule)

        if not cid:
            print("🔁 Retrying with lowercase...")
            cid = get_cid(molecule.lower())

        if not cid:
            print("🔁 Retrying with capitalized...")
            cid = get_cid(molecule.capitalize())

        # -----------------------------
        # FAILURE CASE
        # -----------------------------
        if not cid:
            print("❌ Molecule not found")
            print("💡 Tip: Check spelling or try common name (e.g., Aspirin)")
            continue

        # -----------------------------
        # FETCH DATA
        # -----------------------------
        data = get_properties(cid)

        if not data or 'PropertyTable' not in data:
            print("❌ Failed to fetch molecule data")
            continue

        smiles = get_smiles(cid)

        # -----------------------------
        # ANALYZE + REPORT
        # -----------------------------
        report = analyze_risk(molecule, cid, data, smiles)
        print_report(report)


if __name__ == "__main__":
    main()