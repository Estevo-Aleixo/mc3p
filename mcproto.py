from parsing import *

CLIENT_SIDE = 0
SERVER_SIDE = 1

#TYPE_WINDOW_CLICK = 11

cli_msgs = [None] * 256
srv_msgs = [None] * 256

cli_msgs[0x00] = \
srv_msgs[0x00] = defmsg(0x00,"Keep Alive",[])

cli_msgs[0x01] = defmsg(0x01,"Login Request",[
    ('proto_version',MC_int),
    ('username',MC_string),
    ('map_seed',MC_long),
    ('dimension',MC_byte)])
srv_msgs[0x01] = defmsg(0x01,"Login Response",[
    ('eid',MC_int),
    ('reserved',MC_string),
    ('map_seed',MC_long),
    ('dimension',MC_byte)])

cli_msgs[0x02] = defmsg(0x02,"Handshake",[
    ('username',MC_string)])
srv_msgs[0x02] = defmsg(0x02, "Handshake", [
    ('hash',MC_string)])

cli_msgs[0x03] = \
srv_msgs[0x03] = defmsg(0x03, "Chat",[
    ('chat_msg',MC_string)])

srv_msgs[0x04] = defmsg(0x04, "Time", [
    ('time',MC_long)])

cli_msgs[0x05] = \
srv_msgs[0x05] = defmsg(0x05, "Entity Equipment Spawn",[
    ('eid',MC_int),
    ('slot',MC_short),
    ('item_id',MC_short),
    ('unknown',MC_short)])

srv_msgs[0x06] = defmsg(0x06, "Spawn position",[
    ('x',MC_int),
    ('y',MC_int),
    ('z',MC_int)])

cli_msgs[0x07] = defmsg(0x07, "Use entity", [
    ('eid',MC_int),
    ('target_eid',MC_int),
    ('left_click',MC_bool)])

srv_msgs[0x08] = defmsg(0x08, "Update health", [
    ('health',MC_short)])

cli_msgs[0x09] = \
srv_msgs[0x09] = defmsg(0x09, "Respawn", [])

cli_msgs[0x0a] = defmsg(0x0a, "Player state", [
    ('on_ground',MC_bool)])

cli_msgs[0x0b] = \
srv_msgs[0x0b] = defmsg(0x0b, "Player position", [
    ('x',MC_double),
    ('y',MC_double),
    ('stance',MC_double),
    ('z',MC_double),
    ('on_ground',MC_bool)])

cli_msgs[0x0c] = defmsg(0x0c, "Player look", [
    ('yaw',MC_float),
    ('pitch',MC_float),
    ('on_ground',MC_bool)])

# Note the difference in ordering of 'stance'!
cli_msgs[0x0d] = defmsg(0x0d, "Player position and look",[
    ('x',MC_double),
    ('y',MC_double),
    ('stance',MC_double),
    ('z',MC_double),
    ('yaw',MC_float),
    ('pitch',MC_float),
    ('on_ground',MC_bool)])
srv_msgs[0x0d] = defmsg(0x0d, "Player position and look", [
    ('x',MC_double),
    ('stance',MC_double),
    ('y',MC_double),
    ('z',MC_double),
    ('yaw',MC_float),
    ('pitch',MC_float),
    ('on_ground',MC_bool)])

cli_msgs[0x0e] = \
srv_msgs[0x0e] = defmsg(0x0e, "Digging", [
    ('status',MC_byte),
    ('x',MC_int),
    ('y',MC_byte),
    ('z',MC_int),
    ('face',MC_byte)])

cli_msgs[0x0f] = \
srv_msgs[0x0f] = defmsg(0x0f, "Block placement", [
    ('x',MC_int),
    ('y',MC_byte),
    ('z',MC_int),
    ('dir',MC_byte),
    ('details',MC_item_details)])

cli_msgs[0x10] = \
srv_msgs[0x10] = defmsg(0x10, "Held item selection",[
    ('slot_id', MC_short)])

srv_msgs[0x11] = defmsg(0x11, "Use bed", [
    ('eid', MC_short),
    ('in_bed', MC_bool),
    ('x', MC_int),
    ('y', MC_byte),
    ('z', MC_int)])

