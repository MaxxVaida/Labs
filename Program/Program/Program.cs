using System;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {

                TRectangle r1 = new TRectangle(5, 3);
                TRectangle r2 = new TRectangle(10, 6);
                Console.WriteLine($"r1: {r1}");
                Console.WriteLine($"r2: {r2}");
                Console.WriteLine($"Square of r1 = {r1.getSquare()}");
                Console.WriteLine($"Perimeter of r1 = {r1.getPerimeter()}");
                Console.WriteLine("");

                TParallelepiped prp1 = new TParallelepiped(5, 3, 10);
                Console.WriteLine($"Parallelepiped: {prp1}");
                Console.WriteLine($"Volume of prp1 = {prp1.getVolume()}");
                Console.WriteLine("");

                Console.WriteLine($"r1+r2: {r1 + r2}");
                Console.WriteLine($"r2-r1: {r2 - r1}");
                Console.WriteLine($"{r1 * 10}");
                Console.WriteLine("");
                Console.WriteLine($"r1 = r2: { r1 == r2}");
        }
    }
}
