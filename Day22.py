# Function to reverse the words of the given string
def reverse_sentence(s):
    # Create an empty string stack
    stack = []
    # Create an empty temporary string
    temp = ""
    # Traversing the entire string
    for i in range(len(s)):
        if s[i] == " ":
            # Push the temporary variable into the stack
            stack.append(temp)
            # Assigning temporary variable as empty
            temp = ""
        else:
            temp += s[i]
    # For the last word of the string
    stack.append(temp)

    while len(stack) != 0:
        # Get the words in reverse order
        temp = stack[-1]
        print(temp,end=" ")
        stack.pop()
    print()

def insert_at_bottom(st,ele):
    # base case
    if len(st) == 0:
        st.append(ele)
        return

    topele = st[-1]
    st.pop()
    insert_at_bottom(st,ele)
    st.append(topele)

def reverse(st):
    if len(st) == 0:
        return

    ele = st[-1]
    st.pop()
    reverse(st)
    insert_at_bottom(st,ele)


# Driver code
s = "Hey, How are you doing?"
print(s)
reverse_sentence(s)

stack = [1,2,3,4,5]
reverse(stack)
while len(stack) != 0:
    print(stack[-1],end=" ")
    stack.pop()
print()
