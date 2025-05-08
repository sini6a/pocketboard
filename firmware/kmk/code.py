import microcontroller.pin as board # type: ignore
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

print("Starting")

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Define the GPIO pin you want to control
pin_to_toggle = digitalio.DigitalInOut(board.GPIO12)  # Replace with your pin number
pin_to_toggle.direction = digitalio.Direction.OUTPUT
pin_to_toggle.value = True  # Start with the pin LOW

# Define your keyboard matrix and configuration
keyboard.col_pins = (
    board.GPIO21, board.GPIO20, board.GPIO19, board.GPIO18, board.GPIO22,
    board.GPIO11, board.GPIO10, board.GPIO9, board.GPIO8, board.GPIO7
)
keyboard.row_pins = (
    board.GPIO23, board.GPIO24, board.GPIO26, board.GPIO6
)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Define the keymap
keyboard.keymap = [
    [
        KC.Q                , KC.W                , KC.E               , KC.R               , KC.T                  , KC.Y              , KC.U               , KC.I               , KC.O                , KC.P,
        KC.A                , KC.S                , KC.D               , KC.F               , KC.G                  , KC.H              , KC.J               , KC.K               , KC.L                , KC.SCLN,
        KC.Z                , KC.X                , KC.C               , KC.V               , KC.B                  , KC.N              , KC.M               , KC.COMMA           , KC.DOT              , KC.SLSH,
        KC.NO               , KC.NO               , KC.ESC             , KC.SPC             , KC.TAB                , KC.ENTER          , KC.BACKSPACE       , KC.DEL             , KC.NO               , KC.NO
    ],
]

if __name__ == '__main__':
    keyboard.go()

"""     [1] = LAYOUT_qwerty( // nav layer
        KC_NO,      KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_AGIN,   KC_PASTE,   KC_COPY,   KC_CUT,   KC_UNDO,             KC_NO,
        KC_NO,  KC_LGUI,   KC_LALT,   KC_LCTL,   KC_LSFT,   KC_NO,         KC_CAPS,   KC_LEFT,   KC_DOWN,   KC_UP,   KC_RIGHT,     KC_NO,
        KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_INS,   KC_HOME,   KC_PAGE_DOWN,   KC_PAGE_UP,   KC_END,    KC_NO,
                                   KC_NO, KC_NO, KC_NO,         KC_ENTER, KC_BACKSPACE, KC_DELETE
    ),
    [2] = LAYOUT_qwerty( // function layer
        QK_BOOT,      KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,         KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,             KC_NO,
        KC_NO,     KC_F12,   KC_F7,   KC_F8,   KC_F9,   KC_PSCR,         KC_NO,   KC_NO,   KC_NO,   KC_F11,   KC_F12,             KC_NO,
        KC_NO,     KC_F11,   KC_F4,   KC_F5,   KC_F6,   KC_SCRL,         KC_NO,   KC_RSFT,   KC_RCTL,   KC_RALT,   KC_RGUI,     KC_NO,
        KC_NO,     KC_F10,   KC_F1,   KC_F2,   KC_F3,   KC_PAUS,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,    KC_NO,
                                         KC_APP, KC_SPC, KC_TAB,         KC_NO, KC_NO, KC_NO
    ),
    [3] = LAYOUT_qwerty( // number layer
        KC_NO,      KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,     KC_LBRC,   KC_7,   KC_8,   KC_9,   KC_RCBR,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,     KC_SCLN,   KC_4,   KC_5,   KC_6,   KC_EQL,         KC_NO,   KC_RSFT,   KC_RCTL,   KC_RALT,   KC_RGUI,     KC_NO,
        KC_NO,     KC_COMM,   KC_1,   KC_2,   KC_3,   KC_BSLS,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,    KC_NO,
                                         KC_DOT, KC_0, KC_MINUS,         KC_NO, KC_NO, KC_NO
    ),
    [4] = LAYOUT_qwerty( // symbol layer
        KC_NO,      KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,     KC_LCBR,   KC_AMPR,   KC_ASTR,   KC_LPRN,   KC_RCBR,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,     KC_COLN,   KC_DLR,   KC_PERC,   KC_CIRC,   KC_PLUS,         KC_NO,   KC_RSFT,   KC_RCTL,   KC_RALT,   KC_RGUI,     KC_NO,
        KC_NO,     KC_TILD,   KC_EXLM,   KC_AT,   KC_HASH,   KC_PIPE,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,    KC_NO,
                                         KC_LPRN, KC_RPRN, KC_UNDS,         KC_NO, KC_NO, KC_NO
    ),
    [5] = LAYOUT_qwerty( // media layer
        KC_NO,      KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,     KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         RGB_TOG,   RGB_MOD,   RGB_HUI,   RGB_SAI,   RGB_VAI,             KC_NO,
        KC_NO,     KC_LGUI,   KC_LALT,   KC_LCTL,   KC_LSFT,   KC_NO,         KC_NO,   KC_MPRV,   KC_VOLD,   KC_VOLU,   KC_MNXT,     KC_NO,
        KC_NO,     KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
                                         KC_NO, KC_NO, KC_NO,         KC_MSTP, KC_MPLY, KC_MUTE
    ),
    [6] = LAYOUT_qwerty( // mouse layer
        KC_NO,      KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,             KC_NO,
        KC_NO,         KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_AGIN,   KC_PASTE,   KC_COPY,   KC_CUT,   KC_UNDO,             KC_NO,
        KC_NO,  KC_LGUI,   KC_LALT,   KC_LCTL,   KC_LSFT,   KC_NO,         KC_NO,   KC_MS_L,   KC_MS_D,   KC_MS_U,   KC_MS_R,     KC_NO,
        KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,         KC_NO,   KC_WH_L,   KC_WH_D,   KC_WH_U,   KC_WH_R,    KC_NO,
                                   KC_NO, KC_NO, KC_NO,         KC_BTN2, KC_BTN1, KC_BTN3
    )
 """