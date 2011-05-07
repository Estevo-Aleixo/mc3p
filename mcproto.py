from parsing import *

CLIENT_SIDE = 0
SERVER_SIDE = 1

#TYPE_WINDOW_CLICK = 11

client_packet_spec = {
    0x00: [],   # Keep-alive packet
    0x01: [('proto_version',MC_int),
           ('username',MC_string),
           ('password',MC_string),
           ('map_seed',MC_long),
           ('dimension',MC_byte)],
    0x02: [('username',MC_string)],
    0x03: [('chat_msg',MC_string)],
    0x05: [('eid',MC_int),
           ('slot',MC_short),
           ('item_id',MC_short),
           ('unknown',MC_short)],
    0x07: [('eid',MC_int),
           ('target_eid',MC_int),
           ('left_click',MC_bool)],
    0x09: [], # Respawnn packet
    0x0a: [('on_ground',MC_bool)],
    0x0b: [('x',MC_double),
           ('y',MC_double),
           ('stance',MC_double),
           ('z',MC_double),
           ('on_ground',MC_bool)],
    0x0c: [('yaw',MC_float),
           ('pitch',MC_float),
           ('on_ground',MC_bool)],
    0x0d: [('x',MC_double),
           ('y',MC_double),
           ('stance',MC_double),
           ('z',MC_double),
           ('yaw',MC_float),
           ('pitch',MC_float),
           ('on_ground',MC_bool)],
    0x0e: [('status',MC_byte),
           ('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('face',MC_byte)],
    0x0f: [('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('dir',MC_byte),
           ('id',MC_short),
           ('details',parse_item_details)],
    0x10: [('slot_id', MC_short)],
    0x12: [('eid',MC_int),
           ('animation',MC_byte)],
    0x13: [('eid',MC_int),
           ('action', MC_byte)],
    0x15: [('eid',MC_int),
           ('item',MC_short),
           ('count',MC_byte),
           ('data',MC_short),
           ('x',MC_int),
           ('y',MC_int),
           ('z',MC_int),
           ('rotation',MC_byte),
           ('pitch',MC_byte),
           ('roll',MC_byte)],
    0x1b: [('d1', MC_float),
           ('d2', MC_float),
           ('d3', MC_float),
           ('d4', MC_float),
           ('d5', MC_bool),
           ('d6', MC_bool)],
    0x1c: [('eid',MC_int),
           ('vel_x',MC_short),
           ('vel_y',MC_short),
           ('vel_z',MC_short)],
    0x27: [('eid',MC_int),
           ('vehicle_id',MC_int)],
    0x28: [('eid',MC_int),
           ('metadata',parse_metadata)],
    0x34: [('chunk_x',MC_int),
           ('chunk_z',MC_int),
           ('array_lengths',MC_short),
           ('arrays',parse_multi_block_change)],
    0x35: [('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('block_type',MC_byte),
           ('block_metadata',MC_byte)],
    0x65: [('window_id', MC_byte)],
    0x66: [('window_id', MC_byte),
           ('slot', MC_short),
           ('is_right_click', MC_bool),
           ('action_num', MC_short),
           ('item_id', MC_short),
           ('item_details', parse_item_details)],
    0x6a: [('window_id', MC_byte),
           ('action_num', MC_short),
           ('accepted', MC_bool)],
    0x82: [('x', MC_int),
           ('y', MC_short),
           ('z', MC_int),
           ('text1', MC_string),
           ('text2', MC_string),
           ('text3', MC_string),
           ('text4', MC_string)],
    0xff: [('reason', MC_string)]}

server_packet_spec = {
    0x00: [],
    0x01: [('eid',MC_int),
           ('reserved',MC_string),
           ('reserved',MC_string),
           ('map_seed',MC_long),
           ('dimension',MC_byte)],
    0x02: [('hash',MC_string)],
    0x03: [('chat_msg',MC_string)],
    0x04: [('time',MC_long)],
    0x05: [('eid', MC_int),
           ('slot_id', MC_short),
           ('item_id', MC_short),
           ('unknown', MC_short)],
    0x06: [('x',MC_int),
           ('y',MC_int),
           ('z',MC_int)],
    0x08: [('health',MC_short)],
    0x0b: [('x',MC_double),
           ('y',MC_double),
           ('stance',MC_double),
           ('z',MC_double),
           ('on_ground',MC_bool)],
    0x0d: [('x',MC_double),
           ('stance',MC_double),
           ('y',MC_double),
           ('z',MC_double),
           ('yaw',MC_float),
           ('pitch',MC_float),
           ('on_ground',MC_bool)],
    0x0e: [('status',MC_byte),
           ('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('face',MC_byte)],
    0x0f: [('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('dir',MC_byte),
           ('id',MC_short),
           ('details',parse_item_details)],
    0x10: [('slot_id', MC_short)],
    0x11: [('eid', MC_int),
           ('unknown', MC_byte),
           ('x', MC_int),
           ('y', MC_byte),
           ('z', MC_int)],
    0x12: [('eid',MC_int),
           ('animation',MC_byte)],
    0x13: [('eid',MC_int),
           ('action', MC_byte)],
    0x14: [('eid', MC_int),
           ('name', MC_string),
           ('x', MC_int),
           ('y', MC_int),
           ('z', MC_int),
           ('rotation', MC_byte),
           ('pitch', MC_byte),
           ('curr_item', MC_short)],
    0x15: [('eid',MC_int),
           ('item',MC_short),
           ('count',MC_byte),
           ('data',MC_short),
           ('x',MC_int),
           ('y',MC_int),
           ('z',MC_int),
           ('rotation',MC_byte),
           ('pitch',MC_byte),
           ('roll',MC_byte)],
    0x16: [('item_eid',MC_int),
           ('collector_eid',MC_int)],
    0x17: [('eid',MC_int),
           ('type',MC_byte),
           ('x',MC_int),
           ('y',MC_int),
           ('z',MC_int)],
    0x18: [('eid',MC_int),
           ('mob_type',MC_byte),
           ('x',MC_int),
           ('y',MC_int),
           ('z',MC_int),
           ('yaw',MC_byte),
           ('pitch',MC_byte),
           ('metadata',parse_metadata)],
    0x19: [('eid', MC_int),
           ('title', MC_string),
           ('x', MC_int),
           ('y', MC_int),
           ('z', MC_int),
           ('type', MC_int)],
    0x1b: [('d1', MC_float),
           ('d2', MC_float),
           ('d3', MC_float),
           ('d4', MC_float),
           ('d5', MC_bool),
           ('d6', MC_bool)],
    0x1c: [('eid',MC_int),
           ('vel_x',MC_short),
           ('vel_y',MC_short),
           ('vel_z',MC_short)],
    0x1d: [('eid',MC_int)],
    0x1e: [('eid', MC_int)],
    0x1f: [('eid',MC_int),
           ('dx',MC_byte),
           ('dy',MC_byte),
           ('dz',MC_byte)],
    0x20: [('eid', MC_int),
           ('yaw', MC_byte),
           ('pitch', MC_byte)],
    0x21: [('eid',MC_int),
           ('dx',MC_byte),
           ('dy',MC_byte),
           ('dz',MC_byte),
           ('yaw',MC_byte),
           ('pitch',MC_byte)],
    0x22: [('eid', MC_int),
           ('x', MC_int),
           ('y', MC_int),
           ('z', MC_int),
           ('yaw', MC_byte),
           ('pitch', MC_byte)],
    0x26: [('eid',MC_int),
           ('status',MC_byte)],
    0x27: [('eid', MC_int),
           ('vehicle_id', MC_int)],
    0x28: [('eid',MC_int),
           ('metadata',parse_metadata)],
    0x32: [('x',MC_int),             # Pre-chunk
           ('z',MC_int),
           ('mode',MC_bool)],
    0x33: [('x',MC_int),             # Chunk
           ('y',MC_short),
           ('z',MC_int),
           ('size_x',MC_byte),
           ('size_y',MC_byte),
           ('size_z',MC_byte),
           ('chunk',MC_chunk)],
    0x34: [('chunk_x',MC_int),
           ('chunk_z',MC_int),
           ('array_lengths',MC_short),
           ('arrays',parse_multi_block_change)],
    0x35: [('x',MC_int),
           ('y',MC_byte),
           ('z',MC_int),
           ('block_type',MC_byte),
           ('block_metadata',MC_byte)],
    0x36: [('x', MC_int),
           ('y', MC_short),
           ('z', MC_int),
           ('instrument_type', MC_byte),
           ('pitch', MC_byte)],
    0x3c: [('x', MC_double),
           ('y', MC_double),
           ('z', MC_double),
           ('unknown', MC_float),
           ('count', MC_int),
           ('records', parse_explosion_record)],
    0x64: [('window_id', MC_byte),
           ('inv_type', MC_byte),
           ('window_title', MC_string),
           ('num_slots', MC_byte)],
    0x65: [('window_id', MC_byte)],
    0x67: [('window_id',MC_byte),
           ('slot',MC_short),
           ('slot_update',MC_slot_update)],
    0x68: [('window_id',MC_byte),
           ('inventory',MC_inventory)],
    0x69: [('window_id', MC_byte),
           ('progress_bar',MC_short),
           ('value',MC_short)],
    0x6a: [('window_id', MC_byte),
           ('action_num', MC_short),
           ('accepted', MC_bool)],
    0x82: [('x', MC_int),
           ('y', MC_short),
           ('z', MC_int),
           ('text1', MC_string),
           ('text2', MC_string),
           ('text3', MC_string),
           ('text4', MC_string)],
    0xff: [('reason', MC_string)]}

packet_spec = [ client_packet_spec, server_packet_spec ]


