class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr_line = []
        curr_len = 0
        
        for word in words:
            # Check if adding the current word exceeds maxWidth
            if curr_len + len(word) + len(curr_line) > maxWidth:
                # If exceeds, justify current line, starting new one
                total_spaces = maxWidth - curr_len
                gaps = len(curr_line) - 1
                
                if gaps == 0:
                    result.append(curr_line[0] + ' ' * total_spaces)
                else:
                    spaces_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = curr_line[0]
                    
                    for i in range(1, len(curr_line)):
                        # Distribute spaces evenly, putting extra spaces to the leftmost gaps
                        line += ' ' * (spaces_per_gap + (1 if i <= extra_spaces else 0)) + curr_line[i]
                    
                    result.append(line)
                
                # Reset for the next line
                curr_line = [word]
                curr_len = len(word)
            else:
                # Otherwise add word, if it can fit in current line
                curr_line.append(word)
                curr_len += len(word)
        
        # Left-justify last line
        last_line = ' '.join(curr_line).ljust(maxWidth)
        result.append(last_line)
        
        return result
