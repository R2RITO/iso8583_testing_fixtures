"""
Module containing the fixtures used to test iso8583 stream inputs.
Each fixture has a dictionary illustrating the fields in the stream,
the mti, the bitmap, and the stream used to test.
"""
from iso8583_fields import valid_fields

# Stream with valid mti, bitmap and fields
valid_stream = {
  'mti': '0200',
  'fields': valid_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923451546330530310110221138950595912076512555015additional6dataUSDDOP008reserved',
}

# Stream with a N field with characters
n_with_chars_stream = {
  'mti': '0200',
  'fields': n_with_chars_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923451546330530310110aG1138950595912076512555015additional6dataUSDDOP008reserved',
}

# Stream with a LL field having wrong size
ll_wrong_size_stream = {
  'mti': '0200',
  'fields': ll_wrong_size_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923451546330530310110221138950595912076512555010additional6dataUSDDOP008reserved',
}

# Stream with a date field having letters
date_letters_stream = {
  'mti': '0200',
  'fields': date_letters_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923AS15463305TT310110221138950595912076512555015additional6dataUSDDOP008reserved',
}

# Stream with a date field having invalid day (40th)
date_invalid_value_stream = {
  'mti': '0200',
  'fields': date_invalid_value_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923451546330540310110221138950595912076512555015additional6dataUSDDOP008reserved',
}

# Stream with a 29th february on a non-leap year
date_invalid_leap_stream = {
  'mti': '0200',
  'fields': date_invalid_leap_fields,
  'bitmap': 'f21a64018001c0020080000000000000',
  'stream': b'0200f21a64018001c002008000000000000016123123555403955522200400000003500020121923451546330525310110221138950595912076512555015additional6dataUSDDOP008reserved190229',
}

# Stream with a 29th february on a leap year
date_valid_leap_stream = {
  'mti': '0200',
  'fields': date_valid_leap_fields,
  'bitmap': 'f21a64018001c0020080000000000000',
  'stream': b'0200f21a64018001c002008000000000000016123123555403955522200400000003500020121923451546330525310110221138950595912076512555015additional6dataUSDDOP008reserved160229',
}

# Stream with extra data appended to the body at the end
# of the stream
data_at_end_stream = {
  'mti': '0200',
  'fields': data_at_end_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020121923451546330530310110221138950595912076512555015additional6dataUSDDOP008reserved1213qsfas12123asdASD12!@@@asf12',
}

# Stream with extra data inserted at the middle of the body
data_at_middle_stream = {
  'mti': '0200',
  'fields': data_at_middle_fields,
  'bitmap': '721a64018001c002',
  'stream': b'0200721a64018001c00216123123555403955522200400000003500020112312tasgadg21211111231afsfawq21923451546330530310110221138950595912076512555015additional6dataUSDDOP008reserved',
}

# Stream with a shorter body than the bitmap indicates
shorter_than_bitmap_stream = {
  'mti': '0200',
  'fields': shorter_than_bitmap_fields,
  'bitmap': '721a64018001c002',
  'stream': b'02007200640100018002161231235554039555222004000000035000201219234510221138950595912015additional6dataUSD008reserved',
}


# Revisar campos 28 29 30 31