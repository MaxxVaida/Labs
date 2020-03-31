using System;
using System.Collections.Generic;
using System.Text;

namespace Program
{
    class TParallelepiped : TRectangle
    {
        public double H { get; set; }
        public TParallelepiped(double a, double b, double h) : base(a, b)
        {
            H = h;
        }
        public TParallelepiped(double a)
        {
            H = a;
        }
        public TParallelepiped()
        {
            H = 1;
        }
        public virtual double getVolume()
        {
            return getPerimeter() * H + 2 * base.getSquare();
        }
        public static TParallelepiped operator +(TParallelepiped r1, TParallelepiped r2)
        {
            return new TParallelepiped(r1.A + r2.A, r1.B + r2.B, r1.H+r2.H);
        }
        public static TParallelepiped operator -(TParallelepiped r1, TParallelepiped r2)
        {
            return new TParallelepiped(r1.A - r2.A, r1.B - r2.B, r1.H-r2.H);
        }
        public static TParallelepiped operator* (TParallelepiped r1, double num)
        {
            return new TParallelepiped(r1.A * num, r1.B * num,r1.H*num);
        }
    }
}
