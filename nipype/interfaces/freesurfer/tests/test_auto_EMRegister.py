# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..registration import EMRegister


def test_EMRegister_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    mask=dict(argstr='-mask %s',
    mandatory=False,
    ),
    nbrspacing=dict(argstr='-uns %d',
    mandatory=False,
    ),
    num_threads=dict(),
    out_file=dict(argstr='%s',
    genfile=True,
    mandatory=True,
    position=-1,
    ),
    skull=dict(argstr='-skull',
    ),
    subjects_dir=dict(),
    template=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    terminal_output=dict(nohash=True,
    ),
    transform=dict(argstr='-t %s',
    mandatory=False,
    ),
    )
    inputs = EMRegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_EMRegister_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = EMRegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
