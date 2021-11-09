using System;

namespace Solution
{
    public static class Program
    {
        public static string StringsSum (string s1, string s2)
        {
            int sum = 0;
            string[] strings = {s1, s2};
            foreach (string i in strings)
            {
                int curr_num;

                if (String.IsNullOrEmpty(i))
                {
                    curr_num = 0;
                }
                else
                {
                    curr_num = Convert.ToInt32(i);
                }
                sum += curr_num;
            }
            return sum.ToString();
        }
    }
}
