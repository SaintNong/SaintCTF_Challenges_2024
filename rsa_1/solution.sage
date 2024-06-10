"""
Unfortunately I could not find an adequate cube root function without Sage
so uh yeah, we're using Sage. Deal with it.
"""

c = 11261436105713051634335989902250445470916241105234706384618386302967523437018194236326664674511867558627864775944927181963929276163247230157632232115529458940960065559764985169479574116164170814436682068104330472313985130535812696066347911454588837354890625000



# Since m and e is too small for N, N is never reached when raising m^e.
# Therefore m is literally just the cuberoot of c.

# Recover m
m = c.nth_root(3)

# Get flag from bytes
m_int = int(m)
message_bytes = m_int.to_bytes((m_int.bit_length() + 7) // 8, 'big')
print(message_bytes.decode())
