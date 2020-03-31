using System;
using System.Collections.Generic;
using System.Text;

namespace Program
{
    class TRectangle
    {
        public double A { get; set; }
        public double B { get; set; }
        public TRectangle(double a, double b)
        {
            A = a;
            B = b;
        }
        public TRectangle(double a)
        {
            A = a;
            B = a;
        }
        public TRectangle()
        {
            A = 1;
            B = 1;
        }
        public double getSquare()
        {
            return A * B;
        }
        public double getPerimeter()
        {
            return 2 * (A + B);
        }
        public double getLarger()
        {
            if (A > 5 && B > 5)
                return A;
            else
                return B;
        }
        public static TRectangle operator +(TRectangle r1, TRectangle r2)
        {
            return new TRectangle(r1.A + r2.A, r1.B + r2.B);
        }
        public static TRectangle operator -(TRectangle r1, TRectangle r2)
        {
            return new TRectangle(r1.A - r2.A, r1.B - r2.B);
        }
    }
}
