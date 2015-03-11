"""Font ROMs for use in the Verilog Text Maker."""

class BasicFontRom(object):

    """ Basic 8x8 font ROM. Has an NES look-and-feel. Entries in the font ROM
    can be converted into 2-D pixel arrays by converting them to binary
    and scanning them from left to right, up to down. A properly-mapped sprite
    would be:
                            VALUE[63:56]
                            VALUE[55:48]
                            VALUE[47:40]
                            VALUE[39:32]
                            VALUE[31:24]
                            VALUE[23:16]
                            VALUE[15:8]
                            VALUE[7:0]
    """

    def __init__(self):
        self.font_rom = [
            0x0000000000000000, 0x1818181818001800, 0x6c6c000000000000,
            0x6c6cfe6cfe6c6c00, 0x183e603c067c1800, 0x0066acd8366acc00,
            0x386c6876dcce7b00, 0x1818300000000000, 0x0c18303030180c00,
            0x30180c0c0c183000, 0x00663cff3c660000, 0x0018187e18180000,
            0x0000000000181830, 0x0000007e00000000, 0x0000000000181800,
            0x03060c183060c000, 0x3c666e7e76663c00, 0x1838781818181800,
            0x3c66060c18307e00, 0x3c66061c06663c00, 0x1c3c6cccfe0c0c00,
            0x7e607c0606663c00, 0x1c30607c66663c00, 0x7e06060c18181800,
            0x3c66663c66663c00, 0x3c66663e060c3800, 0x0018180000181800,
            0x0018180000181830, 0x0006186018060000, 0x00007e007e000000,
            0x0060180618600000, 0x3c66060c18001800, 0x3c665a5a5e603c00,
            0x3c66667e66666600, 0x7c66667c66667c00, 0x1e30606060301e00,
            0x786c6666666c7800, 0x7e60607860607e00, 0x7e60607860606000,
            0x3c66606e66663e00, 0x6666667e66666600, 0x3c18181818183c00,
            0x0606060606663c00, 0xc6ccd8f0d8ccc600, 0x6060606060607e00,
            0xc6eefed6c6c6c600, 0xc6e6f6decec6c600, 0x3c66666666663c00,
            0x7c66667c60606000, 0x78ccccccccdc7e00, 0x7c66667c6c666600,
            0x3c66703c0e663c00, 0x7e18181818181800, 0x6666666666663c00,
            0x666666663c3c1800, 0xc6c6c6d6feeec600, 0xc3663c183c66c300,
            0xc3663c1818181800, 0xfe0c183060c0fe00, 0x3c30303030303c00,
            0xc06030180c060300, 0x3c0c0c0c0c0c3c00, 0x183c660000000000,
            0x000000000000fc00, 0x18180c0000000000, 0x00003c063e663e00,
            0x60607c6666667c00, 0x00003c6060603c00, 0x06063e6666663e00,
            0x00003c667e603c00, 0x1c307c3030303000, 0x00003e66663e063c,
            0x60607c6666666600, 0x1800181818180c00, 0x0c000c0c0c0c0c78,
            0x6060666c786c6600, 0x1818181818180c00, 0x0000ecfed6c6c600,
            0x00007c6666666600, 0x00003c6666663c00, 0x00007c66667c6060,
            0x00003e66663e0606, 0x00007c6660606000, 0x00003c603c067c00,
            0x30307c3030301c00, 0x0000666666663e00, 0x00006666663c1800,
            0x0000c6c6d6fe6c00, 0x0000c66c386cc600, 0x00006666663c1830,
            0x00007e0c18307e00, 0x0c18183018180c00, 0x1818181818181800,
            0x3018180c18183000, 0x0076dc0000000000, 0x0000000000000000
        ]

    def display_char(self, char):
        """ Returns a pixelized display of an ASCII character. Only characters
        ' ' through '~' are supported. """

        rom_entry = ord(char) - ord(' ')
        return self.generate_pixels(rom_entry)

    def generate_pixels(self, entry, lookup = True):
        """ Generates a pixelized display of one entry in the font ROM. Active
        pixels are represented as '1', and inactive pixels are represented as
        ' '. If 'lookup' is true, the 'entry' value represents an index into
        the ROM table. If 'lookup' is false, 'entry' represents the 64-bit
        unsigned integer constant. """

        if lookup:
            value = self.font_rom[entry]
        else:
            value = entry
        
        value = bin(value)[2:].zfill(64)
        value = value.replace('0', ' ')
        pixels = [value[x:x + 8] for x in range(0, 64, 8)]
        return pixels

    def display_entry(self, char):
        """ Returns the ROM entry that corresponds with target character. """

        entry = ord(char) - ord(' ')
        return self.font_rom[entry]
    
    def custom_rom(self, string):
        """ Creates a custom ROM that only contains the necessary characters 
        to produce a given input string. Returns the custom ROM, and also
        an list of indexes into the ROM for each character in the input
        string. """
        
        unique_chars = set(string)
        unique_chars = list(unique_chars)
        unique_chars.sort()
        custom_rom = [self.font_rom[ord(x) - ord(' ')] for x in unique_chars]
        
        rom_index = []
        
        for x in string:
            rom_index.append(unique_chars.index(x))
        
        return custom_rom, rom_index

