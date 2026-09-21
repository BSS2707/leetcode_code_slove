class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ('+', '-'):
                # A sign is only valid at the start or immediately after an exponent ('e' or 'E')
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            elif char in ('e', 'E'):
                # An exponent is valid only if we haven't seen one yet AND we've already seen a digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because the exponent MUST be followed by new digit(s)
                seen_digit = False
            elif char == '.':
                # A dot is valid only if we haven't seen a dot OR an exponent yet
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # Any other character (letters other than e/E, special chars) is invalid
                return False
                
        # Must have encountered at least one digit (either before or after 'e'/'E')
        return seen_digit