import unittest
from random import choice
from poly_divmod import *
from numpy import poly1d

class testPolyPrimeDivmod(unittest.TestCase):
    
    def random_p_poly(self,d,p):
        cs = []
        from random import choice
        residues = range(p)
        cs = [choice(residues) for term in range(d+1)]
        return (poly1d(cs))

    def setUp(self):
        # What is the highest power of x?
        range_of_degrees = 6

        # how many pairs of polynomials do you want to test?
        number_of_cases = 9
        
        from practical_sieve import primes_under_10000 as ppp
        self.cases = []
        
        rd = range(range_of_degrees)
        
        # generate this many polynomials:
        for i in range(number_of_cases):  
            p = choice(ppp)
            # choose random degree for f.
            df,dg = choice(rd), choice(rd)
            f,g = self.random_p_poly(df,p),self.random_p_poly(dg,p)
            self.cases.append((f,g,p))

        #test boundary case: f or g is zero
        zero = poly1d([0])
        p = choice(ppp)
        f = self.random_p_poly(df,p)
        self.cases.append((zero,f,p))

        # f mod zero is undefined!
        # see if you can catch it. 
        p = choice(ppp)
        f = self.random_p_poly(df,p)
        self.cases.append((f,zero,p))
         
        
    def tearDown(self):
        del self.cases

    def printReport(self,f,g,p,q,r,i):
        print 
        print '#'*8
        print "test #", i
        print '#'*8
        print
        print "f = "
        print f
        print "g = "
        print g
        print "p = ",p
        print "q = "
        print q
        print "r = "
        print r

    def testConstantCaseDivmod(self):
        print "Testing constant case..."
        from practical_sieve import primes_under_10000 as ppp
        cases = []
        for i in range(10):
            p = choice(ppp)
            a = choice(range(p))
            b = choice(range(p))
            f = poly1d([a])
            g = poly1d([b])
            cases.append((f,g,p))
        for case in cases: 
            q,r = poly_prime_divmod(f,g,p)
            self.assertTrue(r.order == 0 or r.order < g.order)
            h = reduce_prime_poly(g*q + r, p)
            self.assertEqual(f.order,h.order)
            self.assertEqual(f,h)
        
        
    def testDivmod(self):
        for i,(f,g,p) in enumerate(self.cases):
            try: 
                (q,r) = poly_prime_divmod(f,g,p)
                self.printReport(f,g,p,q,r,i)
                print "g = ", g
                print "r = ",r
                self.assertTrue(r.order == 0 or r.order < g.order)
                h = reduce_prime_poly(g*q + r, p)
                self.assertEqual(f.order,h.order)
                self.assertEqual(f,h)
            except(ZeroDivisionError):
                print "you can't divide or mod by zero"
                

if __name__ == '__main__':
    unittest.main()





    

# def test_from_book(self):
#     f = poly1d([7, 0, 1, 0,0,0,0,0,0, 7, 0, 1])
#     g = poly1d([-7,0, -1,0,0,7, 0, 1])
#     q,r = poly_prime_divmod(f,g,13)
#     h =
#     k = 
#     self.assertEqual(q,h)
#     self.assertEqual(r,k)
