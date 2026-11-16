class Solution:
    # Define a method that takes a string 's' and returns a string
    def removeDuplicates(self, s: str) -> str:
        # Initialize an empty list to act as a stack for keeping track of characters
        res = []
        
        # Loop through each character 'c' in the input string 's' (fixed from uppercase 'S')
        for c in s:
            # Check if the list is not empty AND the last added character matches the current character
            if res and res[-1] == c:
                # If they match, remove the last character from the list (removes the duplicate pair)
                res.pop()
            else:
                # Otherwise, add the current character to the end of the list
                res.append(c)
                
        # Join all remaining characters in the list back into a single string and return it
        return "".join(res)
