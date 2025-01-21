import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP21,  # column
    source=board.GP23,  # row
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('Datakonsulten', 'Pocketboard v1.0'),
)
