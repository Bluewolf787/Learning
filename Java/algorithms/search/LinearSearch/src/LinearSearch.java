public class LinearSearch
{
    public static void main(String[] args)
    {
        int[] list_numbers = {1, 5, 2, 14, 23, 32, 12, 8, 3, 9, 0, 6};
        int value = 8;

        int index = linearSearch(list_numbers, value);

        System.out.println("The value is in the list at index " + index);
    }

    static int linearSearch(int[] data, int value)
    {
        for (int i = 0; i < data.length; i++)
        {
            if (data[i] == value)
            {
                return i;
            }
        }

        return -1;
    }
}