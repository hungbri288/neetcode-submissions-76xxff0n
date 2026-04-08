class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        map.put(']', '[');
        map.put('}', '{');
        map.put(')', '(');

        for (Character c : s.toCharArray()) {
            if (!stack.isEmpty() && map.containsKey(c)) {
                if (stack.peek() == map.get(c)) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
