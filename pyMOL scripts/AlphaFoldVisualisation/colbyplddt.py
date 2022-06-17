from pymol import cmd


def colbyplddt(selection="all"):

    """
    AUTHOR
    Bhoomika Basu Mallik
    DESCRIPTION
    Colors Alphafold structures by pLDDT
    USAGE
    colbyplddt sele
    PARAMETERS
    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b > 90")
    cmd.color("cyan", f"({selection}) and b < 90 and b > 70")
    cmd.color("yellow", f"({selection}) and b < 70 and b > 50")
    cmd.color("orange", f"({selection}) and b < 50")


cmd.extend("colbyplddt", colbyplddt)
cmd.auto_arg[0]["colbyplddt"] = [cmd.object_sc, "object", ""]