cli_msgs[0x12] = \
srv_msgs[0x12] = defmsg(0x12, "Change animation",[
    ('eid',MC_int),
    ('animation',MC_byte)])

cli_msgs[0x13] = \
srv_msgs[0x13] = defmsg(0x13, "Entity action", [
    ('eid',MC_int),
    ('action', MC_byte)])

srv_msgs[0x14] = defmsg(0x14, "Entity spawn", [
    ('eid', MC_int),
    ('name', MC_string),
    ('x', MC_int),
    ('y', MC_int),
    ('z', MC_int),
    ('rotation', MC_byte),
    ('pitch', MC_byte),
    ('curr_item', MC_short)])

cli_msgs[0x15] = \
srv_msgs[0x15] = defmsg(0x15, "Pickup spawn", [
    ('eid',MC_int),
    ('item',MC_short),
    ('count',MC_byte),
    ('data',MC_short),
    ('x',MC_int),
    ('y',MC_int),
    ('z',MC_int),
    ('rotation',MC_byte),
    ('pitch',MC_byte),
    ('roll',MC_byte)])

srv_msgs[0x16] = defmsg(0x16, "Collect item", [
    ('item_eid',MC_int),
    ('collector_eid',MC_int)])

srv_msgs[0x17] = defmsg(0x17, "Add vehicle/object", [
    ('eid',MC_int),
    ('type',MC_byte),
    ('x',MC_int),
    ('y',MC_int),
    ('z',MC_int)])

srv_msgs[0x18] = defmsg(0x18, "Mob spawn", [
    ('eid',MC_int),
    ('mob_type',MC_byte),
    ('x',MC_int),
    ('y',MC_int),
    ('z',MC_int),
    ('yaw',MC_byte),
    ('pitch',MC_byte),
    ('metadata',parse_metadata)])

srv_msgs[0x19] = defmsg(0x19, "Painting", [
    ('eid', MC_int),
    ('title', MC_string),
    ('x', MC_int),
    ('y', MC_int),
    ('z', MC_int),
    ('type', MC_int)])

cli_msgs[0x1b] = \
srv_msgs[0x1b] = defmsg(0x1b, "???", [
    ('d1', MC_float),
    ('d2', MC_float),
    ('d3', MC_float),
    ('d4', MC_float),
    ('d5', MC_bool),
    ('d6', MC_bool)])

cli_msgs[0x1c] = \
srv_msgs[0x1c] = defmsg(0x1c, "Entity velocity", [
    ('eid',MC_int),
    ('vel_x',MC_short),
    ('vel_y',MC_short),
    ('vel_z',MC_short)])

srv_msgs[0x1d] = defmsg(0x1d, "Destroy entity", [
    ('eid',MC_int)])

srv_msgs[0x1e] = defmsg(0x1e, "Entity", [
    ('eid', MC_int)])

srv_msgs[0x1f] = defmsg(0x1f, "Entity relative move", [
    ('eid',MC_int),
    ('dx',MC_byte),
    ('dy',MC_byte),
    ('dz',MC_byte)])

srv_msgs[0x20] = defmsg(0x20, "Entity look", [
    ('eid', MC_int),
    ('yaw', MC_byte),
    ('pitch', MC_byte)])

srv_msgs[0x21] = defmsg(0x21, "Entity look/relative move", [
    ('eid',MC_int),
    ('dx',MC_byte),
    ('dy',MC_byte),
    ('dz',MC_byte),
    ('yaw',MC_byte),
    ('pitch',MC_byte)])

srv_msgs[0x22] = defmsg(0x22, "Entity teleport", [
    ('eid', MC_int),
    ('x', MC_int),
    ('y', MC_int),
    ('z', MC_int),
    ('yaw', MC_byte),
    ('pitch', MC_byte)])

srv_msgs[0x26] = defmsg(0x26, "Entity status", [
    ('eid',MC_int),
    ('status',MC_byte)])

