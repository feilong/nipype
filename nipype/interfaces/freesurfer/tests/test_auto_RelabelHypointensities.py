# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import RelabelHypointensities


def test_RelabelHypointensities_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    aseg=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    lh_white=dict(mandatory=True,
    ),
    out_file=dict(argstr='%s',
    genfile=True,
    mandatory=False,
    position=-1,
    ),
    rh_white=dict(mandatory=True,
    ),
    subjects_dir=dict(),
    surf_directory=dict(argstr='%s',
    genfile=True,
    mandatory=False,
    position=-2,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = RelabelHypointensities.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_RelabelHypointensities_outputs():
    output_map = dict(out_file=dict(argstr='%s',
    mandatory=False,
    ),
    )
    outputs = RelabelHypointensities.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
