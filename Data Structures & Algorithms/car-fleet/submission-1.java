class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] arr = new int[speed.length][2];
        for (int i = 0; i < speed.length; i++) {
            arr[i][0] = position[i];
            arr[i][1] = speed[i];
        }
        
        Arrays.sort(arr, (a, b) -> Integer.compare(b[0], a[0]));
        Stack<Double> stack = new Stack<>();
        for (int[] a : arr) {
            stack.push(((double) target - a[0]) / a[1]);
            if (stack.size() >= 2 && (stack.peek() <= stack.get(stack.size() - 2))) {
                stack.pop();
            }
        }
        return stack.size();
    }
}