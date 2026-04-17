from Bio import PDB

def extract_residues(input_pdb, output_pdb, chain_id, start_res, end_res):
    """
    Extracts a range of residues from a specific chain in a PDB file.
    """
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('protein', input_pdb)
    
    class ResidueSelector(PDB.Select):
        def accept_residue(self, residue):
            res_id = residue.get_id()
            if residue.get_parent().id == chain_id and start_res <= res_id[1] <= end_res:
                return True
            return False

    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(output_pdb, ResidueSelector())
    print(f"Extracted residues {start_res}-{end_res} from chain {chain_id} to {output_pdb}")

if __name__ == "__main__":
    input_file = "outputs/P37840.pdb"
    output_file = "inputs/P37840_NAC.pdb"
    # Alpha-synuclein NAC domain: residues 61-95, Chain A
    extract_residues(input_file, output_file, 'A', 61, 95)
