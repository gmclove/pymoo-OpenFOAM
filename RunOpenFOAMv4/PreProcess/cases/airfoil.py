### blockMeshDic airfoil
# Header
af_bMD0 = """
/*--------------------------------*- C++ -*----------------------------------*
| =========                |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  5                                     |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

convertToMeters 1;
"""
# Vertices
af_bMD1 = """
convertToMeters 1;

vertices
(
    ($pc	$rNeg 	$minZ)		// point 0
    (1.0 	$rNeg 	$minZ)		// point 1
    ($l 	$rNeg 	$minZ)		// point 2
    ($pc 	$ypcNeg	$minZ)		// point 3
    ($rNeg 	0.0		$minZ)		// point 4
    (0.0 	0.0		$minZ)		// point 5
    (1.0	0.0		$minZ)		// point 6
    ($l 	0.0		$minZ)		// point 7
    ($pc 	$ypcPos	$minZ)		// point 8
    ($pc 	$rPos	$minZ)		// point 9
    (1.0	$rPos	$minZ)		// point 10
    ($l 	$rPos	$minZ)		// point 11

    ($pc	$rNeg 	$maxZ)		// point 12
    (1.0 	$rNeg 	$maxZ)		// point 13
    ($l 	$rNeg 	$maxZ)		// point 14
    ($pc 	$ypcNeg	$maxZ)		// point 15
    ($rNeg 	0.0		$maxZ)		// point 16
    (0.0 	0.0		$maxZ)		// point 17
    (1.0	0.0		$maxZ)		// point 18
    ($l 	0.0		$maxZ)		// point 19
    ($pc 	$ypcPos	$maxZ)		// point 20
    ($pc 	$rPos	$maxZ)		// point 21
    (1.0	$rPos	$maxZ)		// point 22
    ($l 	$rPos	$maxZ)		// point 23
);\n """

# Blocks
af_bMD2 = """
blocks
(
    hex (17 15 12 16 5 3 0 4) 	($Npre 		$Ny 	$Nz) 	simpleGrading 		// block 0
    ( 
        (
            (0.5 0.65 $pre1)
            (0.5 0.35 $pre2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
    hex (5 8 9 4 17 20 21 16) 	($Npre 		$Ny 	$Nz) 	simpleGrading 		// block 1
    ( 
        (
            (0.5 0.65 $pre1)
            (0.5 0.35 $pre2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
    hex (15 18 13 12 3 6 1 0) 	($Npost 	$Ny 	$Nz) 	simpleGrading 		// block 2
    ( 
        (
            (0.5 0.45 $post1)
            (0.5 0.55 $post2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
    hex (8 6 10 9 20 18 22 21) 	($Npost 	$Ny 	$Nz) 	simpleGrading 		// block 3
    ( 
        (
            (0.5 0.45 $post1)
            (0.5 0.55 $post2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
    hex (18 19 14 13 6 7 2 1) 	($Nwake 	$Ny 	$Nz) 	simpleGrading 		// block 4
    ( 
        (
            (1 1 $wake)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
    hex (6 7 11 10 18 19 23 22)	($Nwake 	$Ny 	$Nz) 	simpleGrading 		// block 5
    ( 
        (
            (1 1 $wake)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
            (1 1 $zDir)
        )
    )
); \n
"""

# Edges are included below

# Boundary
af_bMD3 = """
boundary
(
    inlet
    {
        type patch;
        faces
        (
            (9 21 16 4)
            (4 16 12 0)
        );
    }   

    outlet
    {
        type patch;
        faces
        (
            (23 11 7 19)
            (19 7 2 14)
        );
    }   


    airfoil
    {
        type wall;
        faces
        (
            (8 20 18 6)
            (6 18 15 3)
            (17 5 3 15)
            (20 8 5 17)
        );
    }   

    lower
    {
        type patch;
        faces
        (
            (0 12 13 1)
            (1 13 14 2)
        );
    }   

    upper
    {
        type patch;
        faces
        (
            (21 9 10 22)
            (22 10 11 23)
        );
    }

);

// ************************************************************************* //
"""

