
module overlay_fallback #(
    parameter DATA_WIDTH = 12
    parameter CHARACTER_SIZE = 32
)(
    input wire i_clk,
    input wire [DATA_WIDTH-1:0] i_data
    input wire i_vactive,
    input wire i_hactive,

    output wire [DATA_WIDTH-1:0] o_data,
    output wire o_vactive,
    output wire o_hactive
);

/*--------------------------- Local Parameters -------------------------------*/

    localparam ROM_LENGTH = 15;
    localparam MESSAGE_LENGTH = 23;
    
    initial if((CHARACTER_SIZE % 4) != 0) begin
        $(display "Error: CHARACTER_SIZE must be a multiple of 4!")
        $finish;
    end

    initial if(CHARACTER_SIZE < 32) begin
        $(display "Error: CHARACTER_SIZE must be at least 32!")
        $finish;
    end

/*--------------------------- Local Variables --------------------------------*/
    
    reg [63:0] character_rom [0:ROM_LENGTH-1];
    reg [clog2(ROM_LENGTH)-1:0] message_rom[0:MESSAGE_LENGTH-1];
    
    integer x;

/*-------------------------- ROM Initialization --------------s----------------*/    

    initial
    begin
        for(x = 0; x < ROM_LENGTH; x = x + 1)
            character_rom[x] = rom_lookup(x);
        
        for(x = 0; x < MESSAGE_LENGTH; x = x + 1)
            message_rom[x] = message_index(x);
    end
    
/*---------------------------- ROM Functions ---------------------------------*/

    function [63:0] rom_lookup;
        input integer value;
        begin
            case(value)
                0:  rom_lookup = 64'h0000000000000000;
                1:  rom_lookup = 64'h786c6666666c7800;
                2:  rom_lookup = 64'h00003c063e663e00;
                3:  rom_lookup = 64'h60607c6666667c00;
                4:  rom_lookup = 64'h00003c6060603c00;
                5:  rom_lookup = 64'h06063e6666663e00;
                6:  rom_lookup = 64'h00003c667e603c00;
                7:  rom_lookup = 64'h1c307c3030303000;
                8:  rom_lookup = 64'h1800181818180c00;
                9:  rom_lookup = 64'h6060666c786c6600;
                10: rom_lookup = 64'h1818181818180c00;
                11: rom_lookup = 64'h0000ecfed6c6c600;
                12: rom_lookup = 64'h00007c6666666600;
                13: rom_lookup = 64'h00003c6666663c00;
                14: rom_lookup = 64'h00006666663c1800;
                default: rom_lookup = 0;
            endcase
        end
    endfunction
    
    function integer message_index;
        input integer value;
        begin
            case(value)
                0:  message_index = 1;
                1:  message_index = 6;
                2:  message_index = 14;
                3:  message_index = 8;
                4:  message_index = 4;
                5:  message_index = 6;
                6:  message_index = 0;
                7:  message_index = 8;
                8:  message_index = 12;
                9:  message_index = 0;
                10: message_index = 7;
                11: message_index = 2;
                12: message_index = 10;
                13: message_index = 10;
                14: message_index = 3;
                15: message_index = 2;
                16: message_index = 4;
                17: message_index = 9;
                18: message_index = 0;
                19: message_index = 11;
                20: message_index = 13;
                21: message_index = 5;
                22: message_index = 6;
            endcase
        end
    endfunction

    function integer clog2;
        input integer value;
        begin
            if (value < 2)
                value = 2;

            value = value - 1;
            for (clog2 = 0; value > 0; clog2 = clog2 + 1)
                value = value >> 1;
        end
    endfunction
endmodule
