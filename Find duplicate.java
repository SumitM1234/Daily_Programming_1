public class FindDuplicate {
    public static int findDuplicate(int[] nums) {
       
        int tortoise = nums[0];
        int hare = nums[0];
        
       
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);
        
        
        int finder = nums[0];
        while (finder != tortoise) {
            finder = nums[finder];
            tortoise = nums[tortoise];
        }
        
        return finder;
    }

    public static void main(String[] args) {
      
        int[] arr = {3, 1, 3, 4, 2};
        int duplicate = findDuplicate(arr);
        System.out.println("Duplicate Number: " + duplicate);
    }
}
