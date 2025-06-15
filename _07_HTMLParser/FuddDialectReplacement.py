class FuddDialectReplacement:
    """convert HTML to Elmer Fudd-speak"""
    replacements = ((r'[rl]', r'w'),
                    (r'qu', r'qw'),
                    (r'th\b', r'f'),
                    (r'th', r'd'),
                    (r'n[.]', r'n, uh-hah-hah-hah.'))


#
#   Szwedzki kucharz, zobacz: Elmer Fudd-speak
#