cli_msgs[0x27] = \
srv_msgs[0x27] = defmsg(0x27, "Attach entity", [
    ('eid',MC_int),
    ('vehicle_id',MC_int)])

cli_msgs[0x28] = \
srv_msgs[0x28] = defmsg(0x28, "Entity metadata", [
    ('eid',MC_int),
    ('metadata',parse_metadata)])

srv_msgs[0x32] = defmsg(0x32, "Pre-chunk", [
    ('x',MC_int),
    ('z',MC_int),
    ('mode',MC_bool)])

srv_msgs[0x33] = defmsg(0x33, "Chunk", [
    ('x',MC_int),
    ('y',MC_short),
    ('z',MC_int),
    ('size_x',MC_byte),
    ('size_y',MC_byte),
    ('size_z',MC_byte),
    ('chunk',MC_chunk)])

cli_msgs[0x34] = \
srv_msgs[0x34] = defmsg(0x34, "Multi-block change", [
    ('chunk_x',MC_int),
    ('chunk_z',MC_int),
    ('changes',MC_multi_block_change)])

cli_msgs[0x35] = \
srv_msgs[0x35] = defmsg(0x35, "Block change", [
    ('x',MC_int),
    ('y',MC_byte),
    ('z',MC_int),
    ('block_type',MC_byte),
    ('block_metadata',MC_byte)])

srv_msgs[0x36] = defmsg(0x36, "Play note block",[
    ('x', MC_int),
    ('y', MC_short),
    ('z', MC_int),
    ('instrument_type', MC_byte),
    ('pitch', MC_byte)])

srv_msgs[0x3c] = defmsg(0x3c, "Explosion", [
    ('x', MC_double),
    ('y', MC_double),
    ('z', MC_double),
    ('unknown', MC_float),
    ('records', MC_explosion_records)])

cli_msgs[0x46] = \
srv_msgs[0x46] = defmsg(0x46, "New/Invalid State", [
    ('reason', MC_byte)])

srv_msgs[0x47] = defmsg(0x47, "Weather", [
    ('eid', MC_int),
    ('raining', MC_bool),
    ('x', MC_int),
    ('y', MC_int),
    ('z', MC_int)])

srv_msgs[0x64] = defmsg(0x64, "Open window", [
    ('window_id', MC_byte),
    ('inv_type', MC_byte),
    ('window_title', MC_string8),
    ('num_slots', MC_byte)])

cli_msgs[0x65] = \
srv_msgs[0x65] = defmsg(0x65, "Close window", [
    ('window_id', MC_byte)])

cli_msgs[0x66] = defmsg(0x66, "Window click", [
    ('window_id', MC_byte),
    ('slot', MC_short),
    ('is_right_click', MC_bool),
    ('action_num', MC_short),
    ('shift', MC_bool),
    ('details', MC_item_details)])

srv_msgs[0x67] = defmsg(0x67, "Set slot", [
    ('window_id',MC_byte),
    ('slot',MC_short),
    ('slot_update',MC_slot_update)])

srv_msgs[0x68] = defmsg(0x68, "Window items", [
    ('window_id',MC_byte),
    ('inventory',MC_inventory)])

srv_msgs[0x69] = defmsg(0x69, "Update progress bar", [
    ('window_id', MC_byte),
    ('progress_bar',MC_short),
    ('value',MC_short)])

cli_msgs[0x6a] = \
srv_msgs[0x6a] = defmsg(0x6a, "Transaction", [
    ('window_id', MC_byte),
    ('action_num', MC_short),
    ('accepted', MC_bool)])

cli_msgs[0x82] = \
srv_msgs[0x82] = defmsg(0x82, "Update sign", [
    ('x', MC_int),
    ('y', MC_short),
    ('z', MC_int),
    ('text1', MC_string),
    ('text2', MC_string),
    ('text3', MC_string),
    ('text4', MC_string)])

srv_msgs[0xc8] = defmsg(0xc8, "Increment statistic", [
    ('stat_id', MC_int),
    ('amount', MC_byte)])

cli_msgs[0xff] = \
srv_msgs[0xff] = defmsg(0xff, "Disconnect/Kick", [
    ('reason', MC_string)])


