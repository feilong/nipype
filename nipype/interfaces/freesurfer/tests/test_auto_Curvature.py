# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import Curvature


def test_Curvature_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    averages=dict(argstr='-a %d',
    mandatory=False,
    ),
    distances=dict(argstr='-distances %d %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    n=dict(argstr='-n',
    mandatory=False,
    ),
    save=dict(argstr='-w',
    mandatory=False,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='-thresh %.3f',
    mandatory=False,
    ),
    )
    inputs = Curvature.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Curvature_outputs():
    output_map = dict(out_gauss=dict(),
    out_mean=dict(),
    )
    outputs = Curvature.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
