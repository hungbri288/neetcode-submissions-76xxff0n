class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > stack.peek()[0]) {
                int[] temp = stack.pop();
                res[temp[1]] = i - temp[1];
            }
            stack.push(new int[] {temperatures[i], i});
        }
        return res;
    }
}
