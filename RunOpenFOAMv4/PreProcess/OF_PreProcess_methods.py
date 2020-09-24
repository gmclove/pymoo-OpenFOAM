def OF_header(obj, clas='dictionary', ver='2.0', form='ascii'):
    return """
/*--------------------------------*- C++ -*----------------------------------*
| =========                |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  5                                     |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     %s;
    format      %s;
    class       %s;
    object      %s;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
""" % (obj, clas, ver, form)


def OF_decomposeParDict(nProc, method='scotch'):
    return OF_header('decomposeParDict') + '''
numberOfSubdomains %i;

method          %s;

// ************************************************************************* //
''' % (nProc, method)


def OF_fvSchemes(ddtSchemes='steadyState', gradSchemes='Gauss linear'):
    return OF_header('fvSchemes') + '''
ddtSchemes
{
    default         %s;
}

gradSchemes
{
    default         %s;
}

divSchemes
{
    default         none;
    div(phi,U)      bounded Gauss linearUpwind grad(U);
    div(phi,nuTilda) bounded Gauss linearUpwind grad(nuTilda);
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}

laplacianSchemes
{
    default         Gauss linear corrected;
}

interpolationSchemes
{
    default         linear;
}

snGradSchemes
{
    default         corrected;
}

wallDist
{
    method meshWave;
}


// ************************************************************************* //
''' % (ddtSchemes, gradSchemes)

# print(OF_decomposeParDict(2))
# def OF_parameters():
# def OF_vetices():
# def OF_boundaries